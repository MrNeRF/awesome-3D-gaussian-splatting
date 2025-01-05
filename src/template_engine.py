from string import Template as StringTemplate
from typing import Dict, Any
from pathlib import Path

class TemplateEngine:
    def __init__(self, template_path: Path):
        with open(template_path, 'r', encoding='utf-8') as f:
            self.template = StringTemplate(f.read())
    
    def render(self, context: Dict[str, Any]) -> str:
        """Render the template with the given context."""
        return self.template.substitute(context)