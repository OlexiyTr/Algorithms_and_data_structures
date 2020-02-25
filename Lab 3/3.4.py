from math import sin

def solve(f, c, a, b):
    left = a
    right = b

    m = (left + right) / 2.0
    while left != m and m != right:
        if f(m) > c:
            left = m
        else:
            right = m
        m = (left + right) / 2.0

    return right

def f(x):
    return sin(x) - x/3

x = solve(f, 0, 1.6, 3)

print(x)
print(abs(sin(x) - x/3) < 0.000000000000001)
