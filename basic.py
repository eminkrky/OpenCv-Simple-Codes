import cv2 as cv

img = cv.imread('Photos/car1.jpg')

# #Add Grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# #Add Blur
blur = cv.GaussianBlur(gray,(9,9), cv.BORDER_DEFAULT)

# Edge cascade
canny = cv.Canny(blur, 125, 175)

#dilate genişleme
dilated = cv.dilate(canny,(3,3),iterations=3)

#erode aşınmış
eroded = cv.erode(dilated,(3,3),iterations=3)

#Resize İmage
resized = cv.resize(img,(500,500))

#Crop image
cropped = img[100:-100,100:-100]


cv.imshow("Orginal",cropped)
cv.waitKey(0)