import sys
input = sys.stdin.readline

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Divide
    pivot = arr[0]
    left = []
    right = []
    
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    
    # Conquer
    left_sorted = quick_sort(left)
    right_sorted = quick_sort(right)
    
    # Combine
    return left_sorted + [pivot] + right_sorted

if __name__ == "__main__":
    arr = [3,4,2,1,6,7,8,3,2]
    arr = quick_sort(arr)
    print(arr)