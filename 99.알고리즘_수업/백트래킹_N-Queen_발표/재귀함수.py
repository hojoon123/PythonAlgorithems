import sys
input = sys.stdin.readline

def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    
    return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    n = 4
    print(fib(n))
    