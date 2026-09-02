# IronRow Gym — Membership Website

A responsive gym membership website built with **Python (Flask)**, **Jinja2 templates**, and hand-written CSS (no frameworks). Built as a learning project.

## Features
- Home page with hero section and animated-free "plate loader" stats
- Membership plans page with pricing cards
- Class schedule page
- Contact form with server-side validation (Flask)
- Fully responsive: works on phone, tablet, and desktop
- Mobile hamburger navigation

## Tech Stack
- Python 3
- Flask
- HTML5 / Jinja2 templating
- CSS3 (custom properties, CSS Grid, Flexbox, media queries)
- Vanilla JavaScript (no libraries)

## Running Locally

1. Create and activate a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # Mac/Linux
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the app:
   ```
   python app.py
   ```

4. Open your browser to `http://127.0.0.1:5000`

## Project Structure
```
gym-membership-website/
├── app.py                 # Flask routes and data
├── requirements.txt
├── templates/
│   ├── base.html          # shared layout (nav, footer)
│   ├── index.html         # home page
│   ├── membership.html    # pricing plans
│   ├── classes.html       # class schedule
│   └── contact.html       # contact form
└── static/
    ├── css/style.css
    └── js/script.js
```

## Author's Notes
This project was built as part of a two-week goal to publish two portfolio
projects on GitHub while learning Python and web development basics.
