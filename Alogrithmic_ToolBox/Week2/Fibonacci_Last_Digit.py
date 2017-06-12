##Uses Python3
def fibonacci_lastdigit(n):
    f=[]
    f.append(0)
    f.append(1)
    for i in range(2,n+1):
        a=(f[i-2]+f[i-1])%10
        f.append(a)
    return (f[n])


m=int(input())

print(fibonacci_lastdigit(m))

