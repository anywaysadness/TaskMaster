from fastapi import FastAPI
from fastapi.staticfiles import  StaticFiles
from app.users.router import router as router_users
from app.tasks.router import router as router_tasks
from app.roles.router import router as router_roles
from app.tags.router import router as router_tags
from app.pages.router import router as router_pages
import uvicorn


app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), "static")

app.include_router(router_users)
app.include_router(router_tasks)
app.include_router(router_roles)
app.include_router(router_tags)
app.include_router(router_pages)


@app.get("/")
def root():
    return {"message": "Ты попал верно"}


if __name__ == '__main__':
    uvicorn.run("app.main:app", reload=True)
