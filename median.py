import cv2
from PIL import Image, ImageFilter
	
# creating a image object
im1 = Image.open("imagefilter.tif")
	
# applying the median filter
im2 = im1.filter(ImageFilter.MedianFilter(size = 9))
im2.show()
# cv2.imwrite("med3.png", im2)

# im3 = im1.filter(ImageFilter.MedianFilter(size = 6))
# cv2.imwrite("med6.png", im3)

# im4 = im1.filter(ImageFilter.MedianFilter(size = 9))
# cv2.imwrite("med9.png", im4)
 