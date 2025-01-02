import json
from typing import List, Dict, Any

def generate_html(entries: List[Dict[str, Any]]) -> None:
    """Generate HTML page with paper list using tags and card layout"""
    # Get all unique tags and years
    all_tags = sorted(set(tag for entry in entries for tag in entry['tags']))
    year_options = generate_year_options(entries)
    tag_filters = generate_tag_filters(all_tags)
    paper_cards = generate_paper_cards(entries)
    
    html = f"""<!DOCTYPE HTML>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>awesome-paper-list</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        :root {{
            --primary-color: #1772d0;
            --hover-color: #f09228;
            --bg-color: #ffffff;
            --card-bg: #ffffff;
            --border-color: #e5e7eb;
            --text-color: #1f2937;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: var(--bg-color);
            color: var(--text-color);
            line-height: 1.5;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }}

        h1 {{
            text-align: center;
            font-size: 2.5rem;
            margin-bottom: 2rem;
            color: var(--text-color);
        }}

        /* Search and Filter Styles */
        .filters {{
            display: flex;
            gap: 1rem;
            margin-bottom: 2rem;
            flex-wrap: wrap;
        }}

        .search-box {{
            flex: 1;
            min-width: 200px;
            padding: 0.75rem 1rem;
            border: 1px solid var(--border-color);
            border-radius: 0.5rem;
            font-size: 1rem;
        }}

        .filter-select {{
            padding: 0.75rem 1rem;
            border: 1px solid var(--border-color);
            border-radius: 0.5rem;
            min-width: 150px;
            background-color: white;
        }}

        /* Tag Styles */
        .tag-filters {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-bottom: 2rem;
        }}

        .tag-filter {{
            background: #f3f4f6;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 0.5rem;
            cursor: pointer;
            font-size: 0.9rem;
            transition: all 0.2s;
            color: var(--text-color);
        }}

        .tag-filter:hover {{
            background: #e5e7eb;
        }}

        .tag-filter.active {{
            background: var(--primary-color);
            color: white;
        }}

        /* Paper Card Styles */
        .papers-grid {{
            display: grid;
            gap: 2rem;
        }}

        .paper-card {{
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 0.75rem;
            padding: 2rem;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
            transition: transform 0.2s, box-shadow 0.2s;
        }}

        .paper-card:hover {{
            transform: translateY(-2px);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }}

        .paper-title {{
            font-size: 1.25rem;
            font-weight: 600;
            margin: 0 0 1rem 0;
            color: var(--text-color);
        }}

        .paper-authors {{
            color: #4b5563;
            margin-bottom: 1rem;
        }}

        .paper-tags {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-bottom: 1rem;
        }}

        .paper-tag {{
            background: #f3f4f6;
            padding: 0.25rem 0.75rem;
            border-radius: 0.5rem;
            font-size: 0.85rem;
            color: #4b5563;
        }}

        .paper-links {{
            display: flex;
            flex-wrap: wrap;
            gap: 1rem;
            margin-top: 1rem;
        }}

        .paper-link {{
            color: var(--primary-color);
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.5rem 1rem;
            background: #f3f4f6;
            border-radius: 0.5rem;
            transition: all 0.2s;
            font-size: 0.9rem;
        }}

        .paper-link:hover {{
            background: #e5e7eb;
            color: var(--hover-color);
        }}

        .abstract-toggle {{
            background: none;
            border: 1px solid var(--border-color);
            padding: 0.5rem 1rem;
            border-radius: 0.5rem;
            cursor: pointer;
            margin-top: 1rem;
            color: var(--text-color);
        }}

        .paper-abstract {{
            margin-top: 1rem;
            display: none;
            background: #f9fafb;
            padding: 1rem;
            border-radius: 0.5rem;
            color: #4b5563;
            line-height: 1.6;
        }}

        .paper-abstract.show {{
            display: block;
        }}

        .paper-row {{
            display: none;
        }}

        .paper-row.visible {{
            display: block;
        }}

        @media (max-width: 768px) {{
            .filters {{
                flex-direction: column;
            }}
            .search-box {{
                width: 100%;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>awesome-paper-list</h1>
        
        <div class="filters">
            <input type="text" id="searchInput" class="search-box" placeholder="Search papers by title or authors...">
            <select id="yearFilter" class="filter-select">
                <option value="all">All Years</option>
                {year_options}
            </select>
        </div>

        <div class="tag-filters" id="tagFilters">
            {tag_filters}
        </div>

        <div class="papers-grid">
            {paper_cards}
        </div>
    </div>

    <script>
    document.addEventListener('DOMContentLoaded', function() {{
        const searchInput = document.getElementById('searchInput');
        const yearFilter = document.getElementById('yearFilter');
        const paperCards = document.querySelectorAll('.paper-row');
        const tagFilters = document.querySelectorAll('.tag-filter');
        
        let selectedTags = new Set();

        // Handle abstract toggles
        document.querySelectorAll('.abstract-toggle').forEach(button => {{
            button.addEventListener('click', () => {{
                const abstract = button.nextElementSibling;
                abstract.classList.toggle('show');
                button.textContent = abstract.classList.contains('show') ? 'Hide Abstract' : 'Show Abstract';
            }});
        }});

        // Handle tag filtering
        tagFilters.forEach(tagFilter => {{
            tagFilter.addEventListener('click', () => {{
                const tag = tagFilter.getAttribute('data-tag');
                if (selectedTags.has(tag)) {{
                    selectedTags.delete(tag);
                    tagFilter.classList.remove('active');
                }} else {{
                    selectedTags.add(tag);
                    tagFilter.classList.add('active');
                }}
                filterPapers();
            }});
        }});

        function filterPapers() {{
            const searchTerm = searchInput.value.toLowerCase();
            const selectedYear = yearFilter.value;

            paperCards.forEach(card => {{
                const title = card.getAttribute('data-title').toLowerCase();
                const authors = card.getAttribute('data-authors').toLowerCase();
                const tags = JSON.parse(card.getAttribute('data-tags'));

                const matchesSearch = title.includes(searchTerm) || authors.includes(searchTerm);
                const matchesYear = selectedYear === 'all' || tags.includes(selectedYear);
                const matchesTags = selectedTags.size === 0 || 
                    [...selectedTags].every(tag => tags.includes(tag));

                if (matchesSearch && matchesYear && matchesTags) {{
                    card.classList.add('visible');
                }} else {{
                    card.classList.remove('visible');
                }}
            }});
        }}

        searchInput.addEventListener('input', filterPapers);
        yearFilter.addEventListener('change', filterPapers);

        // Show all papers initially
        paperCards.forEach(card => card.classList.add('visible'));
    }});
    </script>
</body>
</html>"""
    
    with open('index.html', 'w') as file:
        file.write(html)

