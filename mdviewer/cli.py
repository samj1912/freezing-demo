import click

from .parser import converter
from .viewer import display


@click.command()
@click.argument("input_file", type=click.File("r"))
@click.argument("output_path", type=click.Path(writable=True, resolve_path=True))
def convert(input_file, output_path):
    parsed_html = converter(input_file)
    display(parsed_html, output_path)
