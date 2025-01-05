import json
import yaml
import sys
from pathlib import Path
from typing import List, Dict, Any

def generate_html(entries: List[Dict[str, Any]], output_file: str) -> None:
    """Generate optimized HTML page while preserving design."""
    # Get base directory (where this script is located)
    base_dir = Path(__file__).parent

    # Read all required CSS files
    css_files = ['static/css/base.css', 'static/css/components.css', 'static/css/responsive.css']
    css_content = []
    for css_file in css_files:
        with open(base_dir / css_file, 'r', encoding='utf-8') as f:
            css_content.append(f.read())

    # Read all required JS files in order
    js_files = ['static/js/state.js', 'static/js/utils.js', 'static/js/filters.js', 'static/js/selection.js', 'static/js/sharing.js', 'static/js/main.js']
    js_content = []
    for js_file in js_files:
        with open(base_dir / js_file, 'r', encoding='utf-8') as f:
            js_content.append(f.read())

    # Generate year options
    years = sorted({str(e.get("year", "")) for e in entries if e.get("year")}, reverse=True)
    year_options = "\n".join(f'<option value="{y}">{y}</option>' for y in years)

    # Generate tag filters
    all_tags = sorted(set(tag for entry in entries for tag in entry["tags"]))
    filtered_tags = [t for t in all_tags if not t.startswith("Year ")]
    tag_filters = "\n".join(f'<div class="tag-filter" data-tag="{t}">{t}</div>' for t in filtered_tags)

    # Generate paper cards
    paper_cards = []
    for entry in entries:
        # Links
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

        # Tags
        display_tags = [t for t in entry["tags"] if not t.startswith("Year ")]
        tags_html = "\n".join(f'<span class="paper-tag">{t}</span>' for t in display_tags)

        # Abstract
        abstract_html = ""
        if entry.get("abstract"):
            abstract_html = (
                f'<button class="abstract-toggle">Show Abstract</button>\n'
                f'<div class="paper-abstract">{entry["abstract"]}</div>'
            )

        # Year
        year = entry.get("year", "N/A")

        # Thumbnail
        thumb_url = entry.get("thumbnail", f"assets/thumbnails/{entry['id']}.jpg")
        fallback_url = "https://raw.githubusercontent.com/yangcaogit/3DGS-DET/main/assets/teaser.jpg"

        # Build card
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

    # Build complete HTML
    html = '<!DOCTYPE HTML>\n<html lang="en">\n'
    html += '<head>\n'
    html += '  <meta charset="UTF-8">\n'
    html += '  <meta name="viewport" content="width=device-width, initial-scale=1">\n'
    html += '  <title>Awesome 3D Gaussian Splatting Paper List</title>\n\n'
    
    html += '  <!-- Preconnects -->\n'
    html += '  <link rel="preconnect" href="https://cdnjs.cloudflare.com">\n'
    html += '  <link rel="preconnect" href="https://raw.githubusercontent.com">\n\n'
    
    html += '  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">\n'
    html += '  <script src="https://cdnjs.cloudflare.com/ajax/libs/vanilla-lazyload/17.8.3/lazyload.min.js"></script>\n\n'
    
    # Add CSS
    html += '  <style>\n'
    html += '\n'.join(css_content)
    html += '  </style>\n'
    html += '</head>\n'
    html += '<body>\n'
    
    # Main content
    html += '  <div class="container">\n'
    html += '    <h1>MrNeRF\'s Awesome-3D-Gaussian-Splatting-Paper-List</h1>\n\n'
    
    # Donate box
    html += """    <div class="donate-box">
      <h3>Support This Project</h3>
      <p>If you find this resource helpful, consider supporting its development and maintenance.</p>
      <div class="bitcoin-info">
        <span class="bitcoin-label">Bitcoin:</span>
        <code class="bitcoin-address">bc1qz7z4c2cn46t7rkgsh7mr8tw9ssgctepzxrtqfw</code>
        <button class="copy-button" onclick="copyBitcoinAddress()">
          <i class="fas fa-copy"></i> Copy
        </button>
      </div>
    </div>
"""

    # Filter info
    html += """    <div class="filter-info">
      <h3>Filter Options</h3>
      <p><strong>Search:</strong> Enter paper title or author names, then click <i class="fas fa-times"></i> to clear.</p>
      <p><strong>Year:</strong> Filter by publication year</p>
      <p><strong>Tags:</strong> Click once to include (blue), twice to exclude (red), third time to remove filter</p>
      <p><strong>Selection:</strong> Use selection mode to pick and share specific papers</p>
    </div>
"""

    # Selection controls
    html += """    <div class="selection-controls">
      <button class="control-button secondary" onclick="toggleSelectionMode()">
        <i class="fas fa-times"></i> Exit Selection Mode
      </button>
      <div class="selection-counter">0 papers selected</div>
      <button class="control-button secondary" onclick="clearSelection()">
        <i class="fas fa-trash"></i> Clear Selection
      </button>
      <button class="control-button primary" onclick="showShareModal()">
        <i class="fas fa-share"></i> Share Selection
      </button>
    </div>
"""

    # Selection preview
    html += """    <div class="selection-preview">
      <div class="preview-header">Selected Papers</div>
      <div class="preview-container" id="selectionPreview"></div>
    </div>
"""

    # Share modal
    html += """    <div class="share-modal" id="shareModal">
      <div class="share-modal-content">
        <button class="share-modal-close" onclick="hideShareModal()">&times;</button>
        <div class="share-modal-header">
          <h2>Share Selected Papers</h2>
        </div>
        <div class="share-url-container">
          <input type="text" class="share-url-input" id="shareUrl" readonly>
          <button class="control-button primary" onclick="copyShareLink()">
            <i class="fas fa-copy"></i> Copy Link
          </button>
        </div>
      </div>
    </div>
"""

    # Filters bar
    html += f"""    <div class="filters">
      <div class="search-wrapper">
        <input type="text" id="searchInput" class="search-box" placeholder="Search papers by title or authors...">
        <button class="clear-search-btn" onclick="clearSearch()" title="Clear search">
          <i class="fas fa-times"></i>
        </button>
      </div>
      <select id="yearFilter" class="filter-select">
        <option value="all">All Years</option>
        {year_options}
      </select>
      <button class="control-button secondary" onclick="toggleSelectionMode()">
        <i class="fas fa-check-square"></i> Selection Mode
      </button>
    </div>

    <div class="tag-filters" id="tagFilters">
      {tag_filters}
    </div>

    <div class="papers-grid">
      {''.join(paper_cards)}
    </div>
  </div>
"""

    # Add JavaScript
    html += '\n  <script>\n'
    html += '\n'.join(js_content)
    html += '\n  </script>\n'
    
    html += '</body>\n</html>'

    # Write output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)

def main():
    if len(sys.argv) != 3:
        print("Usage: python generate.py <input_yaml> <output_html>")
        sys.exit(1)

    try:
        # Load YAML data
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            entries = yaml.safe_load(f)

        # Generate website
        generate_html(entries, sys.argv[2])
        print(f"Successfully generated {sys.argv[2]}")

    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()