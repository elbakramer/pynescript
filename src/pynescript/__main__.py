"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Pynescript."""


if __name__ == "__main__":
    main(prog_name="pynescript")  # pragma: no cover
