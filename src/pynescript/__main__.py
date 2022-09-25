"""Command-line interface."""
import click


@click.group()
@click.version_option()
def cli():
    pass


@cli.command(short_help="Parse pinescript file to AST tree.")
@click.argument(
    "filename",
    metavar="PATH",
    type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True),
)
@click.option(
    "--encoding",
    default="utf-8",
    help="Text encoding of the file.",
)
@click.option(
    "--indent",
    type=int,
    default=2,
    help="Indentation with of an AST dump.",
)
@click.option(
    "--output-file",
    metavar="PATH",
    type=click.Path(writable=True, allow_dash=True),
    help="Path to output dump file, defaults to standard output.",
    default="-",
)
def parse_and_dump(filename, encoding, indent, output_file):
    from pynescript.ast import dump
    from pynescript.ast import parse_file

    with click.open_file(filename, "r", encoding=encoding) as f:
        script_node = parse_file(f, encoding=encoding)

    script_node_dump = dump(script_node, indent=indent)

    with click.open_file(output_file, "w", encoding=encoding) as f:
        f.write(script_node_dump)


@cli.command(short_help="Parse pinescript file and unparse back to pinescript.")
@click.argument(
    "filename",
    metavar="PATH",
    type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True),
)
@click.option(
    "--encoding",
    default="utf-8",
    help="Text encoding of the file.",
)
@click.option(
    "--output-file",
    metavar="PATH",
    type=click.Path(writable=True, allow_dash=True),
    help="Path to output dump file, defaults to standard output.",
    default="-",
)
def parse_and_unparse(filename, encoding, output_file):
    from pynescript.ast import parse_file
    from pynescript.ast import unparse

    with click.open_file(filename, "r", encoding=encoding) as f:
        script_node = parse_file(f, encoding=encoding)

    unparsed_script = unparse(script_node)

    with click.open_file(output_file, "w", encoding=encoding) as f:
        f.write(unparsed_script)


@cli.command(short_help="Download builtin scripts.")
@click.option(
    "--script-dir",
    type=click.Path(exists=False, file_okay=False, writable=True),
    help="Diretory where scripts to be saved (like tests/data/builtin_scripts).",
    required=True,
)
def download_builtin_scripts(script_dir):
    from pynescript.utils.pine_facade import download_builtin_scripts as download

    download(script_dir)


if __name__ == "__main__":
    cli(prog_name="pynescript")  # pragma: no cover
