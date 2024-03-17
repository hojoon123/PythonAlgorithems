import sys
from collections import deque
input = sys.stdin.readline

def del_node(num, arr):
    arr[num] = -2
    for i in range(len(arr)):
        if num == arr[i]:
            del_node(i, arr)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())

    del_node(k, arr)
    
    cnt = 0
    for i in range(len(arr)):
        if arr[i] != -2 and i not in arr:
            cnt += 1
    print(cnt)