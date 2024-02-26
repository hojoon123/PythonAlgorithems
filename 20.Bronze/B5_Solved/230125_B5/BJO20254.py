from sys import stdin
input = stdin.readline

def check(n, m, k, b):
    print(56 * n + 24 * m + 14 * k + 6 * b)
    
if __name__ == '__main__':
    n, m, k, b = map(int,input().split())
    check(n, m, k, b)
        
    
    
'''
56UR + 24TR + 14UO + 6TO
예제 입력 1 
1 1 1 1
예제 출력 1 
100
'''