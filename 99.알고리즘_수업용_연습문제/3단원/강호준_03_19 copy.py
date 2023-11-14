import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 재귀 구현
# 억지기법을 위한 순서가 있는 모든 순열 전부 찾아서 검사하기
def perm(arr):
    global result
    if len(arr) == 2:
        print(arr)
        return

    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            perm(arr+[i + 1])
            visited[i] = 0

if __name__ == "__main__": # 메인문입니다.
    result = 10**5
    n = int(input()) # n명 n가지 일
    visited = [0 for i in range(n)] # 방문 여부 체크
    arr = []
    perm(arr)

    
    