def generate_html(entries: list[dict[str, any]]) -> None:
    html = f"""
<!DOCTYPE HTML>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>awesome-3D-gaussian-splatting</title>
    <link rel="shortcut icon" href="assets/favicon.ico" type="image/x-icon">
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
            font-family: 'Lato', sans-serif;
            margin: 0;
            padding: 20px;
            background-color: var(--bg-color);
            color: var(--text-color);
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}

        h1 {{
            text-align: center;
            font-size: 2.5rem;
            margin-bottom: 2rem;
            color: var(--text-color);
        }}

        .filters {{
            display: flex;
            gap: 1rem;
            margin-bottom: 2rem;
            flex-wrap: wrap;
        }}

        .search-box {{
            flex: 1;
            min-width: 300px;
            padding: 0.75rem 1rem;
            border: 1px solid var(--border-color);
            border-radius: 0.5rem;
            font-size: 1rem;
            outline: none;
            transition: border-color 0.2s;
        }}

        .search-box:focus {{
            border-color: var(--primary-color);
        }}

        .filter-select {{
            padding: 0.75rem 1rem;
            border: 1px solid var(--border-color);
            border-radius: 0.5rem;
            font-size: 1rem;
            min-width: 150px;
            outline: none;
            cursor: pointer;
        }}

        .papers-grid {{
            display: grid;
            gap: 2rem;
        }}

        .paper-card {{
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 0.75rem;
            padding: 1.5rem;
            transition: transform 0.2s, box-shadow 0.2s;
        }}

        .paper-card:hover {{
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }}

        .paper-title {{
            font-size: 1.25rem;
            font-weight: 600;
            color: var(--text-color);
            margin: 0 0 0.5rem 0;
        }}

        .paper-year {{
            color: var(--primary-color);
            font-weight: 600;
        }}

        .paper-authors {{
            color: #4b5563;
            margin: 0.5rem 0;
            font-size: 0.95rem;
        }}

        .paper-links {{
            display: flex;
            gap: 1rem;
            margin: 1rem 0;
            flex-wrap: wrap;
        }}

        .paper-link {{
            color: var(--primary-color);
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 0.25rem;
            font-size: 0.95rem;
        }}

        .paper-link:hover {{
            color: var(--hover-color);
        }}

        .paper-abstract {{
            margin-top: 1rem;
            font-size: 0.95rem;
            line-height: 1.5;
            color: #4b5563;
            display: none;
        }}

        .paper-abstract.show {{
            display: block;
        }}

        .abstract-toggle {{
            background: none;
            border: 1px solid var(--border-color);
            padding: 0.5rem 1rem;
            border-radius: 0.5rem;
            cursor: pointer;
            color: var(--text-color);
            font-size: 0.9rem;
            transition: all 0.2s;
        }}

        .abstract-toggle:hover {{
            background: #f3f4f6;
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
                min-width: auto;
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
                {generate_year_options(entries)}
            </select>
            <select id="categoryFilter" class="filter-select">
                <option value="all">All Categories</option>
                {generate_category_options(entries)}
            </select>
        </div>

        <div class="papers-grid">
            {generate_paper_cards(entries)}
        </div>

    </div>

    <script>
    document.addEventListener('DOMContentLoaded', function() {{
        const searchInput = document.getElementById('searchInput');
        const yearFilter = document.getElementById('yearFilter');
        const categoryFilter = document.getElementById('categoryFilter');
        const paperCards = document.querySelectorAll('.paper-row');

        // Handle abstract toggles
        document.querySelectorAll('.abstract-toggle').forEach(button => {{
            button.addEventListener('click', () => {{
                const abstract = button.nextElementSibling;
                abstract.classList.toggle('show');
                button.textContent = abstract.classList.contains('show') ? 'Hide Abstract' : 'Show Abstract';
            }});
        }});

        function filterPapers() {{
            const searchTerm = searchInput.value.toLowerCase();
            const selectedYear = yearFilter.value;
            const selectedCategory = categoryFilter.value;

            paperCards.forEach(card => {{
                const title = card.getAttribute('data-title').toLowerCase();
                const authors = card.getAttribute('data-authors').toLowerCase();
                const year = card.getAttribute('data-year');
                const category = card.getAttribute('data-category');

                const matchesSearch = title.includes(searchTerm) || authors.includes(searchTerm);
                const matchesYear = selectedYear === 'all' || year === selectedYear;
                const matchesCategory = selectedCategory === 'all' || category === selectedCategory;

                if (matchesSearch && matchesYear && matchesCategory) {{
                    card.classList.add('visible');
                }} else {{
                    card.classList.remove('visible');
                }}
            }});
        }}

        searchInput.addEventListener('input', filterPapers);
        yearFilter.addEventListener('change', filterPapers);
        categoryFilter.addEventListener('change', filterPapers);

        // Show all papers initially
        paperCards.forEach(card => card.classList.add('visible'));
    }});
    </script>
</body>
</html>
"""
    with open('index.html', 'w') as file:
        file.write(html)

def generate_year_options(entries):
    years = sorted(set(entry['year'] for entry in entries if entry['year']), reverse=True)
    return '\n'.join(f'<option value="{year}">{year}</option>' for year in years)

def generate_category_options(entries):
    categories = sorted(set(entry['category'] for entry in entries if entry['category']))
    return '\n'.join(f'<option value="{category}">{category}</option>' for category in categories)

def generate_paper_cards(entries):
    cards = ''
    for entry in entries:
        links = []
        if entry['project_page']:
            links.append(f"""<a href="{entry['project_page']}" class="paper-link" target="_blank">
                            <i class="fas fa-globe"></i> Project Page
                          </a>""")
        if entry['paper']:
            links.append(f"""<a href="{entry['paper']}" class="paper-link" target="_blank">
                            <i class="fas fa-file-alt"></i> Paper
                          </a>""")
        if entry['code']:
            links.append(f"""<a href="{entry['code']}" class="paper-link" target="_blank">
                            <i class="fas fa-code"></i> Code
                          </a>""")
        if entry['video']:
            links.append(f"""<a href="{entry['video']}" class="paper-link" target="_blank">
                            <i class="fas fa-video"></i> Video
                          </a>""")
        
        abstract_html = f"""
            <button class="abstract-toggle">Show Abstract</button>
            <div class="paper-abstract">
                {entry.get('abstract', 'No abstract available.')}
            </div>
        """ if entry.get('abstract') else ""

        card = f"""
            <div class="paper-row" data-title="{entry['title']}" data-authors="{entry['authors']}" 
                 data-year="{entry['year']}" data-category="{entry.get('category', '')}">
                <div class="paper-card">
                    <h2 class="paper-title">
                        {entry['title']} <span class="paper-year">({entry['year']})</span>
                    </h2>
                    <p class="paper-authors">{entry['authors']}</p>
                    <div class="paper-links">
                        {' '.join(links)}
                    </div>
                    {abstract_html}
                </div>
            </div>
        """
        cards += card

    return cards
