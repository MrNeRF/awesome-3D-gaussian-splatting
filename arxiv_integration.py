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
        
        Args:
            url_or_id (str): arXiv URL (e.g., 'https://arxiv.org/abs/2412.21206') 
                            or ID (e.g., '2412.21206')
        
        Returns:
            str: arXiv ID
        """
        # If it's a URL, parse it
        if url_or_id.startswith('http'):
            path = urlparse(url_or_id).path
            # Extract ID from path
            arxiv_id = path.split('/')[-1]
            return arxiv_id
        # Otherwise, assume it's already an ID
        return url_or_id

    def get_paper(self, url_or_id: str) -> Optional[Dict[str, Any]]:
        """
        Get paper information from arXiv using URL or ID.
        
        Args:
            url_or_id (str): arXiv URL or ID
            
        Returns:
            Optional[Dict[str, Any]]: Paper data in the format needed for the YAML editor
        """
        try:
            # Extract arXiv ID
            arxiv_id = self.extract_arxiv_id(url_or_id)
            
            # Search for specific paper
            search = arxiv.Search(
                id_list=[arxiv_id],
                max_results=1
            )
            
            results = list(self.client.results(search))
            
            if not results:
                return None
                
            paper = results[0]
            
            # Generate ID using the same pattern as in awesome_3dgs_parse.py
            first_author_last_name = paper.authors[0].name.split()[-1]
            year = paper.published.year
            first_title_word = paper.title.split()[0]
            paper_id = f"{first_author_last_name.lower()}{year}{first_title_word.lower()}"
            
            # Clean the ID by removing special characters
            paper_id = re.sub('[^\w\s]', '', paper_id)
            
            # Format authors
            authors = ", ".join([author.name for author in paper.authors])
            
            # Create entry in the required format
            entry = {
                "id": paper_id,
                "category": None,  # Can be filled in manually
                "title": paper.title,
                "authors": authors,
                "year": str(year),
                "abstract": paper.summary,
                "project_page": None,  # arXiv doesn't provide this
                "paper": f"https://arxiv.org/pdf/{arxiv_id}.pdf",
                "code": None,  # arXiv doesn't provide this
                "video": None,  # arXiv doesn't provide this
                "tags": ["Year " + str(year)]  # Basic tag with year
            }
            
            return entry
            
        except Exception as e:
            print(f"Error fetching from arXiv: {str(e)}")
            return None

    def append_to_yaml(self, entry: Dict[str, Any], filename: str = "awesome_3dgs_papers.yaml") -> bool:
        """
        Append a new entry to the YAML file.
        
        Args:
            entry (Dict[str, Any]): Paper entry to append
            filename (str): Path to the YAML file
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Read existing data
            with open(filename, 'r', encoding='utf-8') as file:
                data = yaml.safe_load(file)
            
            # Check if paper with same ID already exists
            if any(existing['id'] == entry['id'] for existing in data):
                print(f"Paper with ID {entry['id']} already exists")
                return False
            
            # Append new entry
            data.append(entry)
            
            # Write back to file
            with open(filename, 'w', encoding='utf-8') as file:
                yaml.dump(data, file, sort_keys=False, allow_unicode=True, width=1000)
            
            return True
            
        except Exception as e:
            print(f"Error appending to YAML: {str(e)}")
            return False