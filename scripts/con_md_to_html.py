import argparse
import logging
import markdown
import yaml
from pathlib import Path
from typing import Any, Dict, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)

def parse_front_matter(content: str) -> Tuple[Dict[str, Any], str]:
    """
    Separates YAML front matter from Markdown content.
    Returns a tuple of (metadata_dict, markdown_body).
    """
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            try:
                meta = yaml.safe_load(parts[1]) or {}
                body = parts[2]
                return meta, body
            except yaml.YAMLError as e:
                logger.warning(f"YAML parsing error: {e}")
    
    return {}, content

def convert_md_to_html(file_path: str) -> Optional[Path]:
    """
    Reads a Markdown file, converts it to HTML, and saves it with a .html extension.
    Returns the output path if successful, None otherwise.
    """
    md_file = Path(file_path)
    if not md_file.is_file():
        logger.error(f"The file '{file_path}' does not exist.")
        return None

    try:
        content = md_file.read_text(encoding="utf-8")
        meta, body = parse_front_matter(content)

        html_body = markdown.markdown(body, extensions=["fenced_code", "tables"])
        
        # Load Template
        script_dir = Path(__file__).parent
        template_path = script_dir / "../templates/post.html"
        
        final_output = html_body
        
        if template_path.exists():
            template = template_path.read_text(encoding="utf-8")
            final_output = template \
                .replace("{{ title }}", str(meta.get("title", "Untitled"))) \
                .replace("{{ description }}", str(meta.get("description", ""))) \
                .replace("{{ date }}", str(meta.get("date", ""))) \
                .replace("{{ author }}", str(meta.get("author", ""))) \
                .replace("{{ content }}", html_body)
        else:
             logger.warning("Template not found. Outputting raw HTML body.")

        # Determine output file name (replace extension with .html)
        output_file = md_file.with_suffix(".html")
        output_file.write_text(final_output, encoding="utf-8")
        
        logger.info(f"Successfully converted '{md_file}' to '{output_file}'")
        return output_file

    except Exception as e:
        logger.error(f"Error converting file: {e}")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a Markdown file to HTML.")
    parser.add_argument("file_path", help="Path to the Markdown file to convert.")
    
    args = parser.parse_args()
    convert_md_to_html(args.file_path)
