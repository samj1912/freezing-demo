import pkgutil
import logging
from typing import TextIO
from markdown import markdown
from mdx_gfm import GithubFlavoredMarkdownExtension as GFM

logger = logging.getLogger(__name__)

try:
    CSS_STYLE = pkgutil.get_data("mdviewer", "markdown.css").decode()
except IOError:
    logger.warning("Unable to import fancy style sheets. Make do with 1980s html you pleb.")
    CSS_STYLE = ""


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
