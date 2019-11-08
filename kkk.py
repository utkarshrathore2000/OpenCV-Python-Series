import cv2
import sys
human_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    human= human_cascade.detectMultiScale(
        gray,1.1,4)
#        flags=cv2.cv.CV_HAAR_SCALE_IMAGE)
    for (x, y, w, h) in human:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 220), 3)
    s=cv2.imshow('Video', frame)
    print(s)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
