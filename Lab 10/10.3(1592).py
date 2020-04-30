def step(n, output):
    if n == 1:
        if output:
            print(m[0])
        return m[0]
    elif n == 2:
        if output:
            print(m[0], m[1])
        return m[1]
    elif n == 3:
        if output:
            print(m[0], m[1])
            print(m[0])
            print(m[0], m[2])
        return m[0] + m[1] + m[2]
    First = m[0] + 2*m[1] + m[n-1]
    Second = 2*m[0] + m[n-2] + m[n-1]
    Best = First if First < Second else Second
    if output:
        if Best == First:
            print(m[0], m[1])
            print(m[0])
            print(m[n - 2], m[n - 1])
            print(m[1])
        else:
            print(m[0], m[n - 2])
            print(m[0])
            print(m[0], m[n - 1])
            print(m[0])
    return Best + step(n - 2, output)

while True:
    try:
        n = int(input())
        m = list(map(int, input().split()))
    except:
        break
    m.sort()
    result = step(n, False)
    print(result)
    step(n, True)
