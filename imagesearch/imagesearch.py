import glob
from PIL import Image
import imagehash

def search(query_path, dir_path):
    print("hah")

    db = {}

    # loop over the image directory
    for imagePath in glob.glob(dir_path + "/*.jpg"):
        print("image path: {}".format(imagePath))
        # load the image and compute the difference hash
        image = Image.open(imagePath)
        h = str(imagehash.dhash(image))

        # extract the filename from the path and update the database
        filename = imagePath[imagePath.rfind("/") + 1:]
        db[h] = (db[h] if h in db else []) + [filename]

    # load the query image, compute the difference image hash,
    # and grab the images from the database that have the same hash
    # value
    queryImage = Image.open(query_path)
    h = str(imagehash.dhash(queryImage))
    filenames = db[h] if h in db else []
    print("Found {} images".format(len(filenames)))

    # loop over the images
    for filename in filenames:
        print("File found: {}".format(filename))
        image = Image.open(dir_path + "/" + filename)
        image.show()
