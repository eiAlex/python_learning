# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import cv2
from darkflow.net.build import TFNet
import numpy as np
import time
import csv
import pandas as pd

options = {
    'model': 'cfg/yolo.cfg',
    'load': 'bin/yolov2.weights',
    'threshold': 0.2,
    'gpu': 0.2
}

tfnet = TFNet(options)
colors = [tuple(255 * np.random.rand(3)) for _ in range(10)]

#capture = cv2.VideoCapture('http://10.2.21.51:8080/videofeed')
capture = cv2.VideoCapture(0)

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
#c = csv.writer(open("MEUARQUIVO.csv", "wb"))

index = 1
while True:
    stime = time.time()
    ret, frame = capture.read()
    if ret:
        results = tfnet.return_predict(frame)
        for color, result in zip(colors, results):
            tl = (result['topleft']['x'], result['topleft']['y'])
            br = (result['bottomright']['x'], result['bottomright']['y'])
            label = result['label']
            confidence = result['confidence']
            text = '{}: {:.0f}%'.format(label, confidence * 100)
            frame = cv2.rectangle(frame, tl, br, color, 5)
            frame = cv2.putText(
                frame, text, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
        cv2.imshow('frame', frame)
        print('FPS {:.1f}'.format(1 / (time.time() - stime)))
        print(results, index)
        #c.writerow(["Nome","Endereço","Telefone","Fax","E-mail","Outros"])
        
        #c.writerow('nome')
    index += 1
    #raw_data = {'ID': index,'TIPO': [result['label']], 'confidence': [result['confidence']]}
    raw_data = {'ID': index}
 
    
        


    if cv2.waitKey(1) & 0xFF == ord('q'):
        #df = pd.DataFrame(raw_data, columns = ['ID','TIPO', 'confidence'])  
        df = pd.DataFrame(raw_data, columns = ['ID'])         
        df.to_csv('example.csv')
        
        break

capture.release()
cv2.destroyAllWindows()