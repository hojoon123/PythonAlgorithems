from sys import stdin
input = stdin.readline

def check(n):
    tmp = 0
    for i in range(0, 4, 2):
        tmp += n[i] * n[i + 1]
    print(tmp)
    
if __name__ == '__main__':
    n = list(map(int,input().split()))
    check(n)
    
    
'''
예제 입력 1 
2 5 3 20
예제 출력 1 
70
'''