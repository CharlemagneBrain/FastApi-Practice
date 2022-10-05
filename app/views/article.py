from http.client import HTTPException
from fastapi import APIRouter
from fastapi import Request
from app.models.articles import Article
from app.core.config import templates
from typing import List, Optional
from app.schemas.article import (Article as ArticleSchema, ArticleCreate, ArticleUpdate)


# async=>méthode effectué en parallèle, non bloquante
                                    # Tte fonction asynchrone non bloquante doit être attendue(await),pour en récupérer son résultat
     # await dit à Python d'attendre la réponse de la méthode create

article_views = APIRouter()

# CREATE
@article_views.post("/articles/create", response_model=List[ArticleSchema])
async def create(article_create: ArticleCreate):
    
    article = await Article.create(
        title = article_create.title,
        content = article_create.content
    )
    
    return article

# EDIT
@article_views.put("/articles/edit/{article_id}", response_model=ArticleSchema)
async def edit(article_id: int, article_edit: ArticleUpdate):
    article: Optional[Article] = await Article.get_or_none(id=article_id)
    if not article:
        raise HTTPException(status_code=404, detail="Article non trouvé")
    
    article.title = article_edit.title
    article.content = article_edit.content
    
    await article.save()
    return article


# Get an article by id
@article_views.get("/articles/{article_id}", response_model=ArticleSchema)
async def get_article(article_id: int):
    
    article: Optional[Article] = await Article.get_or_none(id=article_id)
    if not article:
        raise HTTPException(status_code=404, detail="Article non trouvé")
    
    return article
    
# Get articles with limit and offset parameters
@article_views.get("/articles", response_model=List[ArticleSchema])
async def index_list(offset: int=0, limit: Optional[int] = None):
    
    files_query = Article.all().order_by('-created_at').offset(offset)
    
    if limit:
        files_query = files_query.limit(limit)
    
    articles = await files_query
    
    return articles

@article_views.delete("/articles/delete/{article_id}")
async def delete(article_id: int):
    article: Optional[Article] = await Article.get_or_none(id=article_id)
    
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    
    await article.delete()
    
    
    
