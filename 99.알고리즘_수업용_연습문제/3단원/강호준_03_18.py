import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 재귀 구현
# 억지기법을 위한 모든 조합 전부 찾아서 검사하기
def comb(w, idx, visited, cur_w, cur_v):
    global result

    if cur_w <= w:
        if result < cur_v:
            result = cur_v

    for i in range(idx, n):
        if visited[i] == 0:
            visited[i] = 1
            comb(w, i, visited, cur_w + items[i][0], cur_v + items[i][1])
            visited[i] = 0
            
if __name__ == "__main__": # 메인문입니다.
    result = 0
    w, n = map(int,input().split()) # 배낭 무게 # 아이템 수
    items = [list(map(int,input().split())) for i in range(n)] # 아이템 리스트 (wt, val)
    visited = [0 for i in range(n)] # 방문 여부
    comb(w, 0, visited, 0, 0)
    print(result)
    
    
