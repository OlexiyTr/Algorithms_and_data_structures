from math import sqrt

c = float(input())

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

    return left

def f(x):
    return x**2 + sqrt(x)

print(solve(f, c, 1, 10**5))
