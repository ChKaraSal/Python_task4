# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. 
# n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

element_1 = int(input('Введите количество элементов первого множества: '))
element_2 = int(input('Введите количество элементов второго множества: '))
array_1 = []
array_2 = []
for i in range(element_1):
    array_1.append(int(input('Введите элемент первого массива: ')))
for j in range(element_2):
    array_2.append(int(input('Введите элемент второго массива: ')))
array_3 = []
for i in array_1:
    if i in array_2 and i not in array_3:
            array_3.append(i)
array_3.sort()
print(array_3)