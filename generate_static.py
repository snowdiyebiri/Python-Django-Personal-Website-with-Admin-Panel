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

def get_relative_prefix(path_str):
    if not path_str or path_str == "":
        return "./"
    # Count slashes to determine depth
    depth = path_str.strip("/").count("/")
    # If path is projects/e-commerce-api/ (2 slashes)
    # We need ../../ to reach root (depth 0)
    return "../" * (depth + 1)

def fix_links(html, current_path):
    prefix = get_relative_prefix(current_path)
    
    # Fix static and media using the calculated depth prefix
    html = html.replace('href="/static/', f'href="{prefix}static/')
    html = html.replace('src="/static/', f'src="{prefix}static/')
    html = html.replace('href="/media/', f'href="{prefix}media/')
    html = html.replace('src="/media/', f'src="{prefix}media/')
    
    # Fix internal links
    for p in PATHS:
        old_link = f'href="/{p}"'
        # The path of the target file relative to root
        target = f"{p}index.html" if p else "index.html"
        
        # Calculate relative path from current_path to target
        # e.g., from projects/ai-image-generator/ to about/index.html is ../../about/index.html
        rel_path = os.path.relpath(target, current_path.strip("/") if current_path else ".")
        rel_path = rel_path.replace(os.sep, '/')
        
        new_link = f'href="{rel_path}"'
        if p == "":
            old_link = 'href="/"'
            new_link = f'href="{rel_path}"'
            
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
                html = fix_links(html, path)
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
