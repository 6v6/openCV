# -*- coding: utf-8 -*-

import cv2
import numpy as np
#라이브러리 등록



font = cv2.FONT_HERSHEY_SIMPLEX

def faceDetect():
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    try:
        cap=cv2.VideoCapture(0)
    except:
        print('카메라 로딩 실패')
        return
    while True:
        ret, frame = cap.read()
        if not ret:
            return
        gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 2, 0, (30, 30))
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3, 4, 0)
            cv2.putText(frame, 'Detected Face', (x-5, y-5), font, 0.9, (255,255,0),2)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break   
    cap.release()
    cv2.destroyAllWindows()
#q를 누르면 실행 종료되는 코드

faceDetect()
