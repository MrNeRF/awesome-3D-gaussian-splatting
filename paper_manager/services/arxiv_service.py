import arxiv
from datetime import datetime, timedelta
import pytz
import re
from typing import List, Tuple, Set
from models.paper import Paper

class ArxivService:
    @staticmethod
    def clean_text(text: str) -> str:
        """Clean text by removing extra whitespace and newlines."""
        if not text:
            return ""
        return re.sub(r'\s+', ' ', text).strip()

    @staticmethod
    def extract_links_from_abstract(abstract: str) -> Tuple[List[str], List[str]]:
        """Extract code and project page links from abstract."""
        if not abstract:
            return [], []
            
        code_patterns = [
            r'github\.com/[\w-]+/[\w-]+',
            r'gitlab\.com/[\w-]+/[\w-]+',
            r'code:.*?http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
        ]
        
        project_patterns = [
            r'project page:.*?http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
            r'project website:.*?http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
            r'webpage:.*?http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        ]
        
        code_links: Set[str] = set()
        project_pages: Set[str] = set()
        
        for pattern in code_patterns:
            matches = re.finditer(pattern, abstract, re.IGNORECASE)
            for match in matches:
                url = match.group(0)
                if not url.startswith('http'):
                    url = 'https://' + url
                code_links.add(url)
        
        for pattern in project_patterns:
            matches = re.finditer(pattern, abstract, re.IGNORECASE)
            for match in matches:
                url = match.group(0).split(':', 1)[1].strip()
                if not url.startswith('http'):
                    url = 'https://' + url
                project_pages.add(url)
        
        return list(code_links), list(project_pages)

    @classmethod
    def search(cls, keywords: str, days_back: int) -> List[Paper]:
        formatted_keywords = cls._format_keywords(keywords)
        cutoff_date = datetime.now(pytz.UTC) - timedelta(days=days_back)
        client = arxiv.Client()
        
        papers = []
        for keyword in formatted_keywords:
            search = arxiv.Search(
                query=keyword,
                max_results=100,
                sort_by=arxiv.SortCriterion.SubmittedDate
            )
            
            for result in client.results(search):
                if result.published >= cutoff_date:
                    paper = cls._create_paper_from_result(result)
                    if not any(p.id == paper.id for p in papers):
                        papers.append(paper)
        
        return papers

    @classmethod
    def _format_keywords(cls, raw_keywords: str) -> List[str]:
        keywords = []
        current_keyword = []
        in_quotes = False
        
        for char in raw_keywords:
            if char == '"':
                in_quotes = not in_quotes
            elif char == ',' and not in_quotes:
                if current_keyword:
                    keywords.append(''.join(current_keyword).strip())
                current_keyword = []
            else:
                current_keyword.append(char)
        
        if current_keyword:
            keywords.append(''.join(current_keyword).strip())
        
        return [f'"{k}"' if ' ' in k and not (k.startswith('"') and k.endswith('"')) else k 
                for k in keywords]

    @classmethod
    def _create_paper_from_result(cls, result: arxiv.Result) -> Paper:
        code_links, project_pages = cls.extract_links_from_abstract(result.summary)
        first_author = result.authors[0].name.split()[-1].lower()
        paper_id = f"{first_author}{result.published.year}{result.title.split()[0].lower()}"
        
        return Paper(
            id=paper_id,
            category=result.primary_category,
            title=cls.clean_text(result.title),
            authors=cls.clean_text(', '.join([a.name for a in result.authors])),
            year=str(result.published.year),
            abstract=cls.clean_text(result.summary),
            project_page=project_pages[0] if project_pages else None,
            paper_url=result.pdf_url,
            code_url=code_links[0] if code_links else None
        )
