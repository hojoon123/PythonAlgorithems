import sys
input = sys.stdin.readline

n = int(input())
left, right = 0,n
while True:
    mid = (left + right) // 2
    
    if left > right:
        print(left)
        break
    elif mid ** 2 >= n:
        right = mid - 1
    else: left = mid + 1