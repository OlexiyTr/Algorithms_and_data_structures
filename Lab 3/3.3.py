def solve(f, c, a, b):
    left = a
    right = b

    m = (left + right) / 2.0
    while left != m and m != right:
        if f(m) > c:
            right = m
        else:
            left = m
        m = (left + right) / 2.0

    return right

def f(x):
    return x**3 + x - 4

print(solve(f, 0, 0, 10))
