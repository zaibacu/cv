import sys
import re
import markdown
from weasyprint import HTML

INPUT_FILE = sys.argv[1] if len(sys.argv) > 1 else "cv.md"
OUTPUT_FILE = sys.argv[2] if len(sys.argv) > 2 else "cv.pdf"

CSS = """
@page {
    size: A4;
    margin: 2cm 2cm 2cm 2cm;
}

body {
    font-family: 'Poppins', 'Liberation Sans', sans-serif;
    font-size: 9.5pt;
    line-height: 1.45;
    color: #1A1A2E;
}

h1 {
    font-size: 22pt;
    font-weight: 700;
    color: #1A1A2E;
    text-align: center;
    margin-bottom: 2pt;
    letter-spacing: 0.5pt;
}

/* Subtitle line (first bold paragraph after h1) */
h1 + p {
    text-align: center;
    color: #2B4C7E;
    font-style: italic;
    font-size: 11pt;
    margin-top: 0;
    margin-bottom: 2pt;
}

/* Contact line (second paragraph after h1) */
h1 + p + p {
    text-align: center;
    color: #555;
    font-size: 9pt;
    margin-top: 0;
    margin-bottom: 2pt;
}

/* Third paragraph (social links) */
h1 + p + p + p {
    text-align: center;
    color: #555;
    font-size: 9pt;
    margin-top: 0;
    margin-bottom: 6pt;
}

h2 {
    font-size: 13pt;
    font-weight: 700;
    color: #2B4C7E;
    text-transform: uppercase;
    letter-spacing: 1pt;
    margin-top: 10pt;
    margin-bottom: 4pt;
    padding-bottom: 2pt;
    border-bottom: none;
}

h3 {
    font-size: 10.5pt;
    font-weight: 700;
    color: #1A1A2E;
    margin-top: 6pt;
    margin-bottom: 1pt;
}

h3 em {
    font-weight: 400;
    color: #555;
}

hr {
    border: none;
    border-top: 0.5pt solid #ccc;
    margin: 4pt 0;
}

p {
    margin-top: 2pt;
    margin-bottom: 2pt;
}

em {
    color: #555;
    font-size: 9pt;
}

ul {
    margin-top: 2pt;
    margin-bottom: 2pt;
    padding-left: 16pt;
}

li {
    margin-bottom: 1pt;
}

li::marker {
    color: #2B4C7E;
}

strong {
    font-weight: 600;
    color: #1A1A2E;
}

a {
    color: #2B4C7E;
    text-decoration: none;
}
"""

def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        md_text = f.read()

    html_body = markdown.markdown(md_text, extensions=["extra"])

    full_html = f"""<!DOCTYPE html>
<html lang="lt">
<head>
<meta charset="utf-8">
<style>{CSS}</style>
</head>
<body>
{html_body}
</body>
</html>"""

    HTML(string=full_html).write_pdf(OUTPUT_FILE)
    print(f"✓ Generated {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
