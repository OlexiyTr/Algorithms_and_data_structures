n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

counter = 0
lst.sort()

if n == 1:
    counter = lst[0]
if n == 2:
    counter = lst[1]
for i in range(n - 1, 1, -2):
    if i >= 3:
        counter += min( 2*lst[0] + lst[i-1] + lst[i], lst[0] + 2*lst[1] + lst[i])
        if i == 3:
            counter += lst[1]
    else:
        counter += lst[0] + lst[1] + lst[2]

print(counter)
