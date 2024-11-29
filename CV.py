import cv2
#import img as img
img = cv2.imread('opencv.png',0)
print(img)
cv2.imshow('gr',img)
cv2.waitKey(0)
cv2.waitKey(20000)
cv2.destroyAllWindows()
