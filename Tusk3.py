# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

#[1.1, 1.2, 3.1, 5, 10.01] => 0.19


import random
import math

def randomSpisok(length):
    array = []
    for i in range(length):
        array.append(round(random.random()*10,2))
    return array

def resultArr(array):
    if array[0]%1>array[1]%1:
        min = array[1]%1
        max = array[0]%1
    else:
        min = array[0]%1
        max = array[1]%1       
    for i in range(2, len(array)):
        if array[i]%1<min:
            min = array[i]%1
        if array[i]%1>max:
            max = array[i]%1    
    answer = round((max - min),2)
    return answer


print()
print('"Здесь куют СПИСКИ!"')
print("Добрый день, здрав Государь. Сколько элементов списка тебе отчеканить? ", end = "")
lenArr = int(input())
arr = randomSpisok(lenArr)

print()
print("Выкован следующий список:")
print(arr)

print(f"Алтарь силы говорит, что разница между максимальным и минимальным значением дробной части элементов равна {resultArr(arr)} ... чтобы это не значило, Государь.")
