import math

def solve_quadratic(x):
    l = x + 1
    k =x - 1
    return ((math.sqrt(l)) + (math.sqrt(k))) / (2 * math.sqrt(x))
roots = solve_quadratic(4)
print("Получилось:", roots)