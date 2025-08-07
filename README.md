# influence-os-ai-agent
This project is part of the Influence OS AI Intern Assignment. It helps automate LinkedIn content using AI.


---

## 🌟 Features

- **User Profile Analysis**: Reads and analyzes user data from LinkedIn-like profiles.
- **AI Content Generation**: Generates LinkedIn posts using OpenRouter LLMs like GPT-3.5 or Mixtral.
- **Content Scheduling**: Lets users schedule posts for future publication.
- **Auto Posting**: Automatically posts content based on scheduled time.
- **Post Analytics**: Visual analytics to track reach and engagement.
- **Interactive Dashboard**: Modern UI to control and monitor all functionalities.
- **Built with Free LLM Access**: Integrated with OpenRouter (no OpenAI subscription required).

---

## 🧠 Tech Stack

- **Frontend**: HTML (Jinja2 Templates), CSS (Optional enhancements)
- **Backend**: FastAPI (Python)
- **AI Models**: OpenRouter API (GPT-3.5, Mixtral)
- **Scheduler**: Custom Python logic for auto-posting
- **Data**: JSON for profile, posts, and analytics
- **Hosting**: Local or any FastAPI-compatible deployment

---

## ⚙️ Installation

1. **Clone the repository**

git clone https://github.com/ankush060/influence-os-ai-agent.git
cd influence-os-ai-agent

2. **Create virtual environment**

python -m venv venv
venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Set your OpenRouter API key
Create a .env file in the root:
OPENROUTER_API_KEY=your_actual_openrouter_api_key_here   #add this to .env file

5. Running the App

step1: Start the Dashboard (FastAPI)
uvicorn app.main:app --reload      #command to run in your project environment
Visit: http://127.0.0.1:8000

step2:Run Scheduler for Auto Posting
(Open a new terminal tab with virtual environment activated)
python app/scheduler.py

6. Project Structure
influence-os-ai-agent/
│
├── app/
│   ├── main.py              # FastAPI app
│   ├── scheduler.py         # Content scheduler
│   ├── profile_analyzer.py  # Profile reader
│
├── templates/
│   └── dashboard.html       # Dashboard UI
│
├── static/                  # CSS, JS, etc. (optional)
├── data/
│   ├── sample_profile.json
│   └── scheduled_posts.json
├── .env
├── requirements.txt
└── README.md

7. Testing the Project:

Visit the homepage
Generate AI content → Schedule it
Check logs in scheduler terminal to confirm posting
View analytics on the dashboard

