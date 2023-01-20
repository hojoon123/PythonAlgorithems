from sys import stdin
input = stdin.readline

def check(n, k):
    a = [map(int,input().split()) for i in range(n)]
    print('비와이')

if __name__ == '__main__':
    n, k = map(int,input().split())
    check(n, k)
        
    
    
'''
예제 입력 1 
3 2
10 3
21 8
0 15
예제 출력 1 
비와이
'''