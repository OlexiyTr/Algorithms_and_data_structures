def max_score(score, num):
    global maxScore, s, n

    if num >= s:
        if score > maxScore and score <= n:
            maxScore = score
        return

    max_score(score,          num + 1)
    max_score(score + a[num], num + 1)

while True:
    try:
        a = list(map(int, input().split()))
        n, s, a = a[0], a[1], a[2:]
        maxScore = 0
        max_score(0, 0)
        print(f'sum:{maxScore}')
    except:
        break
