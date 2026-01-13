import yaml
from pathlib import Path

# Setup paths relative to this script
SCRIPT_DIR = Path(__file__).parent
POSTS_DIR = SCRIPT_DIR / "../posts"
BLOG_HTML = SCRIPT_DIR / "../blog.html"

def main():
    print(f"Scanning {POSTS_DIR}...")
    
    posts = []
    if POSTS_DIR.exists():
        for md_file in POSTS_DIR.glob("*.md"):
            try:
                content = md_file.read_text(encoding="utf-8")
                # Parse Front Matter
                if content.startswith("---"):
                    parts = content.split("---", 2)
                    if len(parts) >= 3:
                        meta = yaml.safe_load(parts[1])
                        posts.append({
                            "title": meta.get("title", "Untitled"),
                            "description": meta.get("description", ""),
                            "date": str(meta.get("date", "")),
                            "link": f"posts/{md_file.stem}.html"
                        })
            except Exception as e:
                print(f"Skipping {md_file.name}: {e}")

    # Sort by date (newest first)
    posts.sort(key=lambda x: x["date"], reverse=True)

    # Generate HTML for cards
    cards = []
    for p in posts:
        card = f"""
        <div class="blog-card">
          <h3>{p['title']}</h3>
          <p>{p['description']}</p>
          <div style="margin-top: auto; display: flex; justify-content: space-between; align-items: center; font-size: 0.9rem;">
            <span style="color: #6b7280;">{p['date']}</span>
            <a class="read-more" href="{p['link']}">Read more →</a>
          </div>
        </div>"""
        cards.append(card)

    html_cards = "\n".join(cards)

    # Inject into blog.html
    if BLOG_HTML.exists():
        content = BLOG_HTML.read_text(encoding="utf-8")
        start_marker = "<!-- BLOG_LIST_START -->"
        end_marker = "<!-- BLOG_LIST_END -->"

        if start_marker in content and end_marker in content:
            pre = content.split(start_marker)[0]
            post = content.split(end_marker)[1]
            new_content = f"{pre}{start_marker}\n{html_cards}\n        {end_marker}{post}"
            BLOG_HTML.write_text(new_content, encoding="utf-8")
            print(f"Blog index updated with {len(posts)} posts.")
        else:
            print("Markers not found in blog.html.")
    else:
        print("blog.html not found.")

if __name__ == "__main__":
    main()