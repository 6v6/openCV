import cv2
import numpy as np

img = cv2.imread('landscape.jpg')
rows, cols = img.shape[:2]

if(rows!=cols):
    if(rows>cols):  
        src_points = np.float32([ [0,0], [cols-1,0], [0,rows-1], [cols-1, rows-1] ])
        dst_points = np.float32([ [0,0], [rows-1,0], [0,rows-1], [rows-1, rows-1] ])
        perspective_matrix = cv2.getPerspectiveTransform(src_points, dst_points)
        cols=rows
        img_perspective = cv2.warpPerspective(img, perspective_matrix, (cols, rows))
    else:
        src_points = np.float32([ [0,0], [cols-1,0], [0,rows-1], [cols-1, rows-1] ])
        dst_points = np.float32([ [0,0], [cols-1,0], [0,cols-1], [cols-1, cols-1] ])
        perspective_matrix = cv2.getPerspectiveTransform(src_points, dst_points)
        rows=cols
        img_perspective = cv2.warpPerspective(img, perspective_matrix, (cols, rows))
        
def rotation(event, x, y, flags, param):
    global img_perspective
    if event == cv2.EVENT_LBUTTONDOWN:
        rotation_matrix = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
        img_perspective = cv2.warpAffine(img_perspective, rotation_matrix, (cols, rows))
    if event == cv2.EVENT_RBUTTONDOWN:
        rotation_matrix = cv2.getRotationMatrix2D((cols/2, rows/2), -90, 1)
        img_perspective = cv2.warpAffine(img_perspective, rotation_matrix, (cols, rows))


cv2.namedWindow('original')
cv2.setMouseCallback('original', rotation)

while True:
    cv2.imshow('original', img_perspective)
    c = cv2.waitKey(10)
    if c == 27:
        break
cv2.destroyAllWindows()
