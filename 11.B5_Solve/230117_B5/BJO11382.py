from sys import stdin
input = stdin.readline

def check(a, b, c):
    print(a + b + c)

if __name__ == '__main__':
    a, b, c = map(int,input().split())
    check(a, b, c)
        
    
    
'''
예제 입력 1 
77 77 7777
예제 출력 1 
7931
'''