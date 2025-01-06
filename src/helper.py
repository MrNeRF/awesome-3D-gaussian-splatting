import datetime
from typing import List, Dict, Any
from paper_schema import Paper
from pathlib import Path
from paper_generator import PaperCardGenerator

# Initialize card generator with templates directory
card_generator = PaperCardGenerator(Path(__file__).parent / 'templates')

def generate_year_options(entries: List[Dict[str, Any]]) -> str:
    """Generate HTML for year filter options."""
    years = sorted({str(e.get("year", "")) for e in entries if e.get("year")}, reverse=True)
    return "\n".join(f'<option value="{y}">{y}</option>' for y in years)

def generate_tag_filters(entries: List[Dict[str, Any]]) -> str:
    """Generate HTML for tag filters."""
    all_tags = sorted(set(tag for entry in entries for tag in entry["tags"]))
    filtered_tags = [t for t in all_tags if not t.startswith("Year ")]
    return "\n".join(f'<div class="tag-filter" data-tag="{t}">{t}</div>' for t in filtered_tags)

def generate_paper_cards(entries: List[Dict[str, Any]]) -> str:
    """Generate HTML for paper cards using the Paper model and card generator."""
    # Convert dictionary entries to Paper objects with validation
    papers = []
    for entry in entries:
        try:
            paper = Paper.from_dict(entry)
            papers.append(paper)
        except ValueError as e:
            paper_id = entry.get('id', 'Unknown ID')
            title = entry.get('title', 'Unknown Title')
            print(f"Warning: Invalid paper entry '{paper_id}' ({title}): {e}")
            continue
    
    # Sort papers by publication date (newest first), then author, then title
    papers.sort(key=lambda p: (
        p.publication_date or '9999',  # Use '9999' for papers without dates
        p.authors.split(',')[0].strip().split()[-1].lower(),  # First author's last name
        p.title.lower()
    ), reverse=True)
    
    # Generate HTML using the card generator
    return card_generator.generate_cards(papers)

def format_publication_date(date_str: str, date_source: str) -> str:
    """Format publication date for display."""
    if not date_str:
        return ""
    try:
        date = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
        formatted_date = date.strftime("%B %d, %Y")
        source_indicator = " (est.)" if date_source == 'estimated' else ""
        return f"{formatted_date}{source_indicator}"
    except ValueError:
        return date_str