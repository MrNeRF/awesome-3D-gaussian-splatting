from datetime import datetime
from typing import Optional, List
from dataclasses import dataclass, field

@dataclass
class Paper:
    id: str = ""
    category: str = ""
    title: str = ""
    authors: str = ""
    year: str = str(datetime.now().year)
    abstract: str = ""
    project_page: Optional[str] = None
    paper_url: Optional[str] = None
    code_url: Optional[str] = None
    video_url: Optional[str] = None
    thumbnail_image: bool = False
    thumbnail_video: bool = False

    @classmethod
    def from_dict(cls, data: dict) -> 'Paper':
        return cls(
            id=data.get('id', ''),
            category=data.get('category', ''),
            title=data.get('title', ''),
            authors=data.get('authors', ''),
            year=data.get('year', str(datetime.now().year)),
            abstract=data.get('abstract', ''),
            project_page=data.get('project_page'),
            paper_url=data.get('paper'),
            code_url=data.get('code'),
            video_url=data.get('video'),
            thumbnail_image=data.get('thumbnail_image', False),
            thumbnail_video=data.get('thumbnail_video', False)
        )

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'category': self.category,
            'title': self.title,
            'authors': self.authors,
            'year': self.year,
            'abstract': self.abstract,
            'project_page': self.project_page,
            'paper': self.paper_url,
            'code': self.code_url,
            'video': self.video_url,
            'thumbnail_image': self.thumbnail_image,
            'thumbnail_video': self.thumbnail_video
        }
