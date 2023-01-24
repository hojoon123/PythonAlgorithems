from sys import stdin
input = stdin.readline

def check(a, b):
    print(a * b)
    
if __name__ == '__main__':
    n, m= map(int,input().split())
    a = int(input())
    b = int(input())
    check(a, b)
        
    
    
'''
예제 입력 1 
3 4
123
4567
예제 출력 1 
561741
'''