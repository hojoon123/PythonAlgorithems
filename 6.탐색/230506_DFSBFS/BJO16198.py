import sys
input = sys.stdin.readline


def back(cur_ans):
    global ans
    if len(arr) ==2:
        ans = max(ans, cur_ans)
        return
    for i in range(1, len(arr)-1):
        tmp = arr[i -1] * arr[i + 1]
        elm = arr.pop(i)
        back(cur_ans + tmp)
        arr.insert(i, elm)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int,input().split()))
    ans = 0
    back(0)
    print(ans)



'''
예제 입력 1 
4
1 2 3 4
예제 출력 1 
12  
예제 입력 2 
5
100 2 1 3 100
예제 출력 2 
10400
'''