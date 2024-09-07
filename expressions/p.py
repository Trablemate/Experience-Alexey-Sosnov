import math

def solve_quadratic(a, b, c, x):
    l = (a * x ** 2) + (b * x) + c
    return (1 / math.sqrt(l))
result = solve_quadratic(1, 2, 3, 4)
print("Получилось:", result)