from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from app.users.router import router as router_users


app = FastAPI()
templates = Jinja2Templates(directory="templates")
#app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get('/')
def start(request: Request):
    return templates.TemplateResponse('start.html', {'request': request})


@app.get('/login', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse('login.html', {'request': request})


app.include_router(router_users)