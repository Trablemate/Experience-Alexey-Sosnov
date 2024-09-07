import math

def solve_quadratic(a, s):
    y = (a ** 2) + (s ** 2)
    return (math.sqrt(y))

first = solve_quadratic(1, 2)
print("Получилось:", first)