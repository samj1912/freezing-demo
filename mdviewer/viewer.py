import tempfile
import webbrowser

from typing import TextIO


def display(html: str, output_path: str) -> None:
    with open(output_path, "w") as f:
        f.write(html)
    webbrowser.open(output_path)
