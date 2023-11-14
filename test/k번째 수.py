

def partition(numbers, left, right):
    low = left + 1
    high = right
    pivot = numbers[left]
    
    while low <= high:
        while numbers[low] < pivot and low <= right: low += 1
        while numbers[high] > pivot and high >= left: high -= 1
        
        if low < high:
            numbers[low], numbers[high] = numbers[high], numbers[low]
    
    numbers[left], numbers[high] = numbers[high], numbers[left]
    return high

def quick_select(numbers, left, right, k):
    pos = partition(numbers, left, right)
    
    if pos + 1 == left + k:
        return numbers[pos]
    
    elif pos + 1 < left + k: # 오른쪽에서 찾아야댐
        return quick_select(numbers, pos + 1, right, k - (pos + 1 - left))
    else: # 왼쪽
        return quick_select(numbers, left, pos - 1, k)

if __name__ == "__main__":
    numbers = [5, 3, 8, 4, 9, 1, 6, 2, 7]
    target = 3
    print(quick_select(numbers, 0, len(numbers)-1, target))
    