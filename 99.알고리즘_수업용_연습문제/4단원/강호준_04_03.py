import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 삽입 정렬
def insertion_sort(arr):
    print(f"초기 리스트 : {arr}")
    print()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f"{i}번째 시도 : {arr}")
    else:
        print()
        print(f"정렬된 리스트 : {arr}")
    return arr
        
if __name__ == "__main__": # 메인문입니다.
    user_list = [7, 4, 9, 6, 3, 8, 7, 5]
    insertion_sort(user_list)
    
