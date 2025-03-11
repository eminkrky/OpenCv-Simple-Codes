import cv2 as cv
import numpy as np

img = cv.imread("Photos/car1.jpg")

# Translation İmage
def translate (img, x, y) :
    transMat = np. float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)
# +x Right
# -x Left
# +y Up
# -y Down
# img = translate(img,-0,0)


# Görüntüyü göster
cv.imshow("Image", img)
cv.waitKey(0)
cv.destroyAllWindows()