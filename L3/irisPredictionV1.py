#!/usr/bin/env python
# coding: utf-8

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import mglearn
import pandas as pd
import numpy as np


def prediction(unicSize, measuringBorders):  # Конкретное измерение и зона класификации
    unicPredict = [0, 0, 0]  # Измерения относится Blue Red Green
    if unicSize[measuringBorders[2]] < measuringBorders[0]:
        unicPredict[0] += 1

    if unicSize[measuringBorders[2]] > measuringBorders[0] and unicSize[measuringBorders[2]] < measuringBorders[1]:
        unicPredict[1] += 1

    if unicSize[measuringBorders[2]] > measuringBorders[1]:
        unicPredict[2] += 1

    return unicPredict
iris_dataset = load_iris()

X_train, X_test, y_train, y_test = train_test_split(
 iris_dataset['data'], iris_dataset['target'], random_state=0)

measuringBorders = [  # Граница деления и категория
    [0.75, 1.75, 3],
    [2, 5, 2],
    [0.75, 1.75, 3],
    [2, 5, 2],
    [2, 4.80, 2],
    [2, 4.80, 2],
    [2, 4.80, 2],
    [0.75, 1.75, 3]
]

successResult = 0
for lm in range(len(X_test)):  # Проход по тестовым данным
    d = [0, 0, 0]
    for i in measuringBorders:  # Проход по значащим зонам
        res = prediction(X_test[lm], i)
        d = [d[0] + res[0], d[1] + res[1], d[2] + res[2]]

    if d.index(max(d)) == y_test[lm]:  # Определение правильности предсказания
        successResult += 1

print(str(successResult / len(X_test) * 100) + " %")
