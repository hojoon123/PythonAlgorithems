from sys import stdin
input = stdin.readline

def check(a, b):
    print((a + b) * (a - b))

if __name__ == '__main__':
    a, b =map(int,input().split())
    check(a, b)
        
    
    
'''
A＠B = (A+B)×(A-B)
'''