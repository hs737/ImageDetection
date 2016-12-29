# import the necessary packages
# from PIL import Image
# import imagehash
# import glob
import click

@click.command()
def cli():
    """Example script."""
    click.echo("hahaha")

# # construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-d", "--dataset", required = True, help = "path to input dataset of images")
# ap.add_argument("-q", "--query", required = True, help = "path to the query image")
# args = vars(ap.parse_args())
# print("Arguments: {}".format(args))

# db = {}

# # loop over the image dataset
# for imagePath in glob.glob(args["dataset"] + "/*.jpg"):
#     print("image path: {}".format(imagePath))
#     # load the image and compute the difference hash
#     image = Image.open(imagePath)
#     h = str(imagehash.dhash(image))

#     # extract the filename from the path and update the database
#     filename = imagePath[imagePath.rfind("/") + 1:]
#     db[h] = (db[h] if h in db else []) + [filename]

# # load the query image, compute the difference image hash,
# # and grab the images from the database that have the same hash
# # value
# query = Image.open(args["query"])
# h = str(imagehash.dhash(query))
# filenames = db[h] if h in db else []
# print("Found {} images".format(len(filenames)))

# # loop over the images
# for filename in filenames:
#     print("File found: {}".format(filename))
#     image = Image.open(args["dataset"] + "/" + filename)
#     image.show()
