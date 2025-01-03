import json
from typing import List, Dict, Any

def generate_html(entries: List[Dict[str, Any]]) -> None:
    """Generate optimized HTML page while preserving design"""
    # Get all unique tags and years
    all_tags = sorted(set(tag for entry in entries for tag in entry['tags']))
    year_options = generate_year_options(entries)
    tag_filters = generate_tag_filters(all_tags)
    paper_cards = generate_paper_cards(entries)
    
    html = f"""<!DOCTYPE HTML>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Awesome 3D Gaussian Splatting Paper List</title>
    
    <!-- Preconnect to external resources -->
    <link rel="preconnect" href="https://cdnjs.cloudflare.com">
    <link rel="preconnect" href="https://raw.githubusercontent.com">
    
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    
    <!-- Add vanilla-lazyload -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/vanilla-lazyload/17.8.3/lazyload.min.js"></script>
    
    <style>
        /* Original styles preserved */
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
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            display: flex;
            gap: 1.5rem;
            position: relative;
        }}

        .paper-card:hover {{
            transform: translateY(-2px);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }}

        .paper-number {{
            position: absolute;
            top: -1rem;
            left: -1rem;
            background-color: var(--primary-color);
            color: white;
            width: 2rem;
            height: 2rem;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            z-index: 1;
        }}

        /* Thumbnail styles */
        .paper-thumbnail {{
            flex: 0 0 200px;
            height: 283px;   /* Maintain aspect ratio (1.414, like A4) */
            border-radius: 0.5rem;
            overflow: hidden;
            border: 1px solid var(--border-color);
            background-color: #f3f4f6;
            position: relative;
        }}

        .paper-thumbnail img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.2s;
        }}

        .paper-thumbnail img:hover {{
            transform: scale(1.05);
        }}

        .paper-content {{
            flex: 1;
            min-width: 0; /* Prevent content from overflowing */
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

        /* Performance optimizations that preserve design */
        .paper-thumbnail img.lazy:not(.loaded) {{
            opacity: 0;
        }}
        
        .paper-thumbnail img.lazy.loaded {{
            opacity: 1;
            transition: opacity 0.3s ease-in;
        }}

        @media (prefers-reduced-motion: reduce) {{
            .paper-card,
            .paper-thumbnail img {{
                transition: none;
            }}
        }}

        @media (max-width: 768px) {{
            .filters {{
                flex-direction: column;
            }}
            .search-box {{
                width: 100%;
            }}
            .paper-card {{
                flex-direction: column;
            }}
            
            .paper-thumbnail {{
                width: 100%;
                height: 200px;
                margin-bottom: 1rem;
            }}
            
            .paper-thumbnail img {{
                object-fit: contain;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Awesome-3D-Gaussian-Splatting-Paper-List</h1>
        
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
        // Initialize lazy loading
        const lazyLoadInstance = new LazyLoad({{
            elements_selector: ".lazy",
            callback_error: (img) => {{
                if (img.dataset.fallback) {{
                    img.src = img.dataset.fallback;
                }}
            }},
            callback_loaded: (img) => {{
                img.classList.add('loaded');
            }}
        }});

        const searchInput = document.getElementById('searchInput');
        const yearFilter = document.getElementById('yearFilter');
        const paperCards = document.querySelectorAll('.paper-row');
        const tagFilters = document.querySelectorAll('.tag-filter');
        
        let selectedTags = new Set();

        // Handle abstract toggles
        document.querySelectorAll('.abstract-toggle').forEach(button => {{
            button.addEventListener('click', () => {{
                const abstract = button.nextElementSibling;
                const isShown = abstract.classList.toggle('show');
                button.textContent = isShown ? 'Hide Abstract' : 'Show Abstract';
            }});
        }});

        // Handle tag filtering with debounce
        const debounce = (fn, delay) => {{
            let timeoutId;
            return (...args) => {{
                if (timeoutId) {{
                    clearTimeout(timeoutId);
                }}
                timeoutId = setTimeout(() => {{
                    fn.apply(null, args);
                }}, delay);
            }};
        }};

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

        function updatePaperNumbers() {{
            let number = 1;
            document.querySelectorAll('.paper-row.visible').forEach(card => {{
                const numberElement = card.querySelector('.paper-number');
                numberElement.textContent = number++;
            }});
        }}

        const filterPapers = debounce(() => {{
            const searchTerm = searchInput.value.toLowerCase();
            const selectedYear = yearFilter.value;

            paperCards.forEach(card => {{
                const title = card.getAttribute('data-title').toLowerCase();
                const authors = card.getAttribute('data-authors').toLowerCase();
                const year = card.getAttribute('data-year');
                const tags = JSON.parse(card.getAttribute('data-tags'));

                const matchesSearch = title.includes(searchTerm) || authors.includes(searchTerm);
                const matchesYear = selectedYear === 'all' || year === selectedYear;
                const matchesTags = selectedTags.size === 0 || 
                    [...selectedTags].every(tag => tags.includes(tag));

                if (matchesSearch && matchesYear && matchesTags) {{
                    card.classList.add('visible');
                }} else {{
                    card.classList.remove('visible');
                }}
            }});
            
            updatePaperNumbers();
            lazyLoadInstance.update();
        }}, 150);

        searchInput.addEventListener('input', filterPapers);
        yearFilter.addEventListener('change', filterPapers);

        // Show all papers initially and set initial numbers
        paperCards.forEach(card => card.classList.add('visible'));
        updatePaperNumbers();
    }});
    </script>
</body>
</html>"""
    
    with open('index.html', 'w') as file:
        file.write(html)

