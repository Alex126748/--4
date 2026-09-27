#a = float(input("Введите длину первой стороны прямоугольника: "))
#b = float(input("Введите длину второй стороны прямоугольника: "))
#area = a * b
#perimeter = 2 * (a + b)

#print(f"Площадь прямоугольника = {area}")
#print(f"Периметр прямомоугольника = {perimeter}")

a = 46275
#digits = list(str(a))
digits = [int(i) for i in str(a)]
print(digits)
print(digits[0])
print(digits[1])
print(digits[2])
print(digits[3])
print(digits[4])

algorithm = digits[3] ** digits[4] * digits[2] / (digits[0] - digits[1])
print(algorithm)