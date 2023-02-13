import sys
input = sys.stdin.readline

def check(s):
    a = [s[0]]
    for i in range(1,len(s)):
        if s[i] != a[-1]:
            a.append(s[i])
    print(''.join(a))
    
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        s = str(input().rstrip())
        check(s)
    

'''
예제 입력 1 
3
ABBBBAACC
AAAAA
ABC
예제 출력 1 
ABAC
A
ABC
'''