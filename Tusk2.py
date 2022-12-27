#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

#Пример:

#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

import random
import math

def randomSpisok(length):
    array = []
    for i in range(length):
        array.append(random.randint(0, 10))
    return array

def resultArr(array):
    newArr = []
    whereToGo = math.ceil(len(array)/2)
    for i in range(whereToGo):
        newArr.append(array[i] * array[-1*(i+1)])
    return newArr


print()
print("Через тернии к высшему порядку в коде!")
print("Создадим список и перемножим пары чисел. Парой будет считать первый и последний элемент, второй и предпоследний и т.д.")
print("Почувствуй себя творцом, определи судьбу списка.")
print("Скажи, из какого количества элементов он будет состоять? ", end = "")
lenArr = int(input())
arr = randomSpisok(lenArr)

print()
print("Сгенерировали следующий список:")
print(arr)

print(f"Судьба списка вершиться сейчас. Расчет произведения пар окончен. Принимай результат {resultArr(arr)}")
