import pkgutil
from typing import TextIO
from markdown import markdown
from mdx_gfm import GithubFlavoredMarkdownExtension as GFM

CSS_STYLE = pkgutil.get_data("mdviewer", "markdown.css").decode()

def converter(input_file: TextIO) -> str:
    parsed_html = markdown(input_file.read(), extensions=[GFM()])
    html_page = create_html(parsed_html)
    return html_page


def create_html(input_html: str) -> str:
    return f"""
    <html>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        {CSS_STYLE}
    </style>
    <article class="markdown-body">
        {input_html}
    </article>
    </html>
    """
