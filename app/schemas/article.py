from pydantic import BaseModel
from datetime import datetime


class ArticleBase(BaseModel):
    title: str
    content: str
class Article(ArticleBase):
    id: int
    created_at: datetime
    updated_at: datetime  
class ArticleCreate(ArticleBase):
    pass

class ArticleUpdate(ArticleBase):
    pass