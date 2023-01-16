from sys import stdin
input = stdin.readline

def check(a, b):
    if len(a) >= len(b):
        print('go')
    else:
        print('no')

if __name__ == '__main__':
    a = str(input().rstrip())
    b = str(input().rstrip())
    check(a, b)


'''
예제 입력 1 
aaah
aaaaah
예제 출력 1 
no
예제 입력 2 
aaah
ah
예제 출력 2 
go
'''