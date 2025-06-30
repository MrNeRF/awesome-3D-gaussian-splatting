import yaml
import arxiv
import time
from datetime import datetime
from typing import Dict, Any, Optional, List, Tuple
import re
from concurrent.futures import ThreadPoolExecutor, as_completed

class YAMLUpdater:
    def __init__(self):
        self.client = arxiv.Client()
        self.failed_papers = []
        
    def extract_year_from_id(self, paper_id: str) -> Optional[int]:
        """Extract year from paper ID (e.g., 'smith2024gaussian' -> 2024)."""
        match = re.search(r'20\d{2}', paper_id)
        if match:
            return int(match.group(0))
        return None
        
    def extract_arxiv_id(self, url: str) -> Optional[str]:
        """Extract arXiv ID from paper URL."""
        if not url:
            return None
            
        if 'arxiv.org' in url:
            match = re.search(r'(\d{4}\.\d{4,5}(?:v\d+)?)', url)
            if match:
                return match.group(1)
        return None

    def get_fallback_date(self, entry: Dict[str, Any]) -> Optional[str]:
        """Create a fallback date from paper ID or year field."""
        # Try to get year from paper ID
        paper_id = entry.get('id', '')
        year = self.extract_year_from_id(paper_id)
        
        # If not found in ID, try year field
        if not year and 'year' in entry:
            try:
                year = int(entry['year'])
            except (ValueError, TypeError):
                pass
        
        if year:
            # Use middle of the year as approximate date
            return f"{year}-07-01T00:00:00"
            
        return None

    def process_paper(self, entry: Dict[str, Any]) -> Tuple[Dict[str, Any], bool]:
        """Process a single paper entry."""
        paper_id = entry.get('id', 'unknown')
        
        # Skip if already has date
        if 'publication_date' in entry:
            return entry, True
            
        paper_url = entry.get('paper', '')
        print(f"Processing {paper_id} - URL: {paper_url}")
        
        try:
            arxiv_id = self.extract_arxiv_id(paper_url)
            if arxiv_id:
                # Try to get date from arXiv
                search = arxiv.Search(id_list=[arxiv_id])
                results = list(self.client.results(search))
                
                if results:
                    entry['publication_date'] = results[0].published.isoformat()
                    entry['date_source'] = 'arxiv'
                    print(f"Updated {paper_id} with arXiv date {entry['publication_date']}")
                    return entry, True
            
            # If we couldn't get arXiv date, try fallback
            fallback_date = self.get_fallback_date(entry)
            if fallback_date:
                entry['publication_date'] = fallback_date
                entry['date_source'] = 'estimated'
                print(f"Updated {paper_id} with estimated date {fallback_date}")
                return entry, True
                
            self.failed_papers.append((paper_id, "No date source available"))
            return entry, False
            
        except Exception as e:
            self.failed_papers.append((paper_id, str(e)))
            return entry, False

    def safe_sort_key(self, x: Dict[str, Any]) -> tuple:
        """Safe sort key that handles None values."""
        pub_date = x.get('publication_date', '9999')
        
        # Get last name of first author
        authors = x.get('authors', '')
        if authors and isinstance(authors, str):
            first_author = authors.split(',')[0].strip()
            last_name = first_author.split()[-1].lower() if first_author else 'z'
        else:
            last_name = 'z'
            
        # Get title
        title = x.get('title', 'z')
        title = title.lower() if isinstance(title, str) else 'z'
        
        # Consider date source in sorting
        date_source = x.get('date_source', 'unknown')
        source_priority = {'arxiv': 0, 'estimated': 1, 'unknown': 2}
        
        return (pub_date, source_priority[date_source], last_name, title)

    def update_yaml_with_dates(self, filename: str = "awesome_3dgs_papers.yaml"):
        """Update YAML file with publication dates."""
        # Load existing YAML
        with open(filename, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)

        # Count papers needing updates
        papers_to_update = [p for p in data if 'publication_date' not in p]
        if not papers_to_update:
            print("No papers need date updates.")
            return data

        print(f"Found {len(papers_to_update)} papers needing date updates")

        # Process papers in parallel
        updated_count = {'arxiv': 0, 'estimated': 0}
        with ThreadPoolExecutor(max_workers=5) as executor:
            future_to_paper = {executor.submit(self.process_paper, entry): entry 
                             for entry in papers_to_update}
            
            for future in as_completed(future_to_paper):
                entry, success = future.result()
                if success and 'date_source' in entry:
                    updated_count[entry['date_source']] += 1

        # Sort entries
        try:
            data.sort(key=self.safe_sort_key, reverse=True)  # Newest first
        except Exception as e:
            print(f"Error during sorting: {str(e)}")

        # Save updated YAML
        with open(filename, 'w', encoding='utf-8') as file:
            yaml.dump(data, file, sort_keys=False, allow_unicode=True)

        # Print summary
        print("\nUpdate Summary:")
        print(f"Updated from arXiv: {updated_count['arxiv']} entries")
        print(f"Updated with estimated dates: {updated_count['estimated']} entries")
        print(f"Failed updates: {len(self.failed_papers)} entries")
        
        if self.failed_papers:
            print("\nFailed papers:")
            for paper_id, reason in self.failed_papers:
                print(f"- {paper_id}: {reason}")

        return data

if __name__ == "__main__":
    updater = YAMLUpdater()
    updater.update_yaml_with_dates()
