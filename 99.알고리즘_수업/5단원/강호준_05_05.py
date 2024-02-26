import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

#분할
def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        print(f'Merge Sorting_pre: {arr[left:right+1]}')
        merge(arr, left, mid, right)
        print(f'Merge Sorting_post: {arr[left:right+1]}')

# 정복 및 병합
def merge(arr, left, mid, right):
    k = left
    i = left
    j = mid + 1
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            sorted_list[k] = arr[i]
            i,k = i + 1, k + 1
        
        else:
            sorted_list[k] = arr[j]
            j, k = j + 1, k + 1
    
    if i > mid:
        sorted_list[k: k + right - j + 1] = arr[j: right + 1]
    else:
        sorted_list[k : k + mid - i + 1] = arr[i : mid + 1]
    
    arr[left:right+1] = sorted_list[left:right+1]
        
if __name__ == "__main__": # 메인문입니다.
    user_list = ['A', 'L', 'G', 'O', 'R', 'I', 'T', 'H', 'M']
    sorted_list = [0] * len(user_list)
    print("Original:", user_list)
    merge_sort(user_list, 0, len(user_list)-1)
    print("MergeSort:", user_list)
    
