##Uses Python3
import sys
def LCM(a,b):
    d=a*b
    while b!=1 and b!=0:
        c = a % b
        a = b
        b = c
    if b == 1:
        GCD=b
    else:
        GCD=a
    LCM_F=(d)//GCD
    return int(LCM_F)



if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(LCM(a, b))
