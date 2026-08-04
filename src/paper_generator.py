from pathlib import Path
import json
import re
from html import escape
from typing import List
from paper_schema import Paper
from template_engine import TemplateEngine

_TAG_RE = re.compile(r'<[^>]+>')

def _attr(value: str) -> str:
    """Plain-text, quote-safe version of a field for use inside an HTML attribute.

    Titles may carry inline markup (Sp<sup>2</sup>360) and quotes (GaussianSpa: An
    "Optimizing-Sparsifying" ...). Interpolated raw, either one terminates the attribute
    early and corrupts the row, which also truncates what the search filter can match on.
    """
    return escape(_TAG_RE.sub('', value or ''), quote=True)

class PaperCardGenerator:
    """Generates HTML for paper cards using templates."""
    
    def __init__(self, templates_dir: Path):
        self.template = TemplateEngine(templates_dir / 'paper_card.html')

    def _generate_link(self, url: str, icon: str, text: str, emoji: str = "") -> str:
        """Generate HTML for a paper link with icon and emoji."""
        if not url or url.lower() == 'none':
            return ""
        return (f'<a href="{url}" class="paper-link" target="_blank" rel="noopener">'
                f'{emoji} {text}</a>')

    def _generate_links(self, paper: Paper) -> str:
        """Generate HTML for all paper links in specified order."""
        links = []
        
        # Paper link is always first if available and valid
        if paper.paper and paper.paper.lower() != 'none':
            links.append(self._generate_link(paper.paper, "file-alt", "Paper", "📄"))
        
        # Optional links in specific order
        if paper.project_page and paper.project_page.lower() != 'none':
            links.append(self._generate_link(paper.project_page, "globe", "Project", "🌐"))
        if paper.code and paper.code.lower() != 'none':
            links.append(self._generate_link(paper.code, "code", "Code", "💻"))
        if paper.video and paper.video.lower() != 'none':
            links.append(self._generate_link(paper.video, "video", "Video", "🎥"))
        
        # Abstract is always last if present. <details> gives the disclosure behaviour
        # natively, so it works without JavaScript and is keyboard operable.
        if paper.abstract and paper.abstract.lower() != 'none':
            links.append(
                '<details class="paper-abstract-wrap">'
                '<summary class="abstract-toggle">📖 Abstract</summary>'
                f'<div class="paper-abstract">{paper.abstract}</div>'
                '</details>'
            )
        
        return "\n".join(links)

    def _generate_tags(self, paper: Paper) -> str:
        """Generate HTML for paper tags."""
        display_tags = [t for t in paper.tags if not t.startswith("Year ")]
        return "\n".join(f'<span class="paper-tag">{t}</span>' for t in display_tags)

    def generate_card(self, paper: Paper) -> str:
        """Generate HTML for a paper card using the template."""
        context = {
            'id': paper.id,
            'title': paper.title,
            'title_attr': _attr(paper.title),
            'authors': paper.authors,
            'authors_attr': _attr(paper.authors),
            'year': paper.year,
            'tags_json': json.dumps(paper.tags),
            'thumbnail': paper.thumbnail or f"assets/thumbnails/{paper.id}.jpg",
            'tags_html': self._generate_tags(paper),
            'links_html': self._generate_links(paper),
            'abstract_html': paper.abstract or ""
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