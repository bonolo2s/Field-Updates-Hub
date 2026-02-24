# Field Updates Hub

A community platform for agricultural professionals to share and discover field intelligence — pest alerts, weather observations, crop conditions, fertilizer recommendations, and farming insights.

## Tech Stack

- **Backend:** Django + Django Auth
- **Frontend:** Django Template Language + Tailwind CSS
- **Database:** SQLite

## Features

### Authentication
- User registration and login/logout
- Protected routes — unauthenticated users are redirected to login

### Field Updates (Posts)
- Create, edit, and delete field updates
- Optional image upload on post creation and editing
- Users can remove images from existing posts
- Posts are categorized for easy browsing

### Categories
Each post belongs to one of five categories, color-coded consistently across the app:
- 🐛 Pest Alert
- 🌧️ Weather Observation
- 🌿 Crop Condition
- 🌱 Fertilizer Tip
- 💬 General Insight

### Feed
- Public feed showing all updates in reverse chronological order
- **Search** — searches across post title, message, and author name. Built on the backend using Django's `Q` objects to query the database directly, avoiding loading all posts into memory
- **Filter by category** — backend filtering using Django ORM, only the relevant posts are fetched from the database
- **Pagination** — 5 posts per page using Django's built-in `Paginator`. Translates to SQL `LIMIT/OFFSET` queries, meaning only the current page's posts are loaded from the database at a time — not all posts

### Community & Profiles
- Community page showing all registered members
- User profiles with full post history
- Click any user's avatar on the feed to preview their profile in a modal (powered by HTMX — no page reload)

### Live Weather Widget
- Detects the user's location via the browser
- Fetches real-time weather from the Open-Meteo API (free, no API key required)
- Displays temperature and current conditions
- Advises farmers whether it is **safe to spray** based on wind speed, temperature, rainfall, and fog — key conditions that affect pesticide and fertilizer application effectiveness

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
├── FieldUpdates/                  # Project configuration
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
