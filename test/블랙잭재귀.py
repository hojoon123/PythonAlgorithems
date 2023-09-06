import sys
from itertools import combinations
input = sys.stdin.readline

def dfs(depth,tmp):
    global cnt
    cnt += 1
    rr = int(input())
    print(f"{cnt}번 dfs 함수를 실행하였습니다!")
    print(f"현재 방문 체크는 {visited} 상태입니다.")
    global result
    if depth == 3:
        if tmp <= n:
            result.append(tmp)
            print("3가지 수를 뽑았습니다!")
            print(f"저장한 값은 {tmp}입니다.")
        return
    for i in range(m):
        print(f'{cnt}번 dfs 함수입니다. for문은 {m}번 반복할건데, 현재 인덱스는 {i}, 저장한 값은 {tmp}입니다.')
        if visited[i] == 0:
            visited[i] = 1
            dfs(depth+1,tmp+arr[i])
            visited[i] = 0

if __name__ == "__main__":
    result = []
    m , n = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort()
    visited = [0] * m
    cnt = 0
    dfs(0, 0)
    print(max(result))

'''
입력 값을 받고 우리는 5장 중에서 3장을 뽑아서 21이 넘는지 안 넘는지 체크함.
체크하고 21보다 작거나 같으면 그 수를 리스트에 저장해서 리스트 중에서 가장 큰 수만 출력하면 됨.

'''