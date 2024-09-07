import cmath

def solve_quadratic(x, s, a, b, c):
    da = ((x ** 2) + (s ** 2) - (2 * a) * b * (cmath.cos(c)))
    return (cmath.sqrt(da))

result = solve_quadratic(1, 2, 3, 4, 0.7)
print("Получилось:", result)