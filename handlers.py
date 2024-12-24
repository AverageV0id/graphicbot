import telebot
from setting import *
import cv2
import numpy as np
from new import *
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +
                                     'haarcascade_lefteye_2splits.xml')
bot = telebot.TeleBot(token)
lower_red = np.array([100, 0, 0])
upper_red = np.array(([300, 255, 255]))

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f"Приветствую!")


@bot.message_handler(commands=['face'])
def face(message):
    cap = cv2.VideoCapture(0)
    a = True

    if not cap.isOpened():
        pass

    while a:
        ret, frame = cap.read()

        if not ret:
            print('Ошибка: Не удалось получить кадр')
            a = False
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        mask = cv2.inRange(hsv, lower_red, upper_red)
        faces = face_cascade.detectMultiScale(gray)

        result = cv2.bitwise_and(frame, frame)
        for (x, y, w, h) in faces:
            cv2.line(result, (x+20, y+30), (x+random.randint(0,255) + w+25, y+200 + h+25), (0, 0, 255), 15)
            cv2.imwrite('photo.jpg', result)
            with open('photo.jpg', "rb") as photo:
                bot.send_photo(message.chat.id, photo)

        cv2.imshow('camera', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            a = False

        print(face_cascade)