def generate_year_options(entries: List[Dict[str, Any]]) -> str:
    """Generate HTML options for year filter"""
    years = sorted({tag.split()[-1] for entry in entries 
                   for tag in entry['tags'] if tag.startswith('Year ')}, 
                  reverse=True)
    return '\n'.join(f'<option value="Year {year}">Year {year}</option>' for year in years)

def generate_tag_filters(tags: List[str]) -> str:
    """Generate HTML for tag filters"""
    # Exclude year tags from the tag filters as they're handled by the dropdown
    filtered_tags = [tag for tag in sorted(tags) if not tag.startswith('Year ')]
    return '\n'.join(f'<div class="tag-filter" data-tag="{tag}">{tag}</div>' 
                     for tag in filtered_tags)

def generate_paper_cards(entries: List[Dict[str, Any]]) -> str:
    """Generate HTML for paper cards"""
    cards = []
    for entry in entries:
        # Generate links
        links = []
        if entry.get('project_page'):
            links.append(f"""<a href="{entry['project_page']}" class="paper-link" target="_blank">
                            <i class="fas fa-globe"></i> Project Page
                          </a>""")
        if entry.get('paper'):
            links.append(f"""<a href="{entry['paper']}" class="paper-link" target="_blank">
                            <i class="fas fa-file-alt"></i> Paper
                          </a>""")
        if entry.get('code'):
            links.append(f"""<a href="{entry['code']}" class="paper-link" target="_blank">
                            <i class="fas fa-code"></i> Code
                          </a>""")
        if entry.get('video'):
            links.append(f"""<a href="{entry['video']}" class="paper-link" target="_blank">
                            <i class="fas fa-video"></i> Video
                          </a>""")
        
        # Generate tags HTML (excluding year tags from display)
        display_tags = [tag for tag in entry['tags'] if not tag.startswith('Year ')]
        tags_html = '\n'.join(f'<span class="paper-tag">{tag}</span>' for tag in display_tags)
        
        # Generate abstract HTML if available
        abstract_html = f"""
            <button class="abstract-toggle">Show Abstract</button>
            <div class="paper-abstract">
                {entry.get('abstract', 'No abstract available.')}
            </div>
        """ if entry.get('abstract') else ""

        year_display = next((tag.split()[-1] for tag in entry['tags'] 
                           if tag.startswith('Year ')), 'N/A')

        # Generate card HTML
        card = f"""
            <div class="paper-row" 
                 data-title="{entry['title']}" 
                 data-authors="{entry['authors']}"
                 data-tags='{json.dumps(entry["tags"])}'>
                <div class="paper-card">
                    <h2 class="paper-title">
                        {entry['title']} <span class="paper-year">({year_display})</span>
                    </h2>
                    <p class="paper-authors">{entry['authors']}</p>
                    <div class="paper-tags">
                        {tags_html}
                    </div>
                    <div class="paper-links">
                        {' '.join(links)}
                    </div>
                    {abstract_html}
                </div>
            </div>
        """
        cards.append(card)
    
    return '\n'.join(cards)
