##Uses Python3
import sys
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


def fibonacci(n,m):
    k=pisano_period(10)
    c=(n+2)%k
    d=(m+2)%k
    f=[]
    f.append(0)
    f.append(1)
    for i in range(2,d+1):
        f1=(f[i-1]+f[i-2])
        f.append(f1)
    a=f[d]-f[c-1]
    a=a%10
    return a

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(fibonacci(a, b))
