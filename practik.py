"""Калькулятор"""
while True:

    try:
        a = int(input("Введите первое число: "))
        break
    except ValueError:
        print("Введите корректные данные")
    continue

b = input("Введите арифметический знак: ")

while True:

    try:
        c = int(input("Введите второе число: "))
        break
    except ValueError:
        print("Введите корректные данные")
    continue

if b == "+":
    result = a + c
    print("Результат: " + str(result))

elif b == "-":
     result = a - c
     print("Результат: " + str(result))

elif b == "*":
     result = a * c
     print("Результат: " + str(result))

elif b == "/":
     try:
         result = a / c
     except ZeroDivisionError:
         result = 0
         print("На 0 делить нельзя")
     print("Результат: " + str(result))
else:
    print("Неизвестная операция")
