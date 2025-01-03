import arxiv
import yaml
import re
from datetime import datetime
from typing import Optional, Dict, Any
from urllib.parse import urlparse

class ArxivIntegration:
    def __init__(self):
        self.client = arxiv.Client()

    def extract_arxiv_id(self, url_or_id: str) -> str:
        """
        Extract arXiv ID from URL or return the ID if already in correct format.
        Handles various URL formats.
        """
        # Clean up the input
        url_or_id = url_or_id.strip()
        
        # If it doesn't start with http, add it
        if not url_or_id.startswith('http'):
            url_or_id = 'https://' + url_or_id
            
        # Parse the URL
        parsed = urlparse(url_or_id)
        
        # Extract ID from path
        path = parsed.path
        if 'abs' in path or 'pdf' in path:
            arxiv_id = path.split('/')[-1]
            # Remove .pdf extension if present
            if arxiv_id.endswith('.pdf'):
                arxiv_id = arxiv_id[:-4]
        else:
            # If it's already an ID format (YYMM.NNNNN)
            arxiv_id = path.strip('/')
            
        # Validate the ID format
        if not re.match(r'^\d{4}\.\d{4,5}(?:v\d+)?$', arxiv_id):
            raise ValueError("Invalid arXiv ID format")
            
        return arxiv_id

    def get_paper(self, url_or_id: str) -> Optional[Dict[str, Any]]:
        try:
            # Extract arXiv ID
            arxiv_id = self.extract_arxiv_id(url_or_id)
            
            # Search for specific paper
            search = arxiv.Search(id_list=[arxiv_id], max_results=1)
            results = list(self.client.results(search))
            
            if not results:
                return None
                
            paper = results[0]
            
            # Generate ID using paper details
            first_author_last_name = paper.authors[0].name.split()[-1].lower()
            year = paper.published.year
            first_title_word = re.sub('[^\w\s]', '', paper.title.split()[0].lower())
            paper_id = f"{first_author_last_name}{year}{first_title_word}"
            
            # Format authors
            authors = ', '.join([author.name for author in paper.authors])
            
            # Create entry with empty strings for optional fields
            entry = {
                "id": paper_id,
                "title": paper.title,
                "authors": authors,
                "year": str(year),
                "abstract": paper.summary,
                "project_page": "",
                "paper": f"https://arxiv.org/pdf/{arxiv_id}.pdf",
                "code": "",
                "video": "",
                "tags": [f"Year {year}"]
            }
            
            return entry
            
        except Exception as e:
            print(f"Error fetching from arXiv: {str(e)}")
            return None

    def append_to_yaml(self, entry: Dict[str, Any], filename: str = "awesome_3dgs_papers.yaml") -> bool:
        """
        Append a new entry to the YAML file while preserving formatting.
        """
        try:
            # Read existing file content as text
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Load data for duplicate checking
            data = yaml.safe_load(content)
            
            # Check for duplicates
            if any(existing['id'] == entry['id'] for existing in data):
                print(f"Paper with ID {entry['id']} already exists")
                return False
            
            # Clean the abstract text
            abstract = entry['abstract'].replace('\n', ' ').strip()
            if ':' in abstract:
                abstract = f"'{abstract}'"
                
            # Clean and quote the title if it contains colons
            title = entry['title'].replace('\n', ' ').strip()
            if ':' in title:
                title = f"'{title}'"
            
            # Clean the authors
            authors = entry['authors'].replace('\n', ' ').strip()
            
            # Handle optional fields - use empty string instead of 'null'
            project_page = entry.get('project_page')
            code = entry.get('code')
            video = entry.get('video')
            
            # Format the new entry manually to match existing style
            new_entry = f"""- id: {entry['id']}
  title: {title}
  authors: {authors}
  year: '{entry['year']}'
  abstract: {abstract}
  project_page: {project_page if project_page else ''}
  paper: {entry['paper']}
  code: {code if code else ''}
  video: {video if video else ''}
  thumbnail_image: false
  thumbnail_video: false
  tags:
{chr(10).join('  - ' + tag for tag in entry['tags'])}
  thumbnail: assets/thumbnails/{entry['id']}.jpg"""

            # Append the new entry to the file
            with open(filename, 'a', encoding='utf-8') as file:
                file.write('\n' + new_entry + '\n')
            
            return True
            
        except Exception as e:
            print(f"Error appending to YAML: {str(e)}")
            return False
