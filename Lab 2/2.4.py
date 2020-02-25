n = int(input())

m = n
step = n.bit_length()-1
n1 = ((n<<1)&((1<<step+1)-1)) | (n >> step)

while n1 != n:
    n1 = ((n1<<1)&((1<<step+1)-1)) | (n1 >> step)
    if n1 > m:
        m = n1

print(m)
