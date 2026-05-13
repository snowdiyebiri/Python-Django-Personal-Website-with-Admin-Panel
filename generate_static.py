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

def fix_links(html):
    # Fix static and media: remove leading slash for relative paths
    html = html.replace('href="/static/', 'href="static/')
    html = html.replace('src="/static/', 'src="static/')
    html = html.replace('href="/media/', 'href="media/')
    html = html.replace('src="/media/', 'src="media/')
    
    # Fix internal links
    for p in PATHS:
        old_link = f'href="/{p}"'
        target = f"{p}index.html"
        new_link = f'href="{target}"'
        
        if p == "":
            old_link = 'href="/"'
            new_link = 'href="index.html"'
            
        html = html.replace(old_link, new_link)
        
    return html

def main():
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir()
    
    for path in PATHS:
        url = f"{BASE_URL}/{path}"
        try:
            with urllib.request.urlopen(url) as response:
                html = response.read().decode('utf-8')
                html = fix_links(html)
                target_dir = OUTPUT_DIR / path
                target_dir.mkdir(parents=True, exist_ok=True)
                with open(target_dir / "index.html", "w", encoding="utf-8") as f:
                    f.write(html)
        except Exception as e:
            print(f"Error fetching {url}: {e}")

    # Copy static and media
    shutil.copytree("static", OUTPUT_DIR / "static")
    if Path("media").exists():
        shutil.copytree("media", OUTPUT_DIR / "media")

    (OUTPUT_DIR / ".nojekyll").touch()
    print(f"Static site generated in {OUTPUT_DIR}/")

if __name__ == "__main__":
    main()
