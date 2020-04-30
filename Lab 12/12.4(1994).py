def build (a,v,l,r):
    if l==r:
        lst[v][0], lst[v][1] = a[l], 0
    else:
        mid = l + (r - l)//2
        build (a,v*2,l,mid)
        build (a,v*2 + 1,mid+1,r)
        lst[v][0], lst[v][1] = min(lst[v*2][0], lst[v*2+1][0]),0

def push(v, l, mid, r):
    if lst[v][1]:
        lst[2*v][1] += lst[v][1]
        lst[2*v][0] += lst[v][1]
        lst[2*v+1][1] += lst[v][1]
        lst[2*v+1][0] += lst[v][1]
        lst[v][1] = 0;

def add(v, l, r, L, R, val):
    if L > R:
        return
    if l >= L and r >= R:
        lst[v][1] += val;
        lst[v][0] += val;
        return
    mid = l + (r - l)//2
    push(v,l,mid,r)
    add(2*v,l,mid,L,min(mid,R),val)
    add(2*v+1,mid+1,r,L,max(L,mid+1),val)
    lst[v][0] = min(lst[2*v][0],lst[2*v+1][0])


st = list(input())
n = len(st)
summ = 0
numbers = []
lst = [[0,0]]*100010*4

for i in range(n):
    if st[i] == '()':
        summ+=1
    else:
        summ-+1
    numbers.append(summ)
build (numbers, 1, 0, n - 1)

k = int(input())

for i in range(k):
    p = int(input())
    if st[p] == '(':
        st[p] = ')'
        add(1,0,n-1,p,n-1,-2)
        summ-=2
    else:
        st[p] = '('
        add(1,0,n-1,p,n-1,2)
        summ+=2
    if lst[1][0] >= 0 and summ == 0:
        print('+')
    else:
        print('-')