def generate_year_options(entries: List[Dict[str, Any]]) -> str:
    """Generate HTML options for year filter"""
    years = sorted({str(entry.get('year', '')) for entry in entries if entry.get('year')}, 
                  reverse=True)
    return '\n'.join(f'<option value="{year}">{year}</option>' for year in years)

def generate_tag_filters(tags: List[str]) -> str:
    """Generate HTML for tag filters"""
    filtered_tags = [tag for tag in sorted(tags) if not tag.startswith('Year ')]
    return '\n'.join(f'<div class="tag-filter" data-tag="{tag}">{tag}</div>' 
                     for tag in filtered_tags)

def generate_paper_cards(entries: List[Dict[str, Any]]) -> str:
    """Generate HTML for paper cards with optimized loading while preserving design"""
    cards = []
    for entry in entries:
        # Generate links with security attributes
        links = []
        if entry.get('project_page'):
            links.append(f"""<a href="{entry['project_page']}" class="paper-link" target="_blank" rel="noopener">
                            <i class="fas fa-globe"></i> Project Page
                          </a>""")
        if entry.get('paper'):
            links.append(f"""<a href="{entry['paper']}" class="paper-link" target="_blank" rel="noopener">
                            <i class="fas fa-file-alt"></i> Paper
                          </a>""")
        if entry.get('code'):
            links.append(f"""<a href="{entry['code']}" class="paper-link" target="_blank" rel="noopener">
                            <i class="fas fa-code"></i> Code
                          </a>""")
        if entry.get('video'):
            links.append(f"""<a href="{entry['video']}" class="paper-link" target="_blank" rel="noopener">
                            <i class="fas fa-video"></i> Video
                          </a>""")
        
        # Generate tags HTML (excluding year tags)
        display_tags = [tag for tag in entry['tags'] if not tag.startswith('Year ')]
        tags_html = '\n'.join(f'<span class="paper-tag">{tag}</span>' for tag in display_tags)
        
        # Generate abstract HTML if available
        abstract_html = f"""
            <button class="abstract-toggle">Show Abstract</button>
            <div class="paper-abstract">
                {entry.get('abstract', 'No abstract available.')}
            </div>
        """ if entry.get('abstract') else ""

        year = entry.get('year', 'N/A')
        
        # Prepare thumbnail URL with fallback
        thumbnail_url = entry.get('thumbnail', f'assets/thumbnails/{entry["id"]}.jpg')
        fallback_url = 'https://raw.githubusercontent.com/yangcaogit/3DGS-DET/main/assets/teaser.jpg'

        # Generate card HTML with optimized loading while preserving design
        card = f"""
            <div class="paper-row" 
                 data-title="{entry['title']}" 
                 data-authors="{entry['authors']}"
                 data-year="{year}"
                 data-tags='{json.dumps(entry["tags"])}'>
                <div class="paper-card">
                    <div class="paper-number"></div>
                    <div class="paper-thumbnail">
                        <img data-src="{thumbnail_url}"
                             data-fallback="{fallback_url}"
                             alt="Paper thumbnail for {entry['title']}"
                             class="lazy"
                             loading="lazy"/>
                    </div>
                    <div class="paper-content">
                        <h2 class="paper-title">
                            {entry['title']} <span class="paper-year">({year})</span>
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
            </div>
        """
        cards.append(card)
    
    return '\n'.join(cards)