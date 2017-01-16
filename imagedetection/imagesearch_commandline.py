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
    import imagesearch.imagesearch_business_logic as BL
    from imagesearch.imagesearch_utils import get_log_function_decorator

# create logger with 'spam_application'
logger = logging.getLogger("imagesearch")
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s %(levelname)s - %(filename)s: %(lineno)d - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)
log_function = partial(get_log_function_decorator, logger=logger)

@click.group()
def cli():
    """
        A command line tool to search and query images
        in a file system.
    """
    # click.echo("cli called")
    pass

@cli.command(short_help='Search for a specific image')
@click.option('-r', '--recursive', is_flag=True,
              help='Recursively searches through all sub-directories')
@click.option('-fl', '--follow_links', is_flag=True,
              help="Follow and resolve symbolic links")
@click.option('-v', '--verbose', is_flag=True,
              help="Increase verbosity of logs")
@click.option('--output_type')
@click.option('-q', '--query', type=click.Path(exists=True, dir_okay=False),
              help='Path to the image that is being searched')
@click.argument('directory', type=click.Path(exists=True))
@log_function
def search(directory, query=None, recursive=False, cache=None,
           output_type=None, verbose=False, follow_links=False):
    """
        Search a file system for either duplicate images in general
        or for duplicate images to a specific image.
    """
    # click.echo("Search called directory: {}".format(directory))
    BL.search(directory, recursive, follow_links, verbose, query_path=query)

@cli.command(short_help='Remove images that match the queried file')
@click.option('-r', '--recursive', is_flag=True,
              help='Recursively searches through all sub-directories')
@click.option('-f', '--force', is_flag=True,
              help='Attempt to remove the files without prompting for confirmation')
@click.option('-fl', '--follow_links', is_flag=True,
              help="Follow and resolve symbolic links")
@click.option('-v', '--verbose', is_flag=True,
              help="Increase verbosity of logs")
@click.argument('query', type=click.Path(exists=True, dir_okay=False))
@click.argument('directory', type=click.Path(exists=True))
@log_function
def remove(directory, query, recursive=False, verbose=False,
           follow_links=False, force=False):
    """
        Search and remove duplicate images in a direcotry, and its
        sub-directories, that match the queried image.
    """
    BL.remove(directory, query, recursive, follow_links, verbose, force)
