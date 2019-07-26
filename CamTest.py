import cv2
import numpy as np
import time

cam = cv2.VideoCapture('http://10.2.21.51:8080/videofeed') # passandro o atributo 0 vc conecta na web cam padrão

time.sleep(2)

while True:
    ret,frame = cam.read()
    cv2.imshow('webcam', frame)
    if cv2.waitKey(1)&0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()