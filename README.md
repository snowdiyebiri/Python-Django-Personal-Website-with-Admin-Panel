# Dynamic Django Portfolio Website

A modern, highly customizable personal portfolio website built with Python/Django. Features an extensive admin panel that allows full control over branding, themes, global layout, and content without touching code.


## Features
- **Dynamic Theme Management:** Switch between pre-defined color schemes or create your own.
- **Global Layout Control:** Adjust spacing, container widths, and gaps globally from the admin panel.
- **Admin-Driven Content:** Manage your bio, projects, skills, and contact info directly in the Django Admin.
- **Static Export:** Fully exportable as a static site for GitHub Pages or other hosting services.

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/snowdiyebiri/Python-Django-Personal-Website-with-Admin-Panel.git
   cd Python-Django-Personal-Website-with-Admin-Panel
   ```

2. **Create and activate a virtual environment:**
   - **Windows:**
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server:**
   ```bash
   python manage.py runserver
   ```
   Access the site at `http://127.0.0.1:8000` and the Admin panel at `http://127.0.0.1:8000/admin`.

## Deploying to GitHub Pages

To export your site as a static build for deployment:
```bash
python generate_static.py
```
This will generate the site in the `docs/` folder. Commit and push these changes to your `main` branch:
```bash
git add docs/
git commit -m "Deploy static site"
git push origin main
```
*Ensure your GitHub repository settings are configured to serve pages from the `/docs` folder.*
