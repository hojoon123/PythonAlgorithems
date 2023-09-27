from sys import stdin
input = stdin.readline

def reverse(str_list):
    stack = []
    reverse_result = ''
    for item in str_list:
        stack.append(item)
    while stack:
        reverse_result += stack.pop()
    
    return reverse_result

if __name__ == "__main__": # 메인문입니다.
    user_input = input().rstrip()
    print(reverse(user_input))
'''
문자열 역순 출력
'''    