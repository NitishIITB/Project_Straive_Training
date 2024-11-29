import cv2
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"
image = cv2.imread('text.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_,thresholded = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow('thes',thresholded)
text = pytesseract.image_to_string(Image.fromarray(thresholded), config='--psm 11')
text = text.strip()
print(text)

cv2.imshow('Original Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()