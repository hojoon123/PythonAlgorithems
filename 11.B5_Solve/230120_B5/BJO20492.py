from sys import stdin
input = stdin.readline

def check(n):
    tmp = int(n * 0.78)
    tmp2 = int(n - ((n * 0.2) * 0.22))
    print(tmp, tmp2)
    
if __name__ == '__main__':
    n = int(input().rstrip())
    check(n)
        
    
    
'''
예제 입력 1 
10000000
예제 출력 1 
7800000 9560000
'''