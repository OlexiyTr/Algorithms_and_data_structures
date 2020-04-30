from math import factorial

n,m = map(int,input().split())
m-=1
str = ''

lst = [chr(i) for i in range(97,97+n)]
for i in range(n):
    fc = factorial(n-i-1)
    x = m//factorial(n-i-1)
    str = str + lst.pop(x)
    m = m%fc

print(str)
