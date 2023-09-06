from sys import stdin

input = stdin.readline


def dfs(depth, total, plus, minus, multiply, divide):
    global maxnum, minnum
    if depth == n:
        maxnum = max(total, maxnum)
        minnum = min(total, minnum)
        return

    if plus:
        dfs(depth + 1, total + nums[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - nums[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * nums[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / nums[depth]), plus, minus, multiply, divide - 1)


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    operator = list(map(int, input().split()))
    # oerator[0:4] 0 + 1 - 2 * 3 //
    maxnum = -1e9
    minnum = 1e9

    dfs(1, nums[0], operator[0], operator[1], operator[2], operator[3])
    print(maxnum)
    print(minnum)

'''
예제 입력 1 
2
5 6
1 1 1 1
예제 출력 1 
30
-1
'''