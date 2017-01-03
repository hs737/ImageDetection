import glob
import os
import imagehash
from PIL import Image, ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

def search(dir_path, is_recursive, should_follow_links, query_path=None):
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
        # print("Image path: {}".format(image_path))

        image = Image.open(image_path)
        image_hash = str(imagehash.dhash(image))

        # print("Image path: {}, Image hash: {}, Query hash: {}, EQ: {}".format(image_path, image_hash, query_hash, query_hash == image_hash))

        if query_hash == image_hash:
            # print("File found: {}".format(image_path))
            images_found.append([image_path])
            # image = Image.open(image_path)
            # image.show()

    # print("Images found: {}".format(images_found))
    return images_found

def search_for_all_duplicates(image_paths):
    db = {}

    for image_path in image_paths:
        print("Image path: {}".format(image_path))

        image = Image.open(image_path)
        image_hash = str(imagehash.dhash(image))

        db[image_hash] = (db[image_hash] if image_hash in db else []) + [image_path]

    images_found = [db[image_hash] for image_hash in db if len(db[image_hash]) > 1]
    # print("Images found: {}".format(images_found))

    return images_found

def output_images_found(images_found):
    for image_list in images_found:
        print("Image List found: {}".format(image_list))

        # for image_path in image_list:
        #     image = Image.open(image_path)
        #     image.show()

