import sys
import math
input = sys.stdin.readline

def check(l,a,b,c,d):
    bugger = min(l,a,b)
    drink = min(c,d)
    return bugger + drink - 50
if __name__ == '__main__':
    l = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    print(check(l,a,b,c,d))
    

'''
예제 입력 1 
800
700
900
198
330
예제 출력 1 
848
'''