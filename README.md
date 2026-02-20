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

- Python 3.10+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/field-updates-hub.git
cd field-updates-hub

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Seed sample data (optional)
python manage.py loaddata seed_data.json

# Run the development server
python manage.py runserver
```

### Access the App

Visit `http://127.0.0.1:8000` in your browser.

## Project Structure

```
field_updates_hub/
├── accounts/         # Auth: registration, login, profiles
├── updates/          # Field updates CRUD
├── templates/        # Django HTML templates
├── static/           # Tailwind CSS and static assets
├── manage.py
└── requirements.txt
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
