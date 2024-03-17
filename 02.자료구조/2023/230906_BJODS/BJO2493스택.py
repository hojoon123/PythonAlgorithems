from sys import stdin
input = stdin.readline

def check(len_top, top_list):
    stack = []
    receive_top_list = []
    
    for i in range(len_top):
        while stack:
            if stack[-1][1] > top_list[i]:  # 수신 가능한 상황
                receive_top_list.append(stack[-1][0] + 1)
                break
            else:
                stack.pop()
        if not stack:  # 스택이 비면 레이저를 수신할 탑이 없다.
            receive_top_list.append(0)
        stack.append([i, top_list[i]])  # 인덱스, 값
    return (" ".join(map(str, receive_top_list)))
                
if __name__ == '__main__':
    n = int(input())
    tops = list(map(int,input().split()))
    result = check(n, tops)
    print(result)


'''
예제 입력 1 
5
6 9 5 7 4
예제 출력 1 
0 0 2 2 4

'''