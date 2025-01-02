#!/usr/bin/env python3
from pathlib import Path
import yaml
import requests
from pdf2image import convert_from_bytes
from PIL import Image
import logging
import os
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ThumbnailGenerator:
    def __init__(self, output_dir: str = "assets/thumbnails"):
        """Initialize thumbnail generator with fixed dimensions"""
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        # Fixed dimensions for all thumbnails
        self.THUMB_WIDTH = 300
        self.THUMB_HEIGHT = 424  # Roughly A4 proportion

    def resize_existing_thumbnail(self, thumb_path: Path) -> bool:
        """Resize an existing thumbnail to match required dimensions"""
        try:
            with Image.open(thumb_path) as img:
                if img.size == (self.THUMB_WIDTH, self.THUMB_HEIGHT):
                    return True  # Already correct size
                
                # Create white background
                background = Image.new('RGB', (self.THUMB_WIDTH, self.THUMB_HEIGHT), 'white')
                
                # Resize maintaining aspect ratio
                img.thumbnail((self.THUMB_WIDTH, self.THUMB_HEIGHT), Image.Resampling.LANCZOS)
                
                # Center the image
                offset = ((self.THUMB_WIDTH - img.width) // 2,
                         (self.THUMB_HEIGHT - img.height) // 2)
                background.paste(img, offset)
                
                # Save with temporary name first
                temp_path = thumb_path.with_suffix('.tmp.jpg')
                background.save(temp_path, "JPEG", quality=85, optimize=True)
                
                # Replace original file
                temp_path.replace(thumb_path)
                logger.debug(f"Resized existing thumbnail: {thumb_path.name}")
                return True
                
        except Exception as e:
            logger.error(f"Error resizing thumbnail {thumb_path}: {str(e)}")
            return False

    def check_and_fix_thumbnail(self, paper_id: str) -> bool:
        """Check if thumbnail exists and has correct dimensions, fix if needed"""
        thumb_path = self.output_dir / f"{paper_id}.jpg"
        
        if not thumb_path.exists():
            return False
            
        try:
            with Image.open(thumb_path) as img:
                if img.size == (self.THUMB_WIDTH, self.THUMB_HEIGHT):
                    return True
                
                # Wrong size - resize it
                logger.debug(f"Thumbnail exists but wrong size for {paper_id}, resizing...")
                return self.resize_existing_thumbnail(thumb_path)
                
        except Exception as e:
            logger.error(f"Error checking thumbnail {paper_id}: {str(e)}")
            return False

    def download_pdf(self, url: str) -> bytes:
        """Download PDF with proper headers and content type checking"""
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'application/pdf,*/*'
        }
        
        # Special handling for OpenReview URLs
        if 'openreview.net' in url:
            headers['Accept'] = 'application/pdf'
            
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        
        # Check content type
        content_type = response.headers.get('Content-Type', '').lower()
        if 'pdf' not in content_type and not url.endswith('.pdf'):
            logger.warning(f"Warning: Content-Type is {content_type} for {url}")
        
        return response.content

    def create_thumbnail_from_pdf(self, pdf_content: bytes, paper_id: str) -> bool:
        """Create fixed-size thumbnail from PDF content"""
        try:
            images = convert_from_bytes(
                pdf_content,
                first_page=1,
                last_page=1,
                size=(self.THUMB_WIDTH, self.THUMB_HEIGHT)
            )
            
            if not images:
                return False
            
            # Create white background image
            background = Image.new('RGB', (self.THUMB_WIDTH, self.THUMB_HEIGHT), 'white')
            
            # Paste the PDF image onto the background, maintaining aspect ratio
            thumb = images[0]
            thumb.thumbnail((self.THUMB_WIDTH, self.THUMB_HEIGHT), Image.Resampling.LANCZOS)
            
            # Center the thumbnail
            offset = ((self.THUMB_WIDTH - thumb.width) // 2,
                     (self.THUMB_HEIGHT - thumb.height) // 2)
            background.paste(thumb, offset)
            
            # Save thumbnail
            thumb_path = self.output_dir / f"{paper_id}.jpg"
            background.save(thumb_path, "JPEG", quality=85, optimize=True)
            logger.debug(f"Created new thumbnail for {paper_id}")
            return True
            
        except Exception as e:
            logger.error(f"Error creating thumbnail for {paper_id}: {str(e)}")
            return False

    def process_paper(self, paper: dict) -> tuple[str, bool]:
        """Process a single paper entry"""
        paper_id = paper['id']
        
        # First check if thumbnail exists and has correct dimensions
        if self.check_and_fix_thumbnail(paper_id):
            logger.debug(f"Thumbnail already exists and correct for {paper_id}")
            return paper_id, True
            
        # If we need to create new thumbnail, check if we have PDF URL
        if not paper.get('paper'):
            logger.warning(f"No PDF URL for {paper_id}")
            return paper_id, False
            
        try:
            logger.debug(f"Downloading PDF for {paper_id}")
            pdf_content = self.download_pdf(paper['paper'])
            success = self.create_thumbnail_from_pdf(pdf_content, paper_id)
            return paper_id, success
        except Exception as e:
            logger.error(f"Error processing {paper_id}: {str(e)}")
            return paper_id, False

    def generate_all(self, yaml_path: str, max_workers: int = 4):
        """Generate thumbnails for all papers using parallel processing"""
        # Load YAML data
        with open(yaml_path) as f:
            papers = yaml.safe_load(f)
            
        logger.info(f"Processing {len(papers)} papers using {max_workers} workers")
        
        # Process papers in parallel with progress bar
        successful = 0
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Create futures for all papers
            future_to_paper = {
                executor.submit(self.process_paper, paper): paper 
                for paper in papers
            }
            
            # Process results with progress bar
            with tqdm(total=len(papers), desc="Generating thumbnails") as pbar:
                for future in as_completed(future_to_paper):
                    paper = future_to_paper[future]
                    try:
                        paper_id, success = future.result()
                        if success:
                            successful += 1
                            paper['thumbnail'] = f"{self.output_dir}/{paper_id}.jpg"
                    except Exception as e:
                        logger.error(f"Error processing paper {paper.get('id')}: {str(e)}")
                    pbar.update(1)
        
        logger.info(f"Successfully processed {successful}/{len(papers)} thumbnails")
        return papers

def main():
    parser = argparse.ArgumentParser(description="Generate thumbnails from PDF papers")
    parser.add_argument(
        "--yaml", 
        default="awesome_3dgs_papers.yaml",
        help="Path to YAML file containing paper information"
    )
    parser.add_argument(
        "--output", 
        default="assets/thumbnails",
        help="Output directory for thumbnails"
    )
    parser.add_argument(
        "--workers", 
        type=int, 
        default=4,
        help="Number of worker threads for parallel processing"
    )
    parser.add_argument(
        "--verbose", 
        action="store_true",
        help="Enable verbose logging"
    )
    
    args = parser.parse_args()
    
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    
    generator = ThumbnailGenerator(args.output)
    generator.generate_all(args.yaml, args.workers)

if __name__ == "__main__":
    main()