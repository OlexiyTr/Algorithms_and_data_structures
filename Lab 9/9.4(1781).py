from copy import copy

def max_score(num, first, second, guests, ind, last):
    global n, a, dk
    if num >= n-1:
        dk.append(first)
        return

    guests[ind] = False
    if first > second:
        for i in range(0,n):
            if guests[i]:
                max_score(num+1,first,second+a[i],copy(guests),i, 's')
    elif first < second:
        for i in range(n-1,0,-1):
            if guests[i]:
                max_score(num+1,first+a[i],second,copy(guests),i, 'f')
                break
    else:
        if last == 's':
            for i in range(0,n):
                if guests[i]:
                    max_score(num+1,first,second+a[i],copy(guests),i, 's')
        else:
            for i in range(n-1,0,-1):
                if guests[i]:
                    max_score(num+1,first+a[i],second,copy(guests),i, 'f')
                    break




n = int(input())*2
a = list(map(int, input().split()))

dk = []
guests = [True]*n

max_score(0, a[0], 0,copy(guests),0, 'f')

print(min(dk))
