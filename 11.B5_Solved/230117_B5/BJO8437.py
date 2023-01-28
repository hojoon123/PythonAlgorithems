from sys import stdin
input = stdin.readline

def check(n):
    print((n[0] + n[1]) // 2)
    print((n[0] - n[1]) // 2)
    
if __name__ == '__main__':
    n = [0] * 2
    for i in range(2):
        n[i] = int(input())
    check(n)
    
    
'''
예제 입력 1 
10
2
예제 출력 1 
6
4
'''