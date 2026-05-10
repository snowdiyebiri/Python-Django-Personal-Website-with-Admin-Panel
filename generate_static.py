import os
import shutil
import urllib.request
from pathlib import Path

BASE_URL = "http://127.0.0.1:8000"
OUTPUT_DIR = Path("docs")
PATHS = [
    "",
    "about/",
    "projects/",
    "contact/",
    "references/",
]

# Add projects dynamically if possible, or use the known IDs
PROJECT_IDS = [4, 5, 6, 7, 8, 9]
for pid in PROJECT_IDS:
    PATHS.append(f"projects/{pid}/")

def get_relative_prefix(path_str):
    if not path_str or path_str == "":
        return ""
    depth = path_str.strip("/").count("/") + 1
    return "../" * depth

def fix_links(html, current_path):
    prefix = get_relative_prefix(current_path)
    # Fix static and media
    html = html.replace('href="/static/', f'href="{prefix}static/')
    html = html.replace('src="/static/', f'src="{prefix}static/')
    html = html.replace('href="/media/', f'href="{prefix}media/')
    html = html.replace('src="/media/', f'src="{prefix}media/')
    
    # Fix internal links
    # This is a bit naive but should work for this project's simple URLs
    for p in PATHS:
        old_link = f'href="/{p}"'
        new_link = f'href="{prefix}{p}index.html"'
        if p == "":
             old_link = 'href="/"'
             new_link = f'href="{prefix}index.html"'
        html = html.replace(old_link, new_link)
        
    return html

def main():
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir()

    for path in PATHS:
        url = f"{BASE_URL}/{path}"
        print(f"Fetching {url}...")
        try:
            with urllib.request.urlopen(url) as response:
                html = response.read().decode('utf-8')
                
                # Fix links to be relative
                html = fix_links(html, path)
                
                # Save to file
                target_dir = OUTPUT_DIR / path
                target_dir.mkdir(parents=True, exist_ok=True)
                with open(target_dir / "index.html", "w", encoding="utf-8") as f:
                    f.write(html)
        except Exception as e:
            print(f"Error fetching {url}: {e}")

    # Copy static and media
    print("Copying assets...")
    shutil.copytree("static", OUTPUT_DIR / "static")
    if Path("media").exists():
        shutil.copytree("media", OUTPUT_DIR / "media")

    # Add .nojekyll
    (OUTPUT_DIR / ".nojekyll").touch()
    
    print(f"Static site generated in {OUTPUT_DIR}/")

if __name__ == "__main__":
    main()
