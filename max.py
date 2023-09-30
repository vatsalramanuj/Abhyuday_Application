# Importing Image and ImageFilter module from PIL package
from PIL import Image, ImageFilter

# creating a image object
im1 = Image.open("imagefilter.tif")

# applying the min filter
im2 = im1.filter(ImageFilter.MaxFilter(size = 9))

im2.show()
