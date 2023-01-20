from sys import stdin
input = stdin.readline

def check(m, k):
    x = k // m
    y = k % m
    print(x, y)

if __name__ == '__main__':
    n, m, k = map(int,input().split())
    check(m, k)
        
    
    
'''
예제 입력 1 
3 4 6
예제 출력 1 
1 2
'''