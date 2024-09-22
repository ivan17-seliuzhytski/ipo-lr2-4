import math
x = float(input("Введите x: "))
y = float(input("Введите y: "))
z = float(input("Введите z: "))
h = (pow(x, y + 1) + math.exp(y - 1)) / (1 + x * abs(y - math.tan(z))) * (1 + abs(y - x)) + (pow(abs(y - x), 2)) / 2 - (pow(abs(y - x), 3)) / 3
print("h равно: ", h)