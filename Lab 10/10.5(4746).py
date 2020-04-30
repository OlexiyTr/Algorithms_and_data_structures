n = int(input())
lst = list(map(int,input().split()))

lst = sorted(lst, reverse = True, key=lambda x: x)
MaxScore = 0
t = 0
for el in lst:
    if el - t<=0:
        break
    MaxScore += el-t
    t+= 1

print(MaxScore)
