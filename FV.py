#!/usr/bin/env python
# coding: utf-8

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import mglearn
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

iris_dataset = load_iris()

print("Ключи iris_dataset: \n{}".format(iris_dataset.keys()))
print(iris_dataset['DESCR'][:193] + "\n...")
print("Названия ответов: {}".format(iris_dataset['target_names']))
print("Названия признаков: \n{}".format(iris_dataset['feature_names']))
print("Тип массива data: {}".format(type(iris_dataset['data'])))
print("Форма массива data: {}".format(iris_dataset['data'].shape))
print("Первые пять строк массива data:\n{}".format(iris_dataset['data'][:5]))
print("Тип массива target: {}".format(type(iris_dataset['target'])))
print("Форма массива target: {}".format(iris_dataset['target'].shape))
print("Ответы:\n{}".format(iris_dataset['target']))


X_train, X_test, y_train, y_test = train_test_split(
 iris_dataset['data'], iris_dataset['target'], random_state=0)
print("форма массива X_train: {}".format(X_train.shape))
print("форма массива y_train: {}".format(y_train.shape))
print("форма массива X_test: {}".format(X_test.shape))
print("форма массива y_test: {}".format(y_test.shape))


iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset.feature_names)
# создаем матрицу рассеяния из dataframe, цвет точек задаем с помощью y_train
grr = pd.plotting.scatter_matrix(iris_dataframe, c=y_train, figsize=(15, 15),
                                 marker='o', hist_kwds={'bins': 20}, s=60,
                                 alpha=.8, cmap=mglearn.cm3)
plt.show()

def prediction(unicSize, measuringBorders):  # Конкретное измерение и зона класификации
    unicPredict = [0, 0, 0]  # Измерения относится Blue Red Green
    if unicSize[measuringBorders[2]] < measuringBorders[0]:
        unicPredict[0] += 1

    if unicSize[measuringBorders[2]] > measuringBorders[0] and unicSize[measuringBorders[2]] < measuringBorders[1]:
        unicPredict[1] += 1

    if unicSize[measuringBorders[2]] > measuringBorders[1]:
        unicPredict[2] += 1

    return unicPredict
  
 measuringBorders = [  # Граница деления и категория
    [0.75, 1.75, 3],
    [2, 4.80, 2]

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
