# computer vision cv
import cv2
# create a capture object 
cap = cv2.VideoCapture(0)
while True:
    # cap return two things , which one we dont used then the var name _
    _, frame = cap.read()
    cv2.imshow("Output",frame)
    
    if cv2.waitKey(10) == ord('q'):
        break
cap.relase()
cv2.destroyAllWindows()
