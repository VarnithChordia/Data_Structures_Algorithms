##Uses Python3
def calc_fib(n):
    f=[]
    f.append(0)
    f.append(1)
    for i in range(2,n+1):
        a=f[i-2]+f[i-1]
        f.append(a)
    return f[n]

m=int(input())

print(calc_fib(m))