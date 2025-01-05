from pathlib import Path
import json
from typing import List
from paper_schema import Paper
from template_engine import TemplateEngine

class PaperCardGenerator:
    """Generates HTML for paper cards using templates."""
    
    def __init__(self, templates_dir: Path):
        """Initialize the generator with templates."""
        self.template = TemplateEngine(templates_dir / 'paper_card.html')
        self.fallback_url = "https://raw.githubusercontent.com/yangcaogit/3DGS-DET/main/assets/teaser.jpg"
    
    def _generate_link(self, url: str, icon: str, text: str) -> str:
        """Generate HTML for a paper link with icon."""
        return (f'<a href="{url}" class="paper-link" target="_blank" rel="noopener">'
                f'<i class="fas fa-{icon}"></i> {text}</a>')

    def _generate_links(self, paper: Paper) -> str:
        """Generate HTML for all paper links."""
        links = []
        if paper.project_page:
            links.append(self._generate_link(paper.project_page, "globe", "Project Page"))
        if paper.paper:
            links.append(self._generate_link(paper.paper, "file-alt", "Paper"))
        if paper.code:
            links.append(self._generate_link(paper.code, "code", "Code"))
        if paper.video:
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
            'abstract_html': self._generate_abstract(paper)
        }
        
        return self.template.render(context)

    def generate_cards(self, papers: List[Paper]) -> str:
        """Generate HTML for all paper cards."""
        return "\n".join(self.generate_card(paper) for paper in papers)