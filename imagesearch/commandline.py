import click
import imagesearch

@click.command(short_help='Search for a specific image')
@click.option('-r', '--recursive', is_flag=True,
              help='Recursively searches through all sub-directories')
@click.option('-fl', '--follow_links', is_flag=True, help="Follow and resolve symbolic links")
@click.option('--output_type')
@click.option('-q', '--query', type=click.Path(exists=True, dir_okay=False),
              help='Path to the image that is being searched')
@click.argument('directory', type=click.Path(exists=True))
def cli(directory, query=None, recursive=False, cache=None,
           output_type=None, follow_links=False):
    """
        Search a file system for either duplicate images in general
        or for duplicate images to a specific image.
    """
    # click.echo("Search called directory: {}".format(directory))
    imagesearch.search(directory, recursive, query, follow_links)
