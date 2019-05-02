import cv2
import numpy as np


img = cv2.imread('hwimg.jpg')
rows, cols = img.shape[:2]

src_points = np.float32([[0,0], [0,0], [0,0], [0,0 ]])  
dst_points = np.float32([ [0,0], [0,rows-1], [cols-1, rows-1], [cols-1,0]])
num_pt = 0

def detect_circle (event, x, y, flags, param):
   global num_pt, src_points  
   if event == cv2.EVENT_LBUTTONDOWN :
       cv2.circle(img, (x,y), 5, (0,200,0), -1)
       src_points[num_pt][0] = x
       src_points[num_pt][1] = y
       num_pt= num_pt+1

cv2.namedWindow('original')
cv2.setMouseCallback('original', detect_circle)

while True:
    cv2.imshow('original', img)
    c = cv2.waitKey(10)
    if num_pt == 4:
        break
    
perspective_matrix = cv2.getPerspectiveTransform(src_points, dst_points)
img_perspective = cv2.warpPerspective(img, perspective_matrix, (cols, rows))
cv2.imshow('result',img_perspective)
