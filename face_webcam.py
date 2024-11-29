import cv2
import time

video_path = 'bill.mp4'

video = cv2.VideoCapture(video_path)
#video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    if not check:
        print("End of video.")
        break

    if cv2.waitKey(10) & 0xFF == ord('q'):
        print('pressed q')
        break
    cv2.imshow("Capturing Frame", frame)

cv2.waitKey(0)
video.release()
cv2.destroyAllWindows()