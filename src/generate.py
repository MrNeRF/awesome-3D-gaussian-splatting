import yaml
import sys
from pathlib import Path
from typing import List, Dict, Any
from helper import generate_year_options, generate_tag_filters, generate_paper_cards
from utils import read_files, write_output
from template_engine import TemplateEngine

def generate_html(entries: List[Dict[str, Any]], output_file: str) -> None:
    """Generate optimized HTML page while preserving design."""
    # Get base directory
    base_dir = Path(__file__).parent

    # Read CSS and JS files
    css_files = ['static/css/base.css', 'static/css/components.css', 'static/css/responsive.css']
    js_files = ['static/js/state.js', 'static/js/utils.js', 'static/js/filters.js', 
                'static/js/selection.js', 'static/js/sharing.js', 'static/js/main.js']
    
    css_content = read_files(base_dir, css_files)
    js_content = read_files(base_dir, js_files)

    # Initialize template engine
    template = TemplateEngine(base_dir / 'templates/index.html')

    # Prepare template context
    context = {
        'styles': '\n'.join(css_content),
        'scripts': '\n'.join(js_content),
        'year_options': generate_year_options(entries),
        'tag_filters': generate_tag_filters(entries),
        'paper_cards': generate_paper_cards(entries)
    }

    # Generate final HTML
    html = template.render(context)
    write_output(output_file, html)

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