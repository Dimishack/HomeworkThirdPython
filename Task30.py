list_1 = list()

firstElement = int(input("Введите первое число: "))
step = int(input("Введите шаг: "))
quantity = int(input("Введите количество чисел: "))

list_1 = [i for i in range(firstElement, firstElement + step * quantity, step)]
print(list_1)