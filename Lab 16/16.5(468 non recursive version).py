MAX = 2147483647
MIN = -2147483648

nodes = list(map(int, input().split()))
prev = nodes[0]

while True:
    for cur in nodes:
        if cur < MIN or cur > MAX:
            print('NO')
            exit(0)
        if cur > prev:
            MIN = prev
        elif cur < prev:
            MAX = prev
        prev = cur

    try:
        nodes = list(map(int, input().split()))
    except:
        print('YES')
        break
