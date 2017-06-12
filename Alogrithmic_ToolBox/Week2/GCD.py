##Uses Python3
import sys
def GCD(a,b):
    while b!=1 and b!=0:
        c = a % b
        a = b
        b = c
    if b == 1:
        return b
    else:
        return a

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(GCD(a, b))
