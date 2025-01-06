import arxiv
import yaml
import re
from urllib.parse import urlparse
from typing import Optional, Dict, Any


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
            entry = {
                "id": paper_id,
                "title": paper.title,
                "authors": authors,
                "year": str(year),
                "abstract": paper.summary,
                "project_page": None,
                "paper": f"https://arxiv.org/pdf/{arxiv_id}.pdf",
                "code": None,
                "video": None,
                "tags": [f"Year {year}"],
                "thumbnail": f"assets/thumbnails/{paper_id}.jpg"
            }
            return entry
        except Exception as e:
            print(f"Error fetching from arXiv: {str(e)}")
            return None

    def append_to_yaml(self, entry: Dict[str, Any], filename: str = "awesome_3dgs_papers.yaml") -> bool:
        """Append a new entry to the YAML file while preserving formatting."""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
            data = yaml.safe_load(content) or []
            if any(existing['id'] == entry['id'] for existing in data):
                print(f"Paper with ID {entry['id']} already exists")
                return False
            formatted_entry = self.format_yaml_entry(entry)
            with open(filename, 'a', encoding='utf-8') as file:
                if not content.endswith('\n'):
                    file.write('\n')
                file.write(formatted_entry)
            return True
        except Exception as e:
            print(f"Error appending to YAML: {str(e)}")
            return False

    @staticmethod
    def format_yaml_entry(entry: Dict[str, Any]) -> str:
        """Format a single entry as a YAML block."""
        lines = [
            f"- id: {entry['id']}",
            f"  title: {clean_and_quote(entry['title'])}",
            f"  authors: {entry['authors']}",
            f"  year: '{entry['year']}'",
            f"  abstract: >",
        ]
        # Break long abstract into wrapped lines for readability
        abstract = entry.get('abstract', '').replace('\n', ' ')
        abstract_lines = re.findall(r'.{1,80}(?:\s|$)', abstract)
        lines.extend([f"    {line.strip()}" for line in abstract_lines])
        lines.extend([
            f"  project_page: {format_optional_field(entry.get('project_page'))}",
            f"  paper: {entry['paper']}",
            f"  code: {format_optional_field(entry.get('code'))}",
            f"  video: {format_optional_field(entry.get('video'))}",
            f"  tags:"
        ])
        for tag in sorted(entry.get('tags', [])):
            lines.append(f"  - {tag}")
        lines.append(f"  thumbnail: {entry['thumbnail']}")
        return '\n'.join(lines) + '\n'


def clean_and_quote(text: str) -> str:
    """Clean and quote text if needed."""
    if not text:
        return 'null'
    text = text.strip()
    if any(char in text for char in ':[]{},\n'):
        return f"'{text}'"
    return text


def format_optional_field(value) -> str:
    """Format optional fields for YAML."""
    return 'null' if not value else value
