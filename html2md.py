import argparse
import os
import requests
import html2text

def fetch_webpage(url):
    """
    Fetch HTML content from a URL.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        raise RuntimeError(f"Failed to fetch URL: {e}")

def read_file(path):
    """
    Read HTML content from a local file.
    """
    if not os.path.isfile(path):
        raise FileNotFoundError(f"File not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def html_to_markdown(html_content):
    """
    Convert HTML content to Markdown.
    """
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.body_width = 0
    return h.handle(html_content).strip()

def main():
    parser = argparse.ArgumentParser(description="Convert HTML or a webpage to Markdown.")
    parser.add_argument("input", help="Path to HTML file or URL")
    parser.add_argument("-o", "--output", help="Path to save Markdown output", default="output.md")

    args = parser.parse_args()

    # Determine if input is a URL or file
    if args.input.startswith("http://") or args.input.startswith("https://"):
        html_content = fetch_webpage(args.input)
    else:
        html_content = read_file(args.input)

    markdown = html_to_markdown(html_content)

    # Save to file
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(markdown)

    print(f"Markdown saved to {args.output}")

if __name__ == "__main__":
    main()
