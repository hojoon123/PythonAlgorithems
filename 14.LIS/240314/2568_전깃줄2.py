from sys import stdin
input = stdin.readline

def lower_bound(left, right, d, x):
    while left <= right:
        mid = (left + right) // 2
        if d[mid] >= x:
            right = mid - 1
        else:
            left = mid + 1
    return left

def main():
    n = int(input())
    graph = sorted([list(map(int,input().split())) for i in range(n)])
        
    d = [graph[0][1]]
    dp = [-1] * n
    for i in range(n):
        # 현재 값이 D의 마지막 값보다 큰 경우 - LIS 길이 증가
        if d[-1] < graph[i][1]:
            dp[i] = max(dp) + 1
            d.append(graph[i][1])
        else:
            # x = 현재 수 graph[i]가 만들 수 있는 최대 길이 - 1
            x = lower_bound(0,len(d) - 1, d, graph[i][1])
            if graph[i][1] > d[x]:
                d[-1] = graph[i][1]
            else:
                d[x] = graph[i][1]
                dp[i] = x + 1


    len_out_line = len(d)
    lis = []
    for i in range(n - 1, -1, -1):
        if len_out_line == 0:
            break
        if dp[i] == len_out_line:
            lis.append(graph[i])
            len_out_line -= 1
            
    # 실제 LIS가 아닌 원소들을 저장
    not_lis = []
    for i in graph:
        if i not in lis:
            not_lis.append(i)
        
    # 인덱스 순으로 배열 not_lis를 정렬
    not_lis.sort(key=lambda x : x[0])
    
    print(n - len(d))
    for i in range(n - len(d)):
        print(not_lis[i][0])


if __name__ == "__main__":
    main()