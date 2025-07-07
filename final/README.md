# 🧠 Local Job Opportunity Recommender for Youth

A real-time job recommender that helps youth find local, entry-level jobs based on their interests and location.

## 👨‍💻 How It Works
- User enters location and interest
- System recommends top 3–5 matching jobs from a local CSV file

## 🔧 Tech Stack
- Python, FastAPI
- Scikit-learn (TF-IDF)
- HTML/CSS (Jinja templates)

## 📦 Installation
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
