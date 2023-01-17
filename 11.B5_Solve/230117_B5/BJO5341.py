from sys import stdin
input = stdin.readline

def check(n):
    tmp = 0
    for i in range(1, n + 1):
        tmp += i
    print(tmp)

if __name__ == '__main__':
    while 1:
        n = int(input())
        if n == 0:
            exit()
        check(n)
    
'''
예제 입력 1 
4
6
0
예제 출력 1 
10
21
'''