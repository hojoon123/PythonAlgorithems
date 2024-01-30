n = int(input())
# 4
# 14
# 30
# 4
# 4 + 10
# 4 + 10 + 16
# 4 + 10 + 16 + 22
#이전 값 + 6
# 4 + 6
# 10 + 6
# 16 + 6
# 52
# 4
start = 4
graph = [0] * (n + 1)
graph[1] = 4
for i in range(2, n + 1):
    # graph[i] = graph[i - 1] + (graph[i - 1] + 6)
    graph[i] = graph[i - 1] + 6

print(sum(graph) + (2 * n + 1) ** 2)

