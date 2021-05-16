import cv2
import os
from os import path
from random import randrange
from tkinter import messagebox

trained_face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def detect_face(file):
    img = cv2.imread(file)

    grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    font = cv2.FONT_HERSHEY_SIMPLEX
    if face_coordinates != ():
        for (a, b, c, d) in face_coordinates:
            cv2.rectangle(img, (c + a, d + b), (a, b), (randrange(0, 256), randrange(0, 256), randrange(0, 256)), 3)
            cv2.putText(img, '(' + str(c+a) + ', ' + str(d+b) + ')', (c+a, d+b + 15), font, d/255, (randrange(0, 256), randrange(0, 256), randrange(0, 256)))
            cv2.putText(img, '(' + str(a) + ', ' + str(b) + ')', (a, b-10), font, d/255, (randrange(0, 256), randrange(0, 256), randrange(0, 256)))


        filename = ''
        position = 0
        for i in file[::-1]:
            if i == '/':
                filename = file[-position:]
                break
            position += 1

        filename += '_detected.jpg'


        to_path = path.realpath(__file__)
        count = 0
        for i in to_path[::-1]:
            count += 1
            if i == '\\':
                to_path = to_path[:-count]
                break
        try:
            os.makedirs('output')
        except:
            pass
        to_path = to_path + '\\output'
        cv2.imwrite(os.path.join(to_path, filename), img)
        print("Finished!")
    else:
        messagebox.showerror("Error", "No faces detected!")
