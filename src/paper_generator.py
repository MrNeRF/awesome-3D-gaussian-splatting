from pathlib import Path
import json
from typing import List
from paper_schema import Paper
from template_engine import TemplateEngine

class PaperCardGenerator:
    """Generates HTML for paper cards using templates."""
    
    def __init__(self, templates_dir: Path):
        self.template = TemplateEngine(templates_dir / 'paper_card.html')
        self.fallback_url = "https://raw.githubusercontent.com/yangcaogit/3DGS-DET/main/assets/teaser.jpg"

    def _generate_link(self, url: str, icon: str, text: str) -> str:
        """Generate HTML for a paper link with icon."""
        if not url:  # Skip if URL is None, empty string, or whitespace
            return ""
        return (f'<a href="{url}" class="paper-link" target="_blank" rel="noopener">'
                f'<i class="fas fa-{icon}"></i> {text}</a>')

    def _generate_links(self, paper: Paper) -> str:
        """Generate HTML for all paper links."""
        links = []
        # Helper function to validate non-empty and meaningful URLs
        def is_valid_url(url):
            return bool(url and url.strip() and url.startswith(('http://', 'https://')))

        if is_valid_url(paper.project_page):
            links.append(self._generate_link(paper.project_page, "globe", "Project Page"))
        if is_valid_url(paper.paper):
            links.append(self._generate_link(paper.paper, "file-alt", "Paper"))
        if is_valid_url(paper.code):
            links.append(self._generate_link(paper.code, "code", "Code"))
        if is_valid_url(paper.video):
            links.append(self._generate_link(paper.video, "video", "Video"))
        
        return " ".join(links)

    def _generate_tags(self, paper: Paper) -> str:
        """Generate HTML for paper tags."""
        display_tags = [t for t in paper.tags if not t.startswith("Year ")]
        return "\n".join(f'<span class="paper-tag">{t}</span>' for t in display_tags)

    def _generate_abstract(self, paper: Paper) -> str:
        """Generate HTML for paper abstract section."""
        if not paper.abstract:
            return ""
        return (
            '<button class="abstract-toggle">Show Abstract</button>\n'
            f'<div class="paper-abstract">{paper.abstract}</div>'
        )

    def generate_card(self, paper: Paper) -> str:
        """Generate HTML for a paper card using the template."""
        # Prepare template context
        context = {
            'id': paper.id,
            'title': paper.title,
            'authors': paper.authors,
            'year': paper.year,
            'tags_json': json.dumps(paper.tags),
            'thumbnail': paper.thumbnail or f"assets/thumbnails/{paper.id}.jpg",
            'fallback_url': self.fallback_url,
            'tags_html': self._generate_tags(paper),
            'links_html': self._generate_links(paper),
            'abstract_html': self._generate_abstract(paper),
            'publication_date': paper.publication_date or ''
        }
        
        return self.template.render(context)

    def generate_cards(self, papers: List[Paper]) -> str:
        """Generate HTML for all paper cards."""
        # Sort papers by publication date (newest first), then author, then title
        sorted_papers = sorted(papers, 
            key=lambda p: (p.publication_date or '9999',
                         p.authors.split(',')[0].strip().split()[-1].lower(),
                         p.title.lower()),
            reverse=True
        )
        return "\n".join(self.generate_card(paper) for paper in sorted_papers)