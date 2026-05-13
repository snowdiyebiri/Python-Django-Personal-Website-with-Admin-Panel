import os
import shutil
import urllib.request
import django
from pathlib import Path

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from projects.models import ThemeSettings

BASE_URL = "http://127.0.0.1:8000"
OUTPUT_DIR = Path("docs")
PATHS = [
    "",
    "about/",
    "projects/",
    "contact/",
    "references/",
    "admin-preview/",
]

PROJECT_SLUGS = ['e-commerce-api', 'ai-image-generator', 'task-management-system', 'portfolio-template', 'finance-tracker', 'blog-platform']
for slug in PROJECT_SLUGS:
    PATHS.append(f"projects/{slug}/")

def fix_links(html, current_path, theme_dir=""):
    # Ensure theme_dir starts with a slash if provided
    theme_prefix = f"/{theme_dir}" if theme_dir else ""
    
    # Fix static and media: point to root-relative path
    html = html.replace('href="/static/', f'href="{theme_prefix}/static/')
    html = html.replace('src="/static/', f'src="{theme_prefix}/static/')
    html = html.replace('href="/media/', f'href="{theme_prefix}/media/')
    html = html.replace('src="/media/', f'src="{theme_prefix}/media/')
    
    # Fix internal links
    for p in PATHS:
        old_link = f'href="/{p}"'
        new_link = f'href="{theme_prefix}/{p}index.html"'
        if p == "":
             old_link = 'href="/"'
             new_link = f'href="{theme_prefix}/index.html"'
        html = html.replace(old_link, new_link)
        
    return html

def generate_for_theme(theme):
    print(f"Generating site for theme: {theme.name}...")
    
    # Activate theme
    ThemeSettings.objects.all().update(is_active=False)
    theme.is_active = True
    theme.save()
    
    theme_dir = theme.name.lower().replace(" ", "-")
    theme_folder = OUTPUT_DIR / theme_dir
    theme_folder.mkdir(parents=True, exist_ok=True)
    
    for path in PATHS:
        url = f"{BASE_URL}/{path}"
        try:
            with urllib.request.urlopen(url) as response:
                html = response.read().decode('utf-8')
                html = fix_links(html, path, theme_dir=theme_dir)
                target_dir = theme_folder / path
                target_dir.mkdir(parents=True, exist_ok=True)
                with open(target_dir / "index.html", "w", encoding="utf-8") as f:
                    f.write(html)
        except Exception as e:
            print(f"Error fetching {url}: {e}")

    # Copy static and media
    if (theme_folder / "static").exists():
        shutil.rmtree(theme_folder / "static")
    shutil.copytree("static", theme_folder / "static")
    if Path("media").exists():
        if (theme_folder / "media").exists():
            shutil.rmtree(theme_folder / "media")
        shutil.copytree("media", theme_folder / "media")

def main():
    if OUTPUT_DIR.exists():
        # Remove only the generated content subfolders, keeping root if needed
        for item in OUTPUT_DIR.iterdir():
            if item.is_dir():
                shutil.rmtree(item)
    OUTPUT_DIR.mkdir(exist_ok=True)

    themes = ThemeSettings.objects.all()
    for theme in themes:
        generate_for_theme(theme)

    # Add .nojekyll
    (OUTPUT_DIR / ".nojekyll").touch()
    
    print(f"Static site generated in {OUTPUT_DIR}/")

if __name__ == "__main__":
    main()
