import argparse
import markdown
import sys
import yaml
from pathlib import Path

def convert_md_to_html(file_path):
    """
    Reads a Markdown file, converts it to HTML, and saves it with a .html extension.
    Returns the output path if successful, None otherwise.
    """
    md_file = Path(file_path)
    if not md_file.is_file():
        print(f"Error: The file '{file_path}' does not exist.")
        return None

    try:
        content = md_file.read_text(encoding='utf-8')

        meta = {}
        body = content
        # Strip Front Matter if present (to avoid rendering YAML as text)
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                try:
                    meta = yaml.safe_load(parts[1]) or {}
                    body = parts[2]
                except yaml.YAMLError as e:
                    print(f"Warning: YAML parsing error: {e}")

        html_body = markdown.markdown(body, extensions=['fenced_code', 'tables'])
        
        # Load Template
        script_dir = Path(__file__).parent
        template_path = script_dir / "../templates/post.html"
        
        final_output = html_body
        
        if template_path.exists():
            template = template_path.read_text(encoding='utf-8')
            final_output = template \
                .replace("{{ title }}", meta.get("title", "Untitled")) \
                .replace("{{ description }}", meta.get("description", "")) \
                .replace("{{ date }}", str(meta.get("date", ""))) \
                .replace("{{ author }}", meta.get("author", "")) \
                .replace("{{ content }}", html_body)
        else:
             print("Warning: Template not found. Outputting raw HTML body.")

        # Determine output file name (replace extension with .html)
        output_file = md_file.with_suffix(".html")
        output_file.write_text(final_output, encoding='utf-8')
        
        print(f"Successfully converted '{md_file}' to '{output_file}'")
        return output_file

    except Exception as e:
        print(f"Error converting file: {e}")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a Markdown file to HTML.")
    parser.add_argument("file_path", help="Path to the Markdown file to convert.")
    
    args = parser.parse_args()
    convert_md_to_html(args.file_path)
