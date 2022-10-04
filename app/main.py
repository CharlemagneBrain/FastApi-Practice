from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from tortoise.contrib.fastapi import register_tortoise 
from app.views.article import article_views
from app.core.config import settings


app = FastAPI()

# Nous montons une route  qui va répondre à l'URL /static et qui servira, 
# sous cette adresse, les fichiers que nous mettrons dans le répertoire public/ 
app.mount("/static", StaticFiles(directory=settings.STATIC_FILES_DIRECTORY), name="public")

# Nous créons un objet (templates) qui va nous permettre de créer de 
# l'HTML avec le moteur de templates Jinja2.

register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={
        "models" : settings.TORTOISE_MODELS 
        },
    generate_schemas = True,
    add_exception_handlers = True
)

app.include_router(
    article_views,
    tags=["Article"]
)



