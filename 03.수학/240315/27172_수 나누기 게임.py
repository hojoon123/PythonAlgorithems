import sys
input = sys.stdin.readline

def solve(n, graph, max_n, score):
    for i in range(n):
        idx, num = graph[i]
        
        for target in range(num * 2, max_n + 1, num):
            if target in score:
                score[num] += 1
                score[target] -= 1
    return score

def main():
    n = int(input())
    graph = []
    max_n = 0
    score = {}
    for idx, num in enumerate([*map(int,input().split())]):
        max_n = max(max_n, num)
        graph.append((idx,num))
        score[num] = 0
    graph.sort(key=lambda x:x[1])
    
    score = solve(n, graph, max_n, score)
    
    for i in score:
        print(score[i], end=" ")
    
if __name__ == "__main__":
    main()