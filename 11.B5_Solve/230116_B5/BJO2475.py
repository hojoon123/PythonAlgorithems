from sys import stdin
input = stdin.readline

def verify(arr):
    tmp = 0
    for i in arr:
        tmp  += i ** 2
    print(tmp % 10)

if __name__ == '__main__':
    arr = list(map(int,input().split()))
    verify(arr)


'''
예제 입력 1 
0 4 2 5 6
예제 출력 1 
1
'''