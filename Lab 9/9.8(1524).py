from math import factorial

num = int(input())

def prob(n,k):
    return factorial(n+k)//(factorial(k)*factorial(n))

arr = []

for u in range(num):
    n,t,p = map(int,input().split())
    t = t - n * p
    x = prob(n-1,t)
    arr += [x]

for i in arr:
    print(i)
