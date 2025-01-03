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
            
            # Create entry using None for empty fields
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

            # Clean and format fields
            def clean_and_quote(text: str) -> str:
                if not text:
                    return 'null'
                text = text.replace('\n', ' ').strip()
                # Remove any existing quotes
                text = text.strip("'\"")
                # Add single quotes if needed
                if any(char in text for char in ':[]{},\n'):
                    text = f"'{text}'"
                return text

            # Format optional fields
            def format_optional_field(value) -> str:
                if value is None or value == '':
                    return 'null'
                return value

            # Format the new entry with explicit newlines and indentation
            new_entry = [
                f"- id: {entry['id']}",
                f"  title: {clean_and_quote(entry['title'])}",
                f"  authors: {clean_and_quote(entry['authors'])}",
                f"  year: '{entry['year']}'",
                f"  abstract: {clean_and_quote(entry.get('abstract', ''))}",
                f"  project_page: {format_optional_field(entry.get('project_page'))}",
                f"  paper: {entry['paper']}",
                f"  code: {format_optional_field(entry.get('code'))}",
                f"  video: {format_optional_field(entry.get('video'))}",
                f"  thumbnail_image: false",
                f"  thumbnail_video: false",
                f"  tags:"
            ]
            
            # Add tags with single space indentation to match existing format
            for tag in entry.get('tags', []):
                new_entry.append(f"  - {tag}")  # Changed from 4 spaces to 2 spaces
                
            # Add thumbnail
            new_entry.append(f"  thumbnail: assets/thumbnails/{entry['id']}.jpg")
            
            # Join all lines with newlines
            final_entry = '\n'.join(new_entry)

            # Append the new entry to the file
            with open(filename, 'a', encoding='utf-8') as file:
                file.write('\n' + final_entry + '\n')
            
            return True
            
        except Exception as e:
            print(f"Error appending to YAML: {str(e)}")
            return False