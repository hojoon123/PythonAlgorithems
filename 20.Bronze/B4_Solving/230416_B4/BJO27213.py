import sys
input = sys.stdin.readline

def check(n, m):
    if n == 1 or m == 1:
        print(m + n - 1)
    else:
        print(((n + m) * 2) - 4)
    return 
if __name__ == '__main__':
    n = int(input())
    m = int(input())
    check(n, m)
        
    

'''
print(((a+b)*2)-4)
'''