import arxiv
import yaml
import re
from urllib.parse import urlparse
from typing import Optional, Dict, Any
from pathlib import Path

class LiteralStr(str):
    pass

def literal_str_representer(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')

yaml.add_representer(LiteralStr, literal_str_representer)

class ArxivIntegration:
    def __init__(self):
        self.client = arxiv.Client()

    def extract_arxiv_id(self, url_or_id: str) -> str:
        """Extract arXiv ID from URL or return the ID if already in correct format."""
        url_or_id = url_or_id.strip()
        if not url_or_id.startswith('http'):
            url_or_id = 'https://' + url_or_id
        parsed = urlparse(url_or_id)
        path = parsed.path
        if 'abs' in path or 'pdf' in path:
            arxiv_id = path.split('/')[-1]
            if arxiv_id.endswith('.pdf'):
                arxiv_id = arxiv_id[:-4]
        else:
            arxiv_id = path.strip('/')
        if not re.match(r'^\d{4}\.\d{4,5}(?:v\d+)?$', arxiv_id):
            raise ValueError("Invalid arXiv ID format")
        return arxiv_id

    def get_paper(self, url_or_id: str) -> Optional[Dict[str, Any]]:
        """Fetch paper details from arXiv using its ID or URL."""
        try:
            arxiv_id = self.extract_arxiv_id(url_or_id)
            search = arxiv.Search(id_list=[arxiv_id], max_results=1)
            results = list(self.client.results(search))
            if not results:
                return None

            paper = results[0]
            first_author_last_name = paper.authors[0].name.split()[-1].lower()
            year = paper.published.year
            first_title_word = re.sub(r'[^\w\s]', '', paper.title.split()[0].lower())
            paper_id = f"{first_author_last_name}{year}{first_title_word}"
            authors = ', '.join([author.name for author in paper.authors])

            return {
                "id": paper_id,
                "title": paper.title,
                "authors": authors,
                "year": str(year),
                "abstract": LiteralStr(paper.summary),
                "project_page": None,
                "paper": f"https://arxiv.org/pdf/{arxiv_id}.pdf",
                "code": None,
                "video": None,
                "tags": [f"Year {year}"],
                "thumbnail": f"assets/thumbnails/{paper_id}.jpg"
            }
        except Exception as e:
            print(f"Error fetching from arXiv: {str(e)}")
            return None

    def append_to_yaml(self, entry: Dict[str, Any], filename: str = "awesome_3dgs_papers.yaml") -> bool:
        """Append a new entry to the YAML file."""
        try:
            # Load existing data or initialize empty list
            data = []
            if Path(filename).exists():
                with open(filename, 'r', encoding='utf-8') as file:
                    data = yaml.safe_load(file) or []

            # Check for duplicates
            if any(existing['id'] == entry['id'] for existing in data):
                print(f"Paper with ID {entry['id']} already exists")
                return False

            # Add new entry
            data.append(entry)

            # Write back to file
            with open(filename, 'w', encoding='utf-8') as file:
                yaml.dump(data, file, sort_keys=False, allow_unicode=True, default_style=None, default_flow_style=False)

            return True
        except Exception as e:
            print(f"Error appending to YAML: {str(e)}")
            return False
