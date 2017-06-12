##Uses Python3
import sys
n=int(input())
def pisano_period(m):
    R2=1
    R1=2
    j=4
    while R1!=1 and R2!=0:
        R=(R1%m)+(R2%m)
        R2=R1
        R1=R
        j=j+1
    return j-2

def fibonacci(n):
    k=pisano_period(10)
    c=(n+2)%k
    f=[]
    f.append(0)
    f.append(1)
    for i in range(2,c+1):
        f1=(f[i-1]+f[i-2])%10
        f.append(f1)
    return f[c]-1


print(fibonacci(n))

