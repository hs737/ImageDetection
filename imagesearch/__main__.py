import click

@click.group()
def main():
    """
        A command line tool to search and query images
        in a file system.
    """
    click.echo("Hello Wo!")

@main.command(short_help='Search for duplicate images')
@click.option('--query', type=click.Path(exists=True), help='Path to image being queried')
# @click.argument('directory', help='The path to the directory being searched')
@click.argument('directory', type=click.Path(exists=True))
def duplicates(directory, query=None):
    """
        Search a file system for either duplicate imagess in general
        or for duplicate images to a specific image.
    """
    click.echo("Wolly")

if __name__ == "__main__":
    main()
