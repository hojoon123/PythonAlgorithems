from sys import stdin
input = stdin.readline

def check(s):
    print(s[::-1])
    
if __name__ == '__main__':
    s = str(input().rstrip())
    check(s)
    
    
'''
예제 입력 1 
abc
예제 출력 1 
cba
'''