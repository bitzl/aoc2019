import click

from pathlib import Path

import stylegan


@click.group()
def cli():
    pass


@cli.command()
@click.argument("directory", help="The results directory to resume training")
def init(directory: str):
    target_path = Path(directory)
    stylegan.init(target_path)


@cli.command()
@click.argument("--target", "-c", help="The training config for new trainings")
def train(target: str):
    target_path = Path(target) / "config.yml"
    stylegan.train(target_path)


if __name__ == "__main__":
    cli()
