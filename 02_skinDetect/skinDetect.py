import cv2
import numpy as np

# 1 컬러모델 선택
answer = input("컬러모델 선택(y/h)")


cap = cv2.VideoCapture('injung.mp4')   
lower_skin = np.array([0,133,77])
upper_skin = np.array([255,173,127])

hsv_lower_skin = np.array([0,70,50])
hsv_upper_skin = np.array([50,150, 255])
while True:
    ret, frame = cap.read()
    if ret:
        if answer == 'y':
            # 2 선택된 컬러모델로 변환
            convert_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2YCR_CB)
            
             # 3 픽셀별로 피부색인지 확인
            mask = cv2.inRange(convert_frame,lower_skin,upper_skin)
            res = cv2.bitwise_and(frame,frame,mask=mask)
            
            # 4 rgb모델로 변환
            back = cv2.cvtColor(convert_frame,cv2.COLOR_YCR_CB2BGR)
            
        elif answer == 'h':
            # 2 선택된 컬러모델로 변환
            convert_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            
            # 3 픽셀별로 피부색인지 확인
            mask = cv2.inRange(convert_frame,hsv_lower_skin,hsv_upper_skin)
            res = cv2.bitwise_and(frame,frame,mask=mask)
            
            # 4 rgb모델로 변환
            back = cv2.cvtColor(convert_frame,cv2.COLOR_HSV2BGR)
            
        cv2.imshow('Input1', convert_frame)
        cv2.imshow('Input2', res)
        cv2.imshow('Input3', back)
        cv2.waitKey(1)
    else:
        break

cap.release()
cv2.destroyAllWindows()

    
