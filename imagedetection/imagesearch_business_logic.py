import glob
import os
import imagehash
import logging
from PIL import Image, ImageFile
from functools import partial
from sys import version_info
from builtins import input
if version_info.major == 2:
    # We are using Python 2.x
    from imagesearch_utils import get_log_function_decorator
elif version_info.major == 3:
    # We are using Python 3.x
    from imagedetection.imagesearch_utils import get_log_function_decorator

ImageFile.LOAD_TRUNCATED_IMAGES = True

logger = logging.getLogger("imagesearch.business_logic")
log_function = partial(get_log_function_decorator, logger=logger)

@log_function
def search(dir_path, is_recursive, should_follow_links, query_path=None):
    image_paths = get_list_of_image_paths(dir_path,
                                          is_recursive,
                                          should_follow_links)

    images_found = []
    if query_path:
        images_found = search_for_queried_image(image_paths, query_path)
    else:
        images_found = search_for_all_duplicates(image_paths)

    output_images_found(images_found)

@log_function
def remove(dir_path, query_path, is_recursive, should_follow_links, is_force):
    image_paths = get_list_of_image_paths(dir_path,
                                          is_recursive,
                                          should_follow_links)
    images_found = search_for_queried_image(image_paths, query_path)

    if is_force:
        for image_path in images_found:
            if image_path != query_path:
                logger.debug("Removing image '{}'".format(image_path))
                os.remove(image_path)
    else:
        for image_path in images_found:
            if image_path != query_path:
                response = input("Remove image '{}'? ".format(image_path))
                if response.lower() == 'y':
                    os.remove(image_path)

@log_function
def get_list_of_image_paths(dir_paths, is_recursive, should_follow_links):
    ext = ".jpg"
    image_paths = []

    if is_recursive:
        for dir_path in dir_paths:
            for path, dirnames, files in os.walk(dir_path, followlinks=should_follow_links):
                logger.debug("Path: {}, Dir Names: {}, Files: {}".format(path, dirnames, files))
                image_paths += [os.path.join(path, filename) for filename in files
                                if filename.lower().endswith(ext.lower())]
    else:
        for dir_path in dir_paths:
            for image_path in os.listdir(dir_path):
                filename = os.path.join(dir_path, image_path)
                if os.path.isfile(filename) and filename.lower().endswith(ext.lower()):
                    logger.debug("Filename: {}".format(filename))
                    image_paths.append(filename)

    logger.debug("Image paths found: {}".format(image_paths))
    return image_paths


@log_function
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
            images_found.append(image_path)
            # image = Image.open(image_path)
            # image.show()

    logger.debug("Images found: {}".format(images_found))
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
    for images in images_found:
        logger.debug("Image List found: {} {}".format(images, type(images)))
        if isinstance(images, list):
            print(" ".join(images))
        else:
            print(images)

        # for image_path in image_list:
        #     image = Image.open(image_path)
        #     image.show()
