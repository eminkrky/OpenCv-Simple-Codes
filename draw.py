import cv2 as cv
import numpy as np

#Boş resim oluşturma
blank = np.zeros((500,500,3), dtype='uint8')
#cv.imshow("Blank", blank)

# Boş resmi renklendirme
#blank[200:300 , 200:300] = 0,100,255
blank[:] = 0,100,255
# cv.imshow("Red", blank)



#Dikdörtgen çizme
#cv.rectangle(blank, (200,200), (300,300), (0,250,0), thickness=2)
# cv.imshow("Rectangle",blank)

#Daire Çizme
#cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2),250,(0,255,255),thickness=1)
#cv.imshow("Circle",blank)

#Çizgi çizme
# cv.line(blank, (200,250), (300,250), (0,250,0), thickness=2)
# cv.imshow("Line",blank)

#Yazı Yazma
cv.putText(blank,'Hello, my name is Emin',(0,250),cv.FONT_HERSHEY_COMPLEX_SMALL, 1.4, (0,0,0),1)
cv.imshow("Text",blank)




cv.waitKey(0)
    

