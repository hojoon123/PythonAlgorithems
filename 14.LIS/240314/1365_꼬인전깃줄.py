from sys import stdin
input = stdin.readline

def binarySearch(e, lis):
    start = 0
    end = len(lis) - 1
    while start <= end:
        mid = (start + end) // 2
        
        if lis[mid] == e:
            return mid
        elif lis[mid] > e:
            start = mid + 1
        else:
            end = mid - 1
            
    return start

def main():
    n = int(input())
    graph = list(map(int,input().split()))
    
    lis = [graph[0]] # 수열
    dp = [(0, graph[0])] # idx, 값
    
    #
    for i in range(1, n):
        if graph[i] > lis[-1]:
            lis.append(graph[i])
            dp.append((len(lis) - 1, graph[i]))
        else:
            idx = binarySearch(graph[i], lis)
            lis[idx] = graph[i]
            dp.append((idx, graph[i]))
            
    print(n - len(lis))
    


if __name__ == "__main__":
    main()