from sys import stdin
input = stdin.readline

def check(n):
    if n % 5 != 0:
        print(n // 5 + 1)
    else:
        print(n // 5)

if __name__ == '__main__':
    n = int(input())
    check(n)
        
    
    
'''
예제 입력 1 
12
예제 출력 1 
3
'''