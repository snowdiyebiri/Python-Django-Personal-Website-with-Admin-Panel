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

def fix_links(html, full_path, theme_dir):
    # full_path is e.g. "projects/slug/"
    # theme_dir is "modern-dark"
    # depth is segments of "modern-dark/projects/slug/"
    path_segments = [theme_dir] + [p for p in full_path.strip('/').split('/') if p]
    depth = len(path_segments)
    prefix = "../" * depth
    
    # Fix static/media/internal links using prefix
    html = html.replace('href="/static/', f'href="{prefix}static/')
    html = html.replace('src="/static/', f'src="{prefix}static/')
    html = html.replace('href="/media/', f'href="{prefix}media/')
    html = html.replace('src="/media/', f'src="{prefix}media/')
    
    for p in PATHS:
        old_link = f'href="/{p}"'
        # Target is at root: ../../.. + p + index.html
        target = f"{prefix}{p}index.html"
        new_link = f'href="{target}"'
        
        if p == "":
            old_link = 'href="/"'
            new_link = f'href="{prefix}index.html"'
            
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
                html = fix_links(html, path, theme_dir)
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
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir()

    themes = ThemeSettings.objects.all()
    
    # 1. Generate theme subdirectories
    for theme in themes:
        generate_for_theme(theme)

    # 2. Generate root index.html landing page
    print("Generating root landing page...")
    from django.template.loader import render_to_string
    root_html = render_to_string('index.html', {'themes': themes})
    with open(OUTPUT_DIR / "index.html", "w", encoding="utf-8") as f:
        f.write(root_html)

    # Add .nojekyll
    (OUTPUT_DIR / ".nojekyll").touch()
    print(f"Static site generated in {OUTPUT_DIR}/")

if __name__ == "__main__":
    main()
