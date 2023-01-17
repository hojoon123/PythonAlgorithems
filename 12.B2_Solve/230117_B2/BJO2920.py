from sys import stdin
input = stdin.readline

def check(arr):
    if arr == numbers:
        print('ascending')
    elif arr == numbers[::-1]:
        print('descending')
    else:
        print('mixed')

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    arr = list(map(int,input().split()))
    check(arr)
    
'''
 ascending, descending, mixed 중 하나를 출력
예제 입력 1 
1 2 3 4 5 6 7 8
예제 출력 1 
ascending
'''