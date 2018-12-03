import cv2
import numpy
import imutils



face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
camera = cv2.VideoCapture(0)

PURPLE = (255, 0, 255)



finish = False

while not finish:

    T, frame = camera.read()
    frame = cv2.flip(frame, 1)
    #frame = imutils.resize(frame, width = 500, height = 500)

    brightness = numpy.ones(frame.shape, dtype = 'uint8') * 50
    frame = cv2.add(frame, brightness)


    faces = face_cascade.detectMultiScale(frame, 1.1, 5, 30)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), PURPLE, 2)

    if cv2.waitKey(0) and 0xFF == ord('q') :
        finish = False

    cv2.imshow("Faces", frame)


camera.release()
cv2.destroyAllWindows()
