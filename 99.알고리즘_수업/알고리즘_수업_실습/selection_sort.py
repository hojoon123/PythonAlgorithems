import sys
input = sys.stdin.readline

def selection_sort(user_list):
    len_list = len(user_list)
    
    for i in range(len_list - 1):
        least_idx = i
        for j in range(i + 1, len_list):
            if user_list[j] < user_list[least_idx]:
                least_idx = j
        else:
            user_list[i], user_list[least_idx] = user_list[least_idx], user_list[i]
    
    return user_list
    
if __name__ == "__main__": # 메인문입니다.
    user_input_list = list(map(int,input().split()))
    print(selection_sort(user_input_list))

'''
선택정렬 하기
'''