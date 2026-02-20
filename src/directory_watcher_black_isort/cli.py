import click
from .core import format_on_save

@click.command()
@click.option('--watch-directory', default='src/', help='Directory to watch for changes.')
@click.option('--black-args', multiple=True, help='Arguments for Black formatter.')
@click.option('--isort-args', multiple=True, help='Arguments for isort formatter.')
def cli(watch_directory, black_args, isort_args):
    """A CLI tool that watches a directory for changes and auto-formats Python files on save."""
    format_on_save(watch_directory, black_args, isort_args)

if __name__ == '__main__':
    cli()