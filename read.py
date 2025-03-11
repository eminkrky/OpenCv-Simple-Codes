import cv2 as cv


def changeFrame(frame):
        
        new_width = 600
        new_height = int(frame.shape[0] * (new_width/frame.shape[1]) )

        diemensions = (new_width,new_height)

        return cv.resize(frame, diemensions, interpolation=cv.INTER_AREA)
 

def rescaleFrame(frame, scale=.5):
        
        width = int(frame.shape[1] * scale)
        height = int(frame.shape[0] * scale)

        diemensions = (width,height)

        return cv.resize(frame, diemensions, interpolation=cv.INTER_AREA)

def changeRes(widht,height):
      capture.set(3,widht)
      capture.set(4,height)
      


# for i in range(1,10):
#     img = cv.imread("Photos/car"+str(i)+".jpg")

#     resized_image = rescaleFrame(img)

#     cv.imshow("Car"+str(i) , img)
#     cv.waitKey(0)



    



# capture = cv.VideoCapture('Videos/car1.mp4')
capture = cv.VideoCapture(1)

while True:
    isTrue, frame = capture.read()

    #frame_resized = rescaleFrame(frame)
    #cv.imshow("car1",frame)
    cv.putText(frame,'Hello, my name is Emin',(0,frame.shape[0]//2),cv.FONT_HERSHEY_COMPLEX_SMALL, 1.4, (0,0,0),1)
    cv.imshow("car resized",frame)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

