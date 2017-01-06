import glob
import os
import imagehash
import logging
from PIL import Image, ImageFile
from functools import partial
from sys import version_info
if version_info.major == 2:
    # We are using Python 2.x
    from imagesearch_utils import get_log_function_decorator
elif version_info.major == 3:
    # We are using Python 3.x
    from imagesearch.imagesearch_utils import get_log_function_decorator

ImageFile.LOAD_TRUNCATED_IMAGES = True

logger = logging.getLogger("imagesearch.business_logic")
log_function = partial(get_log_function_decorator, logger=logger)

@log_function
def search(dir_path, is_recursive, should_follow_links, is_verbose, query_path=None):
    ext = ".jpg"
    image_paths = []

    for path, dirnames, files in os.walk(dir_path, followlinks=should_follow_links):
        if not is_recursive:
            dirnames[:] = dirnames[0]

        image_paths += [os.path.join(path, filename) for filename in files
                        if filename.lower().endswith(ext.lower())]

    images_found = []
    if query_path:
        images_found = search_for_queried_image(image_paths, query_path)
    else:
        images_found = search_for_all_duplicates(image_paths)

    output_images_found(images_found)

def search_for_queried_image(image_paths, query_path):
    query_image = Image.open(query_path)
    query_hash = str(imagehash.dhash(query_image))
    images_found = []

    for image_path in image_paths:
        # logger.debug("Image path: {}".format(image_path))

        image = Image.open(image_path)
        image_hash = str(imagehash.dhash(image))

        # logger.debug("Image path: {}, Image hash: {}, Query hash: {}, EQ: {}".format(image_path, image_hash, query_hash, query_hash == image_hash))

        if query_hash == image_hash:
            # logger.debug("File found: {}".format(image_path))
            images_found.append([image_path])
            # image = Image.open(image_path)
            # image.show()

    # logger.debug("Images found: {}".format(images_found))
    return images_found

@log_function
def search_for_all_duplicates(image_paths):
    db = {}

    for image_path in image_paths:
        logger.debug("Image path: {}".format(image_path))

        image = Image.open(image_path)
        image_hash = str(imagehash.dhash(image))

        db[image_hash] = (db[image_hash] if image_hash in db else []) + [image_path]

    images_found = [db[image_hash] for image_hash in db if len(db[image_hash]) > 1]
    # logger.debug("Images found: {}".format(images_found))

    return images_found

@log_function
def output_images_found(images_found):
    for image_list in images_found:
        logger.debug("Image List found: {}".format(image_list))
        print(" ".join(image_list))

        # for image_path in image_list:
        #     image = Image.open(image_path)
        #     image.show()

