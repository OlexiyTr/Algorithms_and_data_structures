n = int(input())
st = [0] + list(map(int, input().split()))

for i in range(1, n//2+1):
    if 2*i <= n and st[i] > st[2*i]:
        print('NO')
        exit(0)
    if 2*i + 1 <= n and st[i] > st[2*i + 1]:
        print('NO')
        exit(0)

print('YES')
