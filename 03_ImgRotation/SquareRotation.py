import cv2
import numpy as np

img = cv2.imread('hw2img.jpg')
num_rows, num_cols = img.shape[:2]
def rotation(event, x, y, flags, param):
    global img
    if event == cv2.EVENT_LBUTTONDOWN:
        rotation_matrix = cv2.getRotationMatrix2D((num_cols/2, num_rows/2), 90, 1)
        img = cv2.warpAffine(img, rotation_matrix, (num_cols, num_rows))
        
    if event == cv2.EVENT_RBUTTONDOWN:
        rotation_matrix = cv2.getRotationMatrix2D((num_cols/2, num_rows/2), -90, 1)
        img = cv2.warpAffine(img, rotation_matrix, (num_cols, num_rows))
        
cv2.namedWindow('original')
cv2.setMouseCallback('original', rotation)
while True:
    cv2.imshow('original', img)
    c = cv2.waitKey(10)
    if c == 27:
        break
cv2.destroyAllWindows()
