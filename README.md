# Django Personal Portfolio Website

A modern, dynamic, and fully customizable personal portfolio website built with Django 6.0. 

## 🚀 Features

- **Dynamic Hero Section:** Customizable greeting, name, and cycling titles via the admin panel.
- **Project Showcase:** Manage your projects with descriptions, technologies, and images.
- **Dynamic Theme Management:** Change site colors, background patterns (dots, grid, or solid), and animation speeds directly from the Django Admin.
- **About & Stats:** Dedicated about page with biography and animated statistics.
- **Contact System:** Functional contact form that saves messages to the database with a custom admin dashboard view.
- **Security Hardened:** Pre-configured security settings for production (HSTS, SSL redirect, etc.).
- **Responsive Design:** Clean, modern UI that works across all devices.

## 🌐 Static Version (GitHub Pages)

A static version of this site can be generated for hosting on GitHub Pages or other static hosting services.

### Generate Static Site

1. Ensure the Django server is running:
   ```bash
   python manage.py runserver
   ```
2. Run the generation script:
   ```bash
   python generate_static.py
   ```
This will create a `docs/` folder containing the static HTML files and assets.

### Deploy to GitHub Pages

1. Push your changes (including the `docs/` folder) to GitHub.
2. Go to your repository **Settings** > **Pages**.
3. Under **Build and deployment** > **Branch**, select your branch (e.g., `main`) and the `/docs` folder.
4. Click **Save**.

*Note: The contact form will not process messages in the static version as it requires a Django backend.*

## 🛠️ Technologies Used

- **Backend:** Django 6.0.5, Python 3.14+
- **Frontend:** Vanilla CSS, FontAwesome 6.0
- **Database:** SQLite (default)
- **Environment Management:** `python-dotenv`
- **Image Processing:** `Pillow`

## 🏁 Getting Started

### Prerequisites

- Python 3.14 or higher
- `pip` (Python package manager)

### Installation

1. **Clone the repository:**
   ```bash
   git clone [<repository-url>](https://github.com/snowdiyebiri/Python-Django-Personal-Website-with-Admin-Panel.git)
   cd DjangoWebSite
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   Create a `.env` file in the root directory (copy from `.env.example` if available) and set your variables:
   ```env
   DJANGO_SECRET_KEY=your-secret-key
   DJANGO_DEBUG=True
   DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
   ```

5. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

The site will be available at `http://127.0.0.1:8000/`.

## 📁 Project Structure

- `config/`: Project configuration, settings, and root URL routing.
- `projects/`: Manages project listings, skills, and site-wide theme settings.
- `pages/`: Handles static-like dynamic pages (Home, About).
- `contact/`: Messaging system and contact form logic.
- `templates/`: Centralized HTML templates.
- `static/`: Global CSS and JavaScript assets.
- `media/`: User-uploaded content (project images, custom icons).

## 🎨 Customization

Most aspects of the site can be customized via the **Django Admin** (`/admin/`):
- **Theme:** Go to "Theme Settings" to change the primary accent color, background patterns, and animation speeds.
- **Hero:** Update your professional titles and CTA text in "Hero Content".
- **Socials:** Add or remove social media links with custom icons.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
