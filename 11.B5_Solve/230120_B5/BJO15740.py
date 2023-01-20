from sys import stdin
input = stdin.readline

def check(n, k):
    print(n + k)

if __name__ == '__main__':
    n, k = map(int,input().split())
    check(n, k)
        
    
    
'''
예제 입력 1 
1 2
예제 출력 1 
3
'''