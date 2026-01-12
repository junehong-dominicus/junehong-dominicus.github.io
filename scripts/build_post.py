import markdown
import yaml
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description="Convert Markdown to HTML.")
parser.add_argument("input", nargs="?", default="../posts/2026-01-11-RAG.md", help="Input Markdown file")
parser.add_argument("output", nargs="?", default="../posts/2026-01-11-RAG.html", help="Output HTML file")
args = parser.parse_args()

POST_MD = Path(args.input)
TEMPLATE = Path("../templates/post.html")
OUTPUT = Path(args.output)

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
