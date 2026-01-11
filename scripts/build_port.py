import markdown
import yaml
from pathlib import Path

POST_MD = Path("../posts/2026-01-11-RAG.md")
TEMPLATE = Path("../templates/post.html")
OUTPUT = Path("../posts/2026-01-11-RAG.html")

raw = POST_MD.read_text()

front_matter, body = raw.split("---", 2)[1:]
meta = yaml.safe_load(front_matter)
html_body = markdown.markdown(body, extensions=["fenced_code"])

template = TEMPLATE.read_text()

output = template \
    .replace("{{ title }}", meta["title"]) \
    .replace("{{ description }}", meta["description"]) \
    .replace("{{ date }}", meta["date"]) \
    .replace("{{ author }}", meta["author"]) \
    .replace("{{ content }}", html_body)

OUTPUT.write_text(output)

print("Post built:", OUTPUT)
