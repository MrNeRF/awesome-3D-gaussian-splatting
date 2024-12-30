def generate_html(entries: list[dict[str, any]]) -> None:
    html = f"""
<!DOCTYPE HTML>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>awesome-paper-list</title>
    <link rel="shortcut icon" href="assets/favicon.ico" type="image/x-icon">
    <link rel="stylesheet" type="text/css" href="style.css">
    <style>
        .filter-container {{
            max-width: 1000px;
            margin: 20px auto;
            padding: 0 20px;
        }}
        .search-box {{
            width: 100%;
            padding: 8px 12px;
            margin-bottom: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 14px;
        }}
        .filter-selects {{
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
        }}
        .filter-select {{
            padding: 8px 12px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 14px;
        }}
        .paper-row {{
            display: none;
        }}
        .paper-row.visible {{
            display: table-row;
        }}
        @media (max-width: 768px) {{
            .filter-selects {{
                flex-direction: column;
            }}
        }}
    </style>
</head>
<body>
<table style="width:100%;max-width:1000px;border:0px;border-spacing:0px;border-collapse:separate;margin-right:auto;margin-left:auto;"><tbody>
<tr style="padding:0px">
    <td style="padding:0px">
        <table style="width:100%;border:0px;border-spacing:0px;border-collapse:separate;margin-right:auto;margin-left:auto;"><tbody>
        <tr>
            <td style="padding:0px;width:100%;vertical-align:middle">
                <h1>awesome-paper-list</h1>
            </td>
        </tr>
        </tbody></table>
        
        <div class="filter-container">
            <input type="text" id="searchInput" class="search-box" placeholder="Search papers by title or authors...">
            <div class="filter-selects">
                <select id="yearFilter" class="filter-select">
                    <option value="all">All Years</option>
                    {generate_year_options(entries)}
                </select>
                <select id="categoryFilter" class="filter-select">
                    <option value="all">All Categories</option>
                    {generate_category_options(entries)}
                </select>
            </div>
        </div>

        <table id="papers-table" style="width:100%;border:0px;border-spacing:0px;border-collapse:separate;margin-right:auto;margin-left:auto;"><tbody>
        {generate_paper_rows(entries)}
        </tbody></table>

        <table style="width:100%;border:0px;border-spacing:0px;border-collapse:separate;margin-right:auto;margin-left:auto;"><tbody>
        <tr>
            <td style="padding:0px">
                <br>
                <p style="text-align:right;font-size:small;">
                    This page was inspired by this <a href="https://github.com/jonbarron/jonbarron_website">template</a> created by <a href="https://jonbarron.info/">Jon Barron</a>.
                </p>
            </td>
        </tr>
        </tbody></table>
    </td>
</tr>
</table>

<script>
document.addEventListener('DOMContentLoaded', function() {{
    const searchInput = document.getElementById('searchInput');
    const yearFilter = document.getElementById('yearFilter');
    const categoryFilter = document.getElementById('categoryFilter');
    const paperRows = document.querySelectorAll('.paper-row');

    function filterPapers() {{
        const searchTerm = searchInput.value.toLowerCase();
        const selectedYear = yearFilter.value;
        const selectedCategory = categoryFilter.value;

        paperRows.forEach(row => {{
            const title = row.getAttribute('data-title').toLowerCase();
            const authors = row.getAttribute('data-authors').toLowerCase();
            const year = row.getAttribute('data-year');
            const category = row.getAttribute('data-category');

            const matchesSearch = title.includes(searchTerm) || authors.includes(searchTerm);
            const matchesYear = selectedYear === 'all' || year === selectedYear;
            const matchesCategory = selectedCategory === 'all' || category === selectedCategory;

            if (matchesSearch && matchesYear && matchesCategory) {{
                row.classList.add('visible');
            }} else {{
                row.classList.remove('visible');
            }}
        }});
    }}

    searchInput.addEventListener('input', filterPapers);
    yearFilter.addEventListener('change', filterPapers);
    categoryFilter.addEventListener('change', filterPapers);

    // Show all papers initially
    paperRows.forEach(row => row.classList.add('visible'));
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

def generate_paper_rows(entries):
    rows = ''
    for entry in entries:
        image_row = ''
        if entry['thumbnail_image'] and entry['thumbnail_video']:
            image_source = 'assets/' + entry['id'] + '.jpg'
            video_source = 'assets/' + entry['id'] + '.mp4'
            image_row = f"""
                <tr class="paper-row" data-title="{entry['title']}" data-authors="{entry['authors']}" data-year="{entry['year']}" data-category="{entry.get('category', '')}">
                    <td style="padding:20px;width:25%;vertical-align:middle">
                        <div class="one">
                            <div class="two" id='{entry['id']}_video'>
                                <video width=100% height=100% muted autoplay loop>
                                    <source src="{video_source}" type="video/mp4"> Your browser does not support the video tag.
                                </video>
                            </div>
                            <img id='{entry['id']}_image' src='{image_source}' width="160">
                        </div>
                        <script type="text/javascript">
                            function {entry['id']}_start() {{
                                document.getElementById('{entry['id']}_image').style.opacity = "0";
                                document.getElementById('{entry['id']}_video').style.opacity = "1";
                            }}
                
                            function {entry['id']}_stop() {{
                                document.getElementById('{entry['id']}_video').style.opacity = "0";
                                document.getElementById('{entry['id']}_image').style.opacity = "1";
                            }}
                            {entry['id']}_stop()
                        </script>
                    </td>"""
        else:
            image_source = 'assets/' + entry['id'] + '.jpg' if entry['thumbnail_image'] else 'assets/no_img_ph.jpg'
            image_row = f"""
                <tr class="paper-row" data-title="{entry['title']}" data-authors="{entry['authors']}" data-year="{entry['year']}" data-category="{entry.get('category', '')}">
                    <td style="padding:20px;width:25%;vertical-align:middle">
                        <div class="one">
                            <img src='{image_source}' width="160">
                        </div>
                    </td>"""

        links = []
        if entry['project_page']:
            links.append(f"<a href='{entry['project_page']}'>project page</a>")
        if entry['paper']:
            links.append(f"<a href='{entry['paper']}'>paper</a>")
        if entry['code']:
            links.append(f"<a href='{entry['code']}'>code</a>")
        if entry['video']:
            links.append(f"<a href='{entry['video']}'>video</a>")
        links = ' / '.join(links)

        row = image_row + f"""
                    <td style="padding:20px;width:75%;vertical-align:middle">
                        <span class="papertitle">{entry['title']}</span> &mdash; {entry['year']}
                        <p style="margin:0">{entry['authors']}</p>
                        {links}
                    </td>
                </tr>
        """
        rows += row

    return rows
