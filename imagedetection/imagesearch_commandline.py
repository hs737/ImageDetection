import click
import logging
from functools import partial
from sys import version_info
if version_info.major == 2:
    # We are using Python 2.x
    import imagesearch_business_logic as BL
    from imagesearch_utils import get_log_function_decorator
elif version_info.major == 3:
    # We are using Python 3.x
    import imagedetection.imagesearch_business_logic as BL
    # import imagedetection.imagesearch_business_logic as BL
    from imagedetection.imagesearch_utils import get_log_function_decorator

# create logger
logger = logging.getLogger("imagesearch")
log_function = partial(get_log_function_decorator, logger=logger)

@click.group()
@click.option('-v', '--verbose', is_flag=True,
              help="Increase verbosity of logs")
@click.option('-l', '--log', type=click.Path(dir_okay=False),
              help='Path to log file that will be created')
def cli(log=None, verbose=False):
    """
        A command line tool to search and query images
        in a file system.
    """

    setLogger(verbose, log)

@cli.command(short_help='Search for a specific image')
@click.option('-r', '--recursive', is_flag=True,
              help='Recursively searches through all sub-directories')
@click.option('-fl', '--follow_links', is_flag=True,
              help="Follow and resolve symbolic links")
@click.option('-q', '--query', type=click.Path(exists=True, dir_okay=False),
              help='Path to the image that is being searched')
@click.argument('directory', type=click.Path(exists=True), nargs=-1, required=True)
@log_function
def search(directory, query=None, recursive=False, follow_links=False):
    """
        Search a file system for either duplicate images in general
        or for duplicate images to a specific image.
    """
    # click.echo("Search called directory: {}".format(directory))
    BL.search(directory, recursive, follow_links, query_path=query)

@cli.command(short_help='Remove images that match the queried file')
@click.option('-r', '--recursive', is_flag=True,
              help='Recursively searches through all sub-directories')
@click.option('-f', '--force', is_flag=True,
              help='Attempt to remove the files without prompting for confirmation')
@click.option('-fl', '--follow_links', is_flag=True,
              help="Follow and resolve symbolic links")
@click.argument('query', type=click.Path(exists=True, dir_okay=False), required=True)
@click.argument('directory', type=click.Path(exists=True), nargs=-1, required=True)
@log_function
def remove(directory, query, recursive=False, follow_links=False, force=False):
    """
        Search and remove duplicate images in a direcotry, and its
        sub-directories, that match the queried image.
    """
    BL.remove(directory, query, recursive, follow_links, force)

def setLogger(is_verbose, log_path):
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s %(levelname)s - %(filename)s: %(lineno)d - %(message)s')

    if is_verbose and log_path:
        fh = logging.FileHandler(log_path)
        fh.setLevel(logging.NOTSET)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG if is_verbose else logging.ERROR)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
