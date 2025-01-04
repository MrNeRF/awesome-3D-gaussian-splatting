import yaml
import sys
import os
import requests
import time
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from github import Github

# Configure requests for better reliability
session = requests.Session()
retries = Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[408, 429, 500, 502, 503, 504],
    allowed_methods=["HEAD", "GET"]
)
adapter = HTTPAdapter(max_retries=retries)
session.mount('http://', adapter)
session.mount('https://', adapter)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
}

allowed_tags = [
    "2DGS", "360 degree", "Acceleration", "Antialiasing", "Autonomous Driving", 
    "Avatar", "Classic Work", "Code", "Compression", "Deblurring", "Densification",
    "Diffusion", "Distributed", "Dynamic", "Editing", "Event Camera", "Feed-Forward", 
    "GAN", "Inpainting", "In the Wild", "Language Embedding", "Large-Scale", "Lidar", 
    "Medicine", "Meshing", "Misc", "Monocular", "Perspective-correct", "Object Detection", 
    "Optimization", "Physics", "Point Cloud", "Poses", "Project", "Ray Tracing", 
    "Rendering", "Relight", "Review", "Robotics", "Segmentation", "SLAM", "Sparse", 
    "Stereo", "Style Transfer", "Texturing", "Transformer", "Uncertainty", "Video", 
    "Virtual Reality", "World Generation"
]

def validate_url(url, required=False):
    """Validate URL with fallback to GET if HEAD fails"""
    if not url:
        return None if not required else "URL is missing or empty"
        
    try:
        # First try HEAD request
        response = session.head(url, headers=headers, timeout=30, allow_redirects=True)
        
        # If HEAD fails, try GET
        if response.status_code in [405, 400, 403]:
            response = session.get(url, headers=headers, timeout=30, allow_redirects=True, stream=True)
            response.close()
        
        valid_codes = {200, 301, 302, 303, 307, 308}
        if response.status_code not in valid_codes:
            return f"URL returns {response.status_code}"
            
        return None
            
    except requests.Timeout:
        return "URL timed out"
    except requests.RequestException as e:
        return f"Error accessing URL: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"

def get_changed_entries():
    """Get entries that were changed or added in this PR"""
    # Initialize GitHub client
    g = Github(os.getenv('GITHUB_TOKEN'))
    repo = g.get_repo(os.getenv('REPO'))
    pr = repo.get_pull(int(os.getenv('PR_NUMBER')))
    
    # Load both versions of the YAML file
    with open("awesome_3dgs_papers.yaml", 'r') as file:
        new_yaml = yaml.safe_load(file)
    
    try:
        # Get base content
        base_content = repo.get_contents("awesome_3dgs_papers.yaml", ref=pr.base.sha).decoded_content.decode()
        base_yaml = yaml.safe_load(base_content)
    except:
        # If file doesn't exist in base, all entries are new
        base_yaml = []
    
    # Create dictionary of existing entries by ID
    base_entries = {entry['id']: entry for entry in base_yaml} if base_yaml else {}
    
    # Find changed or new entries
    changed_entries = []
    for entry in new_yaml:
        entry_id = entry['id']
        if entry_id not in base_entries:
            print(f"New entry found: {entry_id}")
            changed_entries.append(entry)
        elif entry != base_entries[entry_id]:
            print(f"Modified entry found: {entry_id}")
            changed_entries.append(entry)
    
    return changed_entries

def validate_entries(entries):
    """Validate the specified entries"""
    errors = []
    url_fields = {
        'paper': True,
        'project_page': False,
        'code': False,
        'video': False
    }

    # Load full YAML to get entry numbers
    with open("awesome_3dgs_papers.yaml", 'r') as file:
        all_entries = yaml.safe_load(file)
    
    # Create index lookup
    entry_indices = {entry['id']: idx + 1 for idx, entry in enumerate(all_entries)}

    for entry in entries:
        # Basic validation
        if not entry.get('id'):
            errors.append("Entry missing ID")
            continue

        entry_num = entry_indices.get(entry['id'], '?')
        print(f"\nValidating entry #{entry_num}: {entry['id']}")

        # Tags validation
        tags = entry.get('tags', [])
        if not tags:
            errors.append(f"Entry {entry['id']}: No tags provided")
        else:
            invalid_tags = [tag for tag in tags if not tag.startswith('Year ') and tag not in allowed_tags]
            if invalid_tags:
                errors.append(f"Entry {entry['id']}: Invalid tags: {invalid_tags}")
            
            non_year_tags = [tag for tag in tags if not tag.startswith('Year ')]
            if not non_year_tags:
                errors.append(f"Entry {entry['id']}: Must have at least one non-Year tag")

        # URL validation
        for field, required in url_fields.items():
            value = entry.get(field)
            if value or required:
                print(f"Checking {field} URL: {value}")
                error = validate_url(value, required)
                if error:
                    errors.append(f"Entry {entry['id']}: {field} {error}")
                # Add delay between requests
                time.sleep(1)

    return errors

def main():
    try:
        changed_entries = get_changed_entries()
        if not changed_entries:
            print("No entries were changed in this PR")
            sys.exit(0)

        print(f"\nFound {len(changed_entries)} changed/new entries to validate")
        errors = validate_entries(changed_entries)

        if errors:
            print("\n❌ Validation errors found:")
            for error in errors:
                print(error)
            sys.exit(1)
        else:
            print("\n✅ All changed entries passed validation!")

    except Exception as e:
        print(f"\n❌ Error during validation: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
