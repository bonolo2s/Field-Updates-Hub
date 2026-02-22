# Field Updates Hub

A community platform for agricultural professionals to share and discover field intelligence — pest alerts, weather observations, crop conditions, fertilizer recommendations, and farming insights.

## Tech Stack

- **Backend:** Django + Django Auth
- **Frontend:** Django Template Language + Tailwind CSS
- **Database:** SQLite

## Features

- User registration and login/logout
- Create, edit, and delete field updates
- Public feed showing all updates in reverse chronological order
- User profiles with post history
- Categories: Pest Alert, Weather Observation, Crop Condition, Fertilizer Tip, General Insight

## Getting Started

### Prerequisites

- Python 3.10+ — runs the Django backend
- pip — installs Python packages
- Node.js 18+ — required for Vite to bundle Tailwind CSS

### Installation
```bash
# Clone the repository
git clone https://github.com/bonolo2s/Field-Updates-Hub.git
cd FieldUpdatesHub

# Create and activate a virtual environment
python -m venv myenv
source myenv/bin/activate  # Windows: myenv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt

# Install Node dependencies (for Tailwind + Vite)
npm install

# Apply migrations
python manage.py migrate

# Seed sample data (optional)
python manage.py loaddata seed_data.json
```

### Running the App

You need **two terminals** running simultaneously:
```bash
# Terminal 1 — Django server
python manage.py runserver

# Terminal 2 — Vite (Tailwind CSS)
npm run dev
```

> Vite compiles and serves Tailwind CSS in development mode. Without it, the app will have no styles.

### Access the App

Visit `http://127.0.0.1:8000` in your browser.


```
## 📁 Project Structure

```
FieldUpdatesHub/
├── core/                          # Main Django app
│   ├── migrations/
│   ├── templates/
│   │   ├── base.html              # Authenticated layout (sidebar + navbar)
│   │   ├── base_auth.html         # Public layout (login/register/landing)
│   │   ├── landing.html           # Public landing page
│   │   ├── registration/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── core/
│   │       ├── feed.html
│   │       ├── community.html
│   │       ├── profile.html
│   │       ├── profile_modal.html
│   │       ├── create_update.html
│   │       ├── edit_update.html
│   │       └── delete_update.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── FieldUpdates/                  # Project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── media/                         # User uploaded images
├── static/
│   └── src/
│       └── main.css               # Tailwind entry point
├── .gitignore
├── manage.py
├── package.json
├── package-lock.json
├── vite.config.js
├── requirements.txt
└── README.md
```

## Models

**User** — Django's built-in User model (name, email)

**FieldUpdate** — author (FK), timestamp, title, message, category

## Usage

1. Register an account (email confirmation required)
2. Browse the public feed on the homepage
3. Create a field update using the form
4. Click any user to view their profile and posts
5. Edit or delete only your own posts
