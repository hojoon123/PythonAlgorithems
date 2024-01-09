import sys
input = sys.stdin.readline

# (x,h) 튜플 형태 -> ans append 로직
def append_ans(ans, p):
    n = len(ans)
    if n > 0:
        # h값이 동일한 경우 추가 X
        if ans[n - 1][1] == p[1]:
            return
        # x값이 동일한 경우 더 h값이 큰 걸로 대체
        if ans[n - 1][0] == p[0]:
            
            ans[n - 1] = (p[0], p[1])
            # 만약 교체 후 그보다 이전의 h값과 동일하다면 스카이라인 변경이 없으므로 제거
            if n > 1 and ans[n - 2][1] == ans[n - 1][1]:
                ans.pop()
            return
    ans.append(p)

def merge(l, r):
    ans = []
    # 왼쪽 스카이라인의 현재 높이
    h1 = 0
    # 오른쪽 스카이라인의 현재 높이
    h2 = 0
    i = 0
    j = 0
    while i < len(l) and j < len(r):
        u = l[i]
        v = r[j]
        # 등호 처리 중요
        # 만약 u[0] == v[0]면, 정렬 우선순위상 v보다 u의 height가 작거나 right가 작다는 의미가 내포
        # 따라서 u가 먼저 append되는 것이 맞다.
        # 오른쪽 애가 x좌표 더 크거나 같니?
        if u[0] <= v[0]:
            x = u[0]
            h1 = u[1]
            h = max(h1, h2)
            append_ans(ans, (x, h))
            i += 1
        else:
            x = v[0]
            h2 = v[1]
            # 더 큰 높이로 선택
            # 만약 높이가 동일한 점이 있다면
            h = max(h1, h2)
            append_ans(ans, (x, h))
            j += 1

    while i < len(l):
        x = l[i][0]
        h1 = l[i][1]
        h = max(h1, h2)
        append_ans(ans, (x, h))
        i += 1

    while j < len(r):
        x = r[j][0]
        h2 = r[j][1]
        h = max(h1, h2)
        append_ans(ans, (x, h))
        j += 1

    return ans

def go(arr, start, end):
    # 분할
    if start == end:
        # 0번 인덱스 좌측위 기준 1번 인덱스 우측 기준, x축 끝이 기준이기에 y는 항상 0
        ans = [(arr[start][0], arr[start][1]), (arr[start][2], 0)]
        return ans

    mid = (start + end) // 2
    # left and right
    l = go(arr, start, mid)
    r = go(arr, mid + 1, end)

    # 병합
    return merge(l, r)

if __name__ == "__main__":
    n = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(n)]
    # left, height, right 순으로 오름차순 정렬
    # 시작 x 지점 -> 높이 -> 끝나는 x 지점
    arr.sort(key=lambda x: (x[0], x[1], x[2]))
    ans = go(arr, 0, n - 1)
    print(ans)
