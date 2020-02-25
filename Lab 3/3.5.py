from math import sin

def solve(f, c, a, b):
    left = a
    right = b

    m = (left + right) / 2.0
    while left != m and m != right:
        if f(m) < c:
            left = m
        else:
            right = m
        m = (left + right) / 2.0

    return right

def f(x):
    return x**3 + 4 * x**2 + x - 6

x = solve(f, 0, 0, 2)

print(x)
print(abs(x**3 + 4 * x**2 + x - 6) < 0.000000000000001)
