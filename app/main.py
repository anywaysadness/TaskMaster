from fastapi import FastAPI
from app.users.router import router as router_users
from app.tasks.router import router as router_tasks
from app.roles.router import router as router_roles
from app.tags.router import router as router_tags


app = FastAPI()

app.include_router(router_users)
app.include_router(router_tasks)
app.include_router(router_roles)
app.include_router(router_tags)


@app.get("/")
def root():
    return {"message": "Ты попал верно"}
