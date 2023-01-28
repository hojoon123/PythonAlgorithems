from sys import stdin
input = stdin.readline

def check(n):
    print(sum(n) * 5)
    
if __name__ == '__main__':
    n = list(map(int,input().split()))
    check(n)
        
    
    
'''
예제 입력 1 
0 0 0 23 3 100
예제 출력 1 
630
'''