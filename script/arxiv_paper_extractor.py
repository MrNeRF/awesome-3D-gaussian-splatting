import arxiv
from datetime import datetime, timedelta
import pytz
import re
import yaml
import argparse
from urllib.parse import urlparse

def clean_text(text):
    """Clean text by removing extra whitespace and newlines."""
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def extract_links_from_abstract(abstract):
    """Extract code and project page links from abstract."""
    code_patterns = [
        r'github\.com/[\w-]+/[\w-]+',
        r'gitlab\.com/[\w-]+/[\w-]+',
        r'code:.*?http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
    ]
    
    project_patterns = [
        r'project page:.*?http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
        r'project website:.*?http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
        r'webpage:.*?http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    ]
    
    code_links = set()
    project_pages = set()
    
    for pattern in code_patterns:
        matches = re.finditer(pattern, abstract, re.IGNORECASE)
        for match in matches:
            url = match.group(0)
            if not url.startswith('http'):
                url = 'https://' + url
            code_links.add(url)
    
    for pattern in project_patterns:
        matches = re.finditer(pattern, abstract, re.IGNORECASE)
        for match in matches:
            url = match.group(0).split(':', 1)[1].strip()
            if not url.startswith('http'):
                url = 'https://' + url
            project_pages.add(url)
    
    return list(code_links), list(project_pages)

def search_arxiv(keywords, days_back=1, max_results=100):
    """Search arXiv using the Client interface."""
    cutoff_date = datetime.now(pytz.UTC) - timedelta(days=days_back)
    unique_papers = {}
    
    client = arxiv.Client()
    
    for keyword in keywords:
        search = arxiv.Search(
            query=keyword,
            max_results=max_results,
            sort_by=arxiv.SortCriterion.SubmittedDate
        )
        
        for result in client.results(search):
            if result.published >= cutoff_date:
                code_links, project_pages = extract_links_from_abstract(result.summary)
                
                paper_info = {
                    'title': result.title,
                    'authors': [author.name for author in result.authors],
                    'published': result.published,
                    'abstract': result.summary,
                    'pdf_url': result.pdf_url,
                    'arxiv_url': result.entry_id,
                    'primary_category': result.primary_category,
                    'categories': result.categories,
                    'code_links': code_links,
                    'project_pages': project_pages,
                    'keywords_matched': set([keyword])
                }
                
                if result.entry_id in unique_papers:
                    unique_papers[result.entry_id]['keywords_matched'].add(keyword)
                else:
                    unique_papers[result.entry_id] = paper_info
    
    return sorted(
        unique_papers.values(),
        key=lambda x: x['published'],
        reverse=True
    )

def format_paper_yaml(paper):
    """Convert paper info to YAML format with clean text."""
    year = str(paper['published'].year)
    
    # Generate paper ID
    first_author = paper['authors'][0].split()[-1].lower()
    paper_id = f"{first_author}{year}{paper['title'].split()[0].lower()}"
    
    # Clean and format the data
    yaml_data = {
        'id': paper_id,
        'category': paper['primary_category'],
        'title': clean_text(paper['title']),
        'authors': clean_text(', '.join(paper['authors'])),
        'year': year,
        'abstract': clean_text(paper['abstract']),
        'project_page': paper['project_pages'][0] if paper['project_pages'] else None,
        'paper': paper['pdf_url'],
        'code': paper['code_links'][0] if paper['code_links'] else None,
        'video': None,
        'thumbnail_image': False,
        'thumbnail_video': False
    }
    
    return yaml_data

class CustomDumper(yaml.Dumper):
    """Custom YAML dumper that handles string literals properly."""
    def increase_indent(self, flow=False, indentless=False):
        return super().increase_indent(flow, False)

def represent_str(dumper, data):
    """Custom string representer for YAML."""
    if len(data.split('\n')) > 1:  # Check if string contains newlines
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)

# Register the custom string representer
yaml.add_representer(str, represent_str, Dumper=CustomDumper)

def format_yaml_output(papers):
    """Format papers as YAML with custom formatting."""
    yaml_papers = [format_paper_yaml(paper) for paper in papers]
    return yaml.dump(
        yaml_papers,
        sort_keys=False,
        allow_unicode=True,
        Dumper=CustomDumper,
        width=80,
        default_flow_style=False
    )

def print_results(papers, output_format='text'):
    """Print results in specified format."""
    if not papers:
        print("No papers found matching the criteria.")
        return
    
    if output_format == 'yaml':
        print(format_yaml_output(papers))
    else:
        print(f"\nFound {len(papers)} unique papers:\n")
        for paper in papers:
            print("=" * 100)
            print(f"Title: {clean_text(paper['title'])}")
            print(f"\nAuthors: {clean_text(', '.join(paper['authors']))}")
            print(f"Published: {paper['published'].strftime('%Y-%m-%d %H:%M:%S')} UTC")
            print(f"Category: {paper['primary_category']}")
            print(f"All Categories: {', '.join(paper['categories'])}")
            print(f"Matched Keywords: {', '.join(paper['keywords_matched'])}")
            print("\nAbstract:")
            print(clean_text(paper['abstract']))
            print("\nLinks:")
            print(f"ArXiv: {paper['arxiv_url']}")
            print(f"PDF: {paper['pdf_url']}")
            if paper['code_links']:
                print("\nCode Repositories:")
                for link in paper['code_links']:
                    print(f"- {link}")
            if paper['project_pages']:
                print("\nProject Pages:")
                for link in paper['project_pages']:
                    print(f"- {link}")
            print("\n" + "=" * 100 + "\n")

def main():
    parser = argparse.ArgumentParser(description='Search arXiv for papers')
    parser.add_argument('--keywords', nargs='+', default=[
        "gaussian splatting",
        "3D Gaussian",
        "2D Gaussian",
        "Surfels"
    ], help='Keywords to search for')
    parser.add_argument('--days', type=int, default=7,
                      help='Number of days to look back')
    parser.add_argument('--max-results', type=int, default=100,
                      help='Maximum results per keyword')
    parser.add_argument('--format', choices=['text', 'yaml'], default='text',
                      help='Output format')
    parser.add_argument('--output', type=str, help='Output file path')
    
    args = parser.parse_args()
    
    print(f"Searching for papers from the last {args.days} days with keywords: {', '.join(args.keywords)}")
    papers = search_arxiv(args.keywords, args.days, args.max_results)
    
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            if args.format == 'yaml':
                f.write(format_yaml_output(papers))
            else:
                import sys
                original_stdout = sys.stdout
                sys.stdout = f
                print_results(papers, 'text')
                sys.stdout = original_stdout
        print(f"Results written to {args.output}")
    else:
        print_results(papers, args.format)

if __name__ == "__main__":
    main()