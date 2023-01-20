from sys import stdin
input = stdin.readline

def check(n, m):
    print(m - n, m)

if __name__ == '__main__':
    n, m =map(int,input().split())
    check(n, m)
        
    
    
'''
예제 입력 1 
2 7
예제 출력 1 
5 7
'''