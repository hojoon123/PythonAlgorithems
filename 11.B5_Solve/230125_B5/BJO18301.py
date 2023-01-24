from sys import stdin
input = stdin.readline

def check(n, m, k):
    print(abs(((n + 1) * (m + 1)) // (k + 1) - 1))
    
if __name__ == '__main__':
    n, m, k = map(int,input().split())
    check(n, m, k)
        
    
    
'''
N := ⌊(n1 + 1)(n2 + 1)/(n12 + 1) - 1⌋
예제 입력 1 
15 18 11
예제 출력 1 
24
'''