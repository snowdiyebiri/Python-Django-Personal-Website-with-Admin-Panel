# Dynamic Django Portfolio Website

A modern, highly customizable personal portfolio website built with Python/Django. Features an extensive admin panel that allows full control over branding, themes, global layout, and content without touching code.

## Key Features

- **Dynamic Theme Management:** Switch between pre-defined color schemes (Modern Dark, Midnight Deep, Emerald Forest, Soft Rose) or create your own.
- **Global Layout Control:** Adjust container widths, navbar spacing, hero section gaps, and section paddings globally from the admin panel.
- **Content Management:** Easily update your bio, project details, skills, references, and contact information through a clean, intuitive Django Admin.
- **Modern UI:** Built with modern CSS (glassmorphism, interactive stacks, typewriter effects) and optimized for responsiveness.
- **Static Site Generation:** Includes a generator script for publishing to GitHub Pages or similar static hosting.

## Admin Panel Customization

The project uses a powerful **Site Configuration** and **Theme Settings** system:
- **Theme Settings:** Customize primary/secondary colors for both Dark and Light modes, backgrounds, patterns (dots/grid), and animations.
- **Site Configuration:** Globally manage layout spacing, container sizes, navbar/footer text, and navigation links.

## Prerequisites

- Python 3.x
- Django 6.0+

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

5. **Access the Admin Panel:**
   Navigate to `/admin` to start customizing your theme and content.

## Generating Static Files

To export your site as a static build for deployment:
```bash
python generate_static.py
```
Generated files are saved in the `docs/` directory.

## Architecture Highlights
- **Dynamic Themes:** Uses custom template tags and filters (`hex_to_rgb`) to generate dynamic CSS variables on the fly.
- **Global Layout:** Spacing logic is decoupled from individual themes to ensure structural consistency across all color schemes.
