from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

@dataclass
class Paper:
    """Data model for a research paper."""
    id: str
    title: str
    authors: str
    year: int
    tags: List[str]
    thumbnail: Optional[str] = None
    abstract: Optional[str] = None
    project_page: Optional[str] = None
    paper: Optional[str] = None
    code: Optional[str] = None
    video: Optional[str] = None

    @classmethod
    def from_dict(cls, data: dict) -> 'Paper':
        """Create a Paper instance from a dictionary."""
        # Ensure required fields are present
        required_fields = ['id', 'title', 'authors', 'year', 'tags']
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")

        # Validate and convert year
        try:
            # Handle various year formats
            year_value = data['year']
            if isinstance(year_value, str):
                # Remove any non-digit characters and convert to int
                year_str = ''.join(filter(str.isdigit, year_value))
                if not year_str:
                    raise ValueError(f"Invalid year format: {year_value}")
                year_value = int(year_str)
            elif isinstance(year_value, float):
                year_value = int(year_value)
            elif not isinstance(year_value, int):
                raise ValueError(f"Invalid year type: {type(year_value)}")
            
            # Basic sanity check for year range
            current_year = datetime.now().year
            if not (1900 <= year_value <= current_year + 1):  # Allow next year for preprints
                raise ValueError(f"Year {year_value} is outside valid range")
        except (ValueError, TypeError) as e:
            raise ValueError(f"Invalid year value ({data['year']}): {str(e)}")

        # Validate tags
        if not isinstance(data['tags'], list):
            raise ValueError("Tags must be a list")

        # Create instance with validated data
        return cls(
            id=str(data['id']),
            title=str(data['title']),
            authors=str(data['authors']),
            year=int(data['year']),
            tags=list(data['tags']),
            thumbnail=str(data.get('thumbnail', '')),
            abstract=str(data.get('abstract', '')),
            project_page=str(data.get('project_page', '')),
            paper=str(data.get('paper', '')),
            code=str(data.get('code', '')),
            video=str(data.get('video', ''))
        )

    def to_dict(self) -> dict:
        """Convert Paper instance to dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'authors': self.authors,
            'year': self.year,
            'tags': self.tags,
            'thumbnail': self.thumbnail if self.thumbnail else None,
            'abstract': self.abstract if self.abstract else None,
            'project_page': self.project_page if self.project_page else None,
            'paper': self.paper if self.paper else None,
            'code': self.code if self.code else None,
            'video': self.video if self.video else None
        }