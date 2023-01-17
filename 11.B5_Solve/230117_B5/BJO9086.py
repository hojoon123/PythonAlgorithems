from sys import stdin
input = stdin.readline

def check(s):
    print(s[0], s[-1], sep = '')
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input().rstrip())
        check(s)
        
    
    
'''
예제 입력 1 
3
ACDKJFOWIEGHE
O
AB
예제 출력 1 
AE
OO
AB
'''