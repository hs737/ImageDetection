import click
import imagesearch

@click.group()
def main():
    """
        A command line tool to search and query images
        in a file system.
    """
    click.echo("main called")
    pass

@main.command(short_help='Search for a specific image')
@click.option('--recursive', is_flag=True)
@click.option('--follow_links', is_flag=True)
@click.option('--output_type')
@click.option('--query', type=click.Path(exists=True))
@click.argument('directory', type=click.Path(exists=True))
def search(directory, query=None, recursive=False, cache=None, output_type=None, follow_links=False):
    """
        Search a file system for either duplicate images in general
        or for duplicate images to a specific image.
    """
    click.echo("Search called directory: {}".format(directory))
    imagesearch.search(directory, recursive, query)

# @main.command(short_help='Search for all duplicate images for a particular path')
# @click.option('--recursive', is_flag=True)
# @click.argument('directory', type=click.Path(exists=True))
# def scan(directory, recursive=None):
#     """
#         Search a file system for all duplicate images.
#     """
#     imagesearch.search_

if __name__ == "__main__":
    main()
