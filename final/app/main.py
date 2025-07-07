from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pandas as pd
from recommender import get_recommendations

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/recommend", response_class=HTMLResponse)
def recommend(request: Request, location: str = Form(...), interest: str = Form(...)):
    jobs = get_recommendations(location, interest)
    return templates.TemplateResponse("index.html", {"request": request, "jobs": jobs})
