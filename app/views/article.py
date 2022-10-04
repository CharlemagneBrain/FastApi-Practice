from fastapi import APIRouter
from fastapi import Request
from app.models.articles import Article
from app.core.config import templates


# async=>méthode effectué en parallèle, non bloquante
                                    # Tte fonction asynchrone non bloquante doit être attendue(await),pour en récupérer son résultat
     # await dit à Python d'attendre la réponse de la méthode create

article_views = APIRouter()

@article_views.get("/articles/create", include_in_schema=False)
async def create(request: Request):
    
    article = await Article.create(
        title = "Article Test",
        content = "Contenu Test"
    )
    
    return templates.TemplateResponse(
        "articles_create.html",
        {
            "article" : article,
            "request" : request  
        }
    )

@article_views.get("/articles", include_in_schema=False)
async def index(request: Request):
    
    articles = await Article.all().order_by("created_at")
    
    return templates.TemplateResponse(
        "articles_list",
        {
            "article" : articles,
            "request" : request
        }
    )
    
@article_views.get("/api/articles")
async def api_articles_list():

    articles = await Article.all().order_by('created_at')

    return articles


@article_views.get("/", include_in_schema=False)
async def root(request: Request):

    return templates.TemplateResponse(
        "home.html",
        {
            "request": request
        })