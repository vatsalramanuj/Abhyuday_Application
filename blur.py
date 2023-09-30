import cv2
import numpy as np
from PIL import Image as im

img = cv2.imread("imagefilter.tif")
avg3 = cv2.blur(img, (3,3))
cv2.imwrite("avg3.png", avg3)

cv2.imwrite("log.png",np.log(img) )
z = cv2.imread("log.png")
for i in range(3):
    ksize = 3*(i+1)
    geomean = np.uint8(np.exp(cv2.blur(z, (ksize, ksize))))
    cv2.imwrite("geomean_{}.png".format(ksize),geomean)


avg6 = cv2.blur(img, (6,6))
cv2.imwrite("avg6.png", avg6)


avg9 = cv2.blur(img, (9,9))

cv2.imwrite("avg9.png", avg9)

