from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
import openai
import os
import json
from datetime import datetime

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

load_dotenv()
openai.api_key = os.getenv("OPENROUTER_API_KEY")
openai.base_url = "https://openrouter.ai/api/v1"

def load_profile():
    with open("data/sample_profile.json", "r") as f:
        return json.load(f)

def load_scheduled_posts():
    try:
        with open("data/scheduled_posts.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_scheduled_posts(posts):
    with open("data/scheduled_posts.json", "w") as f:
        json.dump(posts, f, indent=4)

def get_analytics_data():
    posts = load_scheduled_posts()
    return {
        "total_posts": len(posts),
        "estimated_reach": len(posts) * 250,
        "avg_engagement": round(len(posts) * 0.4, 2)
    }

@app.get("/")
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "profile": load_profile(),
        "scheduled_posts": load_scheduled_posts(),
        "analytics": get_analytics_data(),
        "generated_post": None
    })

@app.post("/schedule")
async def schedule_post(request: Request, content: str = Form(...), post_time: str = Form(...)):
    posts = load_scheduled_posts()
    posts.append({
        "content": content,
        "post_time": post_time
    })
    save_scheduled_posts(posts)
    return RedirectResponse(url="/", status_code=303)

@app.post("/generate")
async def generate_post(request: Request):
    try:
        response = openai.chat.completions.create(
            model="mistralai/mixtral-8x7b",
            messages=[
                {
                    "role": "user",
                    "content": "Generate a short, engaging LinkedIn post about how AI is transforming personal branding."
                }
            ]
        )
        ai_post = response.choices[0].message.content
    except Exception as e:
        ai_post = f"❌ Error generating post: {str(e)}"

    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "profile": load_profile(),
        "scheduled_posts": load_scheduled_posts(),
        "analytics": get_analytics_data(),
        "generated_post": ai_post
    })
