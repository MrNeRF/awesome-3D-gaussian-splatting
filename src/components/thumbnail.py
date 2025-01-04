from pathlib import Path
import requests
from pdf2image import convert_from_bytes
from PIL import Image
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ThumbnailGenerator:
    def __init__(self, output_dir: str = "assets/thumbnails"):
        """Initialize thumbnail generator with fixed dimensions"""
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.THUMB_WIDTH = 300
        self.THUMB_HEIGHT = 424  # Roughly A4 proportion

    def download_pdf(self, url: str) -> bytes:
        """Download PDF with proper headers"""
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36',
            'Accept': 'application/pdf,*/*'
        }
        
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        return response.content

    def create_thumbnail(self, pdf_content: bytes, paper_id: str) -> bool:
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
            
            # Create white background
            background = Image.new('RGB', (self.THUMB_WIDTH, self.THUMB_HEIGHT), 'white')
            
            # Paste the PDF image onto background
            thumb = images[0]
            thumb.thumbnail((self.THUMB_WIDTH, self.THUMB_HEIGHT), Image.Resampling.LANCZOS)
            
            # Center the thumbnail
            offset = ((self.THUMB_WIDTH - thumb.width) // 2,
                     (self.THUMB_HEIGHT - thumb.height) // 2)
            background.paste(thumb, offset)
            
            # Save thumbnail
            thumb_path = self.output_dir / f"{paper_id}.jpg"
            background.save(thumb_path, "JPEG", quality=85, optimize=True)
            logger.info(f"Created thumbnail for {paper_id}")
            return True
            
        except Exception as e:
            logger.error(f"Error creating thumbnail for {paper_id}: {str(e)}")
            return False