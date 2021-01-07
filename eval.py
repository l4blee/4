# -*- coding: utf-8 -*-
# импортируйте все библиотеки, которые вам понадобятся
import cv2
import os


def standardize_input(img_path):
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    img = cv2.inRange(img, (0, 0, 0), (255, 45, 255))
    img = cv2.erode(img, (3, 3), iterations=4)
    img = cv2.dilate(img, (3, 3), iterations=4)

    c = max(cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)[0], key=cv2.contourArea)
    extreme = tuple(c[c[:, :, 0].argmin()][0]), tuple(c[c[:, :, 1].argmin()][0]), \
              tuple(c[c[:, :, 0].argmax()][0]), tuple(c[c[:, :, 1].argmax()][0])
    x, y = (extreme[0][0], extreme[1][1]), (extreme[2][0], extreme[3][1])
    img = source_img[x[1]:y[1], x[0]:y[0]]

    return img


MODEL_FILE_NAME = ''  # Пропишите путь к вашей модели


def load_final_model():
    """ Функция осуществляет загрузку модели машинного обучения из файла MODEL_FILE_NAME.
        Выходные параметры: загруженная модель
    """
    # TODO: Функция загрузки модели
    model = tuple()
    return model


def predict(image, model):
    """ Функция осуществляет подачу данных на вход модели и возвращает вектор формата [1, 2]. Длина вектора может быть от 1 до 3.
         Входные параметры: изображение
         Выходные параметры: вектор с определёнными цифрами на изображении.
    """
    # TODO: Функция предсказания вектора цифр по заданной картинке
    vec = tuple()
    return vec


# Просмотр обработанных картинок в директории path
path = 'pictures_numeric_train/21'
for filename in os.listdir(path):
    file = path + '/' + filename
    source = cv2.imread(file)
    image = standardize_input(source)

    cv2.imshow('image', image)
    while True:
        if cv2.waitKey(0) == ord('q'):
            cv2.destroyWindow('image')
            break
