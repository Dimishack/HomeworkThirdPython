# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
arr = [4, 2, 62, -4, 2, 54, -6]
indexs = list()
min = int(input("Введите минимальные диапазон: "))
max = int(input("Введите максимальный диапазон: "))
for i in range(len(arr)):
    if arr[i] >= min and arr[i] <= max:
        indexs.append(i)
print(indexs)
