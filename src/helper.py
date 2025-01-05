from typing import List, Dict, Any
import json

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
    """Generate HTML for paper cards."""
    paper_cards = []
    for entry in entries:
        # Generate links
        links = []
        if entry.get("project_page"):
            links.append(f'<a href="{entry["project_page"]}" class="paper-link" target="_blank" rel="noopener">'
                        '<i class="fas fa-globe"></i> Project Page</a>')
        if entry.get("paper"):
            links.append(f'<a href="{entry["paper"]}" class="paper-link" target="_blank" rel="noopener">'
                        '<i class="fas fa-file-alt"></i> Paper</a>')
        if entry.get("code"):
            links.append(f'<a href="{entry["code"]}" class="paper-link" target="_blank" rel="noopener">'
                        '<i class="fas fa-code"></i> Code</a>')
        if entry.get("video"):
            links.append(f'<a href="{entry["video"]}" class="paper-link" target="_blank" rel="noopener">'
                        '<i class="fas fa-video"></i> Video</a>')

        # Generate tags
        display_tags = [t for t in entry["tags"] if not t.startswith("Year ")]
        tags_html = "\n".join(f'<span class="paper-tag">{t}</span>' for t in display_tags)

        # Generate abstract section
        abstract_html = ""
        if entry.get("abstract"):
            abstract_html = (
                f'<button class="abstract-toggle">Show Abstract</button>\n'
                f'<div class="paper-abstract">{entry["abstract"]}</div>'
            )

        year = entry.get("year", "N/A")
        thumb_url = entry.get("thumbnail", f"assets/thumbnails/{entry['id']}.jpg")
        fallback_url = "https://raw.githubusercontent.com/yangcaogit/3DGS-DET/main/assets/teaser.jpg"

        # Build card HTML
        card = (
            f'<div class="paper-row" data-id="{entry["id"]}" '
            f'data-title="{entry["title"]}" '
            f'data-authors="{entry["authors"]}" '
            f'data-year="{year}" '
            f'data-tags=\'{json.dumps(entry["tags"])}\'>\n'
            '  <div class="paper-card">\n'
            f'    <input type="checkbox" class="selection-checkbox" onclick="handleCheckboxClick(event, \'{entry["id"]}\', this)">\n'
            '    <div class="paper-number"></div>\n'
            '    <div class="paper-thumbnail">\n'
            f'      <img data-src="{thumb_url}" data-fallback="{fallback_url}" '
            f'alt="Paper thumbnail for {entry["title"]}" class="lazy" loading="lazy"/>\n'
            '    </div>\n'
            '    <div class="paper-content">\n'
            f'      <h2 class="paper-title">{entry["title"]} <span class="paper-year">({year})</span></h2>\n'
            f'      <p class="paper-authors">{entry["authors"]}</p>\n'
            f'      <div class="paper-tags">{tags_html}</div>\n'
            f'      <div class="paper-links">{" ".join(links)}</div>\n'
            f'      {abstract_html}\n'
            '    </div>\n'
            '  </div>\n'
            '</div>'
        )
        paper_cards.append(card)
    
    return "\n".join(paper_cards)
