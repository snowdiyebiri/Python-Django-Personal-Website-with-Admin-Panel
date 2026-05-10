# 🚀 Modern Django Portfolio Template | Dynamic & SEO-Friendly

**Live Demo:** [https://snowdiyebiri.github.io/Python-Django-Personal-Website-with-Admin-Panel/](https://snowdiyebiri.github.io/Python-Django-Personal-Website-with-Admin-Panel/)

A professional, high-performance personal portfolio website built with **Django 6.0**. This template is designed for developers, designers, and makers who want a fully manageable, aesthetically pleasing online presence.

## ✨ Key Features

- **🎨 Dynamic Theme Engine:** Change your entire site's look (colors, background patterns, animations) via the Admin Panel.
- **🔍 Global Search:** Filter projects and content using dynamic search with Django `Q` objects.
- **🖼️ Logo & Favicon Support:** Upload your custom branding directly through the theme settings.
- **📱 Responsive Hero Section:** Interactive project stack and cycling professional titles.
- **📂 Automated Project Showcase:** All your projects are automatically synced and displayed in the hero and project sections.
- **📊 Animated Statistics:** Showcase your impact with dynamic, animated counter stats.
- **📩 Integrated Contact System:** Functional form that saves messages to your private dashboard.
- **🛡️ Security Hardened:** Pre-configured for production with SSL, HSTS, and XSS protections.

## 🛠️ Tech Stack

- **Backend:** Python 3.14+, Django 6.0.5
- **Frontend:** Vanilla CSS (Modern CSS Variables), FontAwesome 6.0
- **Storage:** SQLite (Development), Media Support for Images/SVGs
- **Deployment:** Optimized for GitHub Pages (via included static generator)

## 🏁 Quick Start

### 1. Installation
```bash
git clone https://github.com/snowdiyebiri/Python-Django-Personal-Website-with-Admin-Panel.git
cd Python-Django-Personal-Website-with-Admin-Panel
python -m venv venv
source venv/Scripts/activate  # Windows
pip install -r requirements.txt
```

### 2. Setup
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### 3. Personalization
Access the **Command Center** at `/admin/` to:
- Create your **Theme** (Colors, Patterns, Logo).
- Update your **Hero Content** (Name, Bio, Titles).
- Add your **Projects** and **Social Links**.

## 🌐 Static Deployment (GitHub Pages)

This project includes a built-in static crawler to export your dynamic Django site into a GitHub-ready format.

1. Run the local server: `python manage.py runserver`
2. Generate static files: `python generate_static.py`
3. Push the `docs/` folder to GitHub and set your Pages source to `/docs`.

*Note: Search and Contact form functionality require the Django backend and will not process data in the static version.*


- `config/`: System core & security settings.
- `projects/`: The engine behind projects, themes, and branding.
- `pages/`: Dynamic views for Home and About.
- `contact/`: Messaging logic and admin API.
- `docs/`: The generated static version of the site.

---
*Crafted with 💜 by **SERHAT ÇAM***
