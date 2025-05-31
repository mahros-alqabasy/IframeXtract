# iframextract/extractor.py

from bs4 import BeautifulSoup
import os


def format_filename(template, filename, index, title):
    name = os.path.splitext(os.path.basename(filename))[0]
    title_sanitized = "".join(
        c if c.isalnum() or c in "-_ " else "_" for c in title
    ).strip()
    return template.format(
        filename=name, iframe_index=index, iframe_title=title_sanitized
    )


def extract_iframes_from_file(input_path, output_dir, name_template):
    with open(input_path, "r", encoding="utf-8") as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, "html.parser")
    iframes = soup.find_all("iframe")

    os.makedirs(output_dir, exist_ok=True)

    for idx, iframe in enumerate(iframes):
        title = iframe.get("title", f"iframe-{idx}")
        filename = format_filename(name_template, input_path, idx, title)
        output_path = os.path.join(output_dir, filename)

        standalone_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{title}</title>
</head>
<body>
  {str(iframe)}
</body>
</html>
"""

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(standalone_html)

        print(f"Extracted iframe '{title}' to {output_path}")


def extract_iframes_from_directory(input_dir, output_dir, name_template):
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith(".html"):
                extract_iframes_from_file(
                    os.path.join(root, file), output_dir, name_template
                )
