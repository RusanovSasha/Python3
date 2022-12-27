# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

def randomSpisok(length):
    array = []
    for i in range(length):
        array.append(random.randint(0, 100))
    return array

def summArr(array):
    summa = 0
    for i in array:
        summa += i
    return summa

print()
print("Добрейшего времени суток!")
print("Мы сегодня создадим список и посчитаем сумму элементов.")
print("Нужна твоя помощь. Сколько элементов будет в списке? ", end = "")
len = int(input())
arr = randomSpisok(len)

print()
print("Сгенерировали следующий список:")
print(arr)

print(f"Сумма элементов в массиве равна {summArr(arr)}")
