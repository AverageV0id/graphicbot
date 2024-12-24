import cv2
import random


def face(face_cascade):
    cap = cv2.VideoCapture(0)
    a = True

    if not cap.isOpened():
        pass

    while a:
        ret, frame = cap.read()

        if not ret:
            print('Ошибка: Не удалось получить кадр')
            a = False

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray)
        result = cv2.bitwise_and(frame, frame)
        for (x, y, w, h) in faces:
            cv2.rectangle(result, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.imwrite('photo.jpg', result)
            a = False

        cv2.imshow('camera', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            a = False
    cap.release()
    cv2.destroyAllWindows()
