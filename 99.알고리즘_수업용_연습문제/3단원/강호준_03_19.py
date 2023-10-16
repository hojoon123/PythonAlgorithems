import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 재귀 구현
# 억지기법을 위한 순서가 있는 모든 순열 전부 찾아서 검사하기
def perm(arr):
    global result
    if len(arr) == n:
        cur_v = 0
        for i in range(len(arr)):
            cur_v += items[i][arr[i]]

        if result > cur_v:
            result = cur_v
        return

    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            perm(arr+[i])
            visited[i] = 0

if __name__ == "__main__": # 메인문입니다.
    result = 10**5
    n = int(input()) # n명 n가지 일
    items = [list(map(int,input().split())) for i in range(n)] # 아이템 리스트 2차원 리스트의 인덱스 = 사람 1차원 리스트 값 사람의 일 당 비용
    visited = [0 for i in range(n)] # 방문 여부 체크
    arr = []
    perm(arr)
    print(result)
    
    
