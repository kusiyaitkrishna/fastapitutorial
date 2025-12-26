from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import user
from config import settings

app =FastAPI()
app.mount(
    settings.MEDIA_URL,
    StaticFiles(directory=settings.MEDIA_ROOT),
    name="media"
)
app.include_router(user.router)

