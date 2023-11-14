import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 파티션 알고리즘
def partition(A, left, right):
    low = left + 1
    high = right
    pivot = A[left]
    while low <= high:
        while low <= right and A[low] < pivot : low += 1
        while high >= left and A[high] > pivot : high -= 1
        
        if low < high:
            A[low], A[high] = A[high], A[low]
            
    A[left], A[high] = A[high], A[left]
    return high

# 퀵정렬
def quick_select(A, left, right, k):
    pos = partition(A, left, right)
    
    if (pos + 1 == left + k):
        return A[pos]
    elif (pos + 1 > left + k):
        return quick_select(A, left, pos - 1, k)
    else:
        return quick_select(A, pos + 1, right, k - (pos + 1 - left))
            
if __name__ == "__main__": # 메인문입니다.
    A = [12, 5, 7, 9, 18, 3, 8]
    n = len(A)
    print(f"중앙값: {quick_select(A, 0, n - 1, 4)}")