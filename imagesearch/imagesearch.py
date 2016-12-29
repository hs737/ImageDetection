import glob
import os
import imagehash
from PIL import Image

def search(dir_path, query_path):
    db = {}

    # loop over the image directory
    print("Finger printing each discovered image")
    image_paths = [x for x in glob.glob(os.path.join(dir_path, "*.jpg"))
                   if not os.path.samefile(query_path, x)]
    for image_path in image_paths:
        print("image path: {}".format(image_path))
        # load the image and compute the difference hash
        image = Image.open(image_path)
        h = str(imagehash.dhash(image))

        # extract the filename from the path and update the database
        # filename = image_path[image_path.rfind("/") + 1:]
        filename = os.path.basename(image_path)
        print("Filename: {}".format(filename))
        db[h] = (db[h] if h in db else []) + [filename]

    # load the query image, compute the difference image hash,
    # and grab the images from the database that have the same hash
    # value
    print("Querying discovered finger prints")
    query_image = Image.open(query_path)
    h = str(imagehash.dhash(query_image))
    filenames = db[h] if h in db else []
    print("Found {} images: {}".format(len(filenames), filenames))

    # loop over the images
    for filename in filenames:
        print("File found: {}".format(filename))
        image = Image.open(dir_path + "/" + filename)
        image.show()
