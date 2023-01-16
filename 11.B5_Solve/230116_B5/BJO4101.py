from sys import stdin
input = stdin.readline

def check(a, b):
    if a > b :
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    while 1:
        a, b = map(int,input().split())
        if a == 0 and b == 0:
            break
        check(a, b)


'''
예제 입력 1 
1 19
4 4
23 14
0 0
예제 출력 1 
No
No
Yes
'''