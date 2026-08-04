import json
from html import escape
from typing import List, Dict, Any
from paper_schema import Paper
from pathlib import Path
from paper_generator import PaperCardGenerator

SITE_URL = "https://mrnerf.github.io/awesome-3D-gaussian-splatting/"
SITE_NAME = "Awesome 3D Gaussian Splatting"
SITE_TITLE = "Awesome 3D Gaussian Splatting — Searchable 3DGS Paper Database"
REPO_URL = "https://github.com/MrNeRF/awesome-3D-gaussian-splatting"
DATA_URL = "https://raw.githubusercontent.com/MrNeRF/awesome-3D-gaussian-splatting/main/awesome_3dgs_papers.yaml"

# Initialize card generator with templates directory
card_generator = PaperCardGenerator(Path(__file__).parent / 'templates')

def site_description(count: int) -> str:
    """One-sentence page description shared by the meta, Open Graph and card tags."""
    return (f"Searchable database of {count} 3D Gaussian Splatting papers — SLAM, dynamic and 4D "
            f"scenes, compression, avatars, relighting and real-time rendering. Filter by year and tag.")

def generate_year_options(entries: List[Dict[str, Any]]) -> str:
    """Generate HTML for year filter options."""
    years = sorted({str(e.get("year", "")) for e in entries if e.get("year")}, reverse=True)
    return "\n".join(f'<option value="{y}">{y}</option>' for y in years)

def generate_tag_filters(entries: List[Dict[str, Any]]) -> str:
    """Generate HTML for tag filters as real buttons so they are keyboard reachable."""
    all_tags = sorted(set(tag for entry in entries for tag in entry["tags"]))
    filtered_tags = [t for t in all_tags if not t.startswith("Year ")]
    return "\n".join(
        f'<button type="button" class="tag-filter" data-tag="{escape(t, quote=True)}" '
        f'aria-pressed="false" aria-label="{escape(t, quote=True)}: not filtered">'
        f'<span class="tag-filter-state" aria-hidden="true"></span>{escape(t)}</button>'
        for t in filtered_tags
    )

def generate_structured_data(entries: List[Dict[str, Any]], last_modified: str) -> str:
    """Schema.org description of the page and of the paper collection behind it.

    The list is described by size rather than enumerated: emitting 500+ ScholarlyArticle
    nodes would add roughly 8% to the transferred page for markup that has no rich result
    in web search. The Dataset node is what makes the collection eligible for Google
    Dataset Search.
    """
    count = len(entries)
    graph = [
        {
            "@type": "CollectionPage",
            "@id": SITE_URL + "#page",
            "url": SITE_URL,
            "name": SITE_TITLE,
            "description": site_description(count),
            "inLanguage": "en",
            "dateModified": last_modified,
            "isPartOf": {"@type": "WebSite", "url": SITE_URL, "name": SITE_NAME},
            "about": {"@type": "Thing", "name": "3D Gaussian Splatting"},
            "mainEntity": {
                "@type": "ItemList",
                "name": "3D Gaussian Splatting papers",
                "numberOfItems": count,
            },
        },
        {
            "@type": "Dataset",
            "@id": SITE_URL + "#dataset",
            "name": "Awesome 3D Gaussian Splatting paper database",
            "description": (
                f"A curated, continuously updated database of {count} research papers on 3D Gaussian "
                "Splatting (3DGS), each tagged by topic and linked to its paper, project page, code "
                "and video where available."
            ),
            "url": SITE_URL,
            "sameAs": REPO_URL,
            "license": "https://opensource.org/licenses/MIT",
            "isAccessibleForFree": True,
            "dateModified": last_modified,
            "keywords": [
                "3D Gaussian Splatting", "3DGS", "radiance fields", "novel view synthesis",
                "neural rendering", "SLAM", "computer vision", "computer graphics",
            ],
            "creator": {"@type": "Person", "name": "Janusch Patas", "url": "https://www.mrnerf.com"},
            "distribution": {
                "@type": "DataDownload",
                "encodingFormat": "application/x-yaml",
                "contentUrl": DATA_URL,
            },
        },
    ]
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, indent=2, ensure_ascii=False)

def generate_sitemap(last_modified: str) -> str:
    """Single-URL sitemap; the page is one document with a changing paper list."""
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        '  <url>\n'
        f'    <loc>{SITE_URL}</loc>\n'
        f'    <lastmod>{last_modified}</lastmod>\n'
        '    <changefreq>daily</changefreq>\n'
        '    <priority>1.0</priority>\n'
        '  </url>\n'
        '</urlset>\n'
    )

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
