from sys import stdin
input = stdin.readline

def check(n):
    tmp = []
    for i in range(2, 4):
        tmp.append(i * (n + 1))
    print(*tmp)
if __name__ == '__main__':
    n = int(input())
    check(n)
    
    
'''
예제 입력 1 
5
예제 출력 1 
12 18
'''