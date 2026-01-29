import markdown
import yaml
import math
from pathlib import Path

def convert_md_to_html(md_file_path):
    md_path = Path(md_file_path)
    if not md_path.exists():
        print(f"File not found: {md_path}")
        return

    print(f"Converting {md_path.name}...")
    content = md_path.read_text(encoding="utf-8")
    
    # Parse Front Matter
    meta = {}
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            meta = yaml.safe_load(parts[1])
            md_content = parts[2]
        else:
            md_content = content
    else:
        md_content = content

    # Convert Markdown
    html_content = markdown.markdown(md_content, extensions=['fenced_code', 'tables'])

    # Template
    title = meta.get("title", "Blog Post")
    description = meta.get("description", "")
    author = meta.get("author", "June Hong")
    date = meta.get("date", "")
    tags = meta.get("tags", [])

    # Calculate Read Time (approx 200 words per minute)
    word_count = len(md_content.split())
    read_time = max(1, math.ceil(word_count / 200))

    # Generate Tags HTML
    tags_html = ""
    if tags:
        tags_list = "".join([f'<span class="tag">{tag}</span>' for tag in tags])
        tags_html = f'<div class="tags-container">{tags_list}</div>'

    template = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} – June Hong</title>
  <link rel="icon" type="image/png" href="../assets/images/JHD.png">
  <link rel="stylesheet" href="../style.css">
  <meta name="description" content="{description}">
  <meta name="author" content="{author}">
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5789326916093083"
     crossorigin="anonymous"></script>
</head>

<body>
  <nav>
    <div class="nav-inner">
      <a href="../index.html" class="nav-brand">
        <img src="../assets/images/JHD.png" alt="JH" class="monogram" />
        <span>June Hong, Dominicus</span>
      </a>
      <div class="nav-links">
        <a href="../index.html">Home</a>
        <a href="../projects.html">Projects</a>
        <a href="../blog.html">Blog</a>
        <a href="https://github.com/junehong-dominicus" target="_blank">GitHub</a>
        <a href="https://www.linkedin.com/in/junehong-dominicus/" target="_blank">LinkedIn</a>
      </div>
    </div>
  </nav>

  <header class="article-header">
    <div class="ad-container">
        <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-5789326916093083" data-ad-slot="1816196154" data-ad-format="auto" data-full-width-responsive="true"></ins>
        <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
    </div>
    <h1>{title}</h1>
    <div class="article-meta">
      <span class="meta-item">By {author}</span>
      <span class="meta-item">📅 {date}</span>
      <span class="meta-item">⏱️ {read_time} min read</span>
    </div>
    {tags_html}
  </header>

  <main class="article-container">
    <article>
      {html_content}
    </article>
  </main>

  <footer>© 2026 June Hong — Built with plain HTML & CSS</footer>
</body>
</html>"""

    output_path = md_path.with_suffix(".html")
    output_path.write_text(template, encoding="utf-8")
    print(f"Generated {output_path.name}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        convert_md_to_html(sys.argv[1])