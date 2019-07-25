import requests
import numpy as np
import cv2
while True:
    img_res = requests.get("http://10.2.21.51:8080/shot.jpg")
    img_arr = np.array(bytearray(img_res.content), dtype = np.uint8)
    img = cv2.imdecode(img_arr,-1)

    cv2.imshow('frame', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break