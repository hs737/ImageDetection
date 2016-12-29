import click
import imagesearch

@click.group()
def main():
    """
        A command line tool to search and query images
        in a file system.
    """
    click.echo("Hello Wo!")

@main.command(short_help='Search for a specific image')
@click.option('--recursive')
@click.option('--output_type')
# @click.argument('directory', help='The path to the directory being searched')
@click.argument('directory', type=click.Path(exists=True))
@click.argument('query', type=click.Path(exists=True))
def search(query, directory, recursive=None, cache=None, output_type=None):
    """
        Search a file system for either duplicate images in general
        or for duplicate images to a specific image.
    """
    click.echo("Directory: {}".format(directory))
    imagesearch.search(directory, query)

@main.command(short_help='Search for all duplicate images')
@click.option('--query', type=click.Path(exists=True), help='Path to image being queried')
@click.option('--recursive')
@click.option('--output_type')
# @click.argument('directory', help='The path to the directory being searched')
@click.argument('directory', type=click.Path(exists=True))
def discover_duplicates(directory, query=None, recursive=None, cache=None, output_type=None):
    """
        Search a file system for all duplicate images.
    """
    pass

if __name__ == "__main__":
    main()
