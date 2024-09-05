import math

def solve_quadratic(a):
    x = (1 - (math.sin(a) ** 2))
    return (math.sqrt(x))

first = solve_quadratic(1)
print("результат:", first)