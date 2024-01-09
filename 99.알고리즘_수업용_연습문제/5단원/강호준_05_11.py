import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

#분할
def quick_sort(arr, left, right):
    if left < right:
        mid = partition(arr, left, right)
        quick_sort(arr, left, mid - 1)
        quick_sort(arr, mid + 1, right)

# 파티션 알고리즘
def partition(arr, left, right):
    low = left + 1
    high = right
    pivot = arr[left]
    while low <= high:
        while low <= right and arr[low] < pivot : low += 1
        while high >= left and arr[high] > pivot : high -= 1
        
        if low < high:
            arr[low], arr[high] = arr[high], arr[low]
        
        if low == high:
            break
        
        print("QuickSorting : ", arr)
            
    arr[left], arr[high] = arr[high], arr[left]
    return high
        
if __name__ == "__main__": # 메인문입니다.
    user_list = [71, 49, 92, 55, 38, 82, 72, 53]
    print("Original:", user_list)
    quick_sort(user_list, 0, len(user_list)-1)
    print("QuickSort:", user_list)
    
