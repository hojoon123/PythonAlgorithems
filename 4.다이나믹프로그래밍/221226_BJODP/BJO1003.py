from sys import stdin
input = stdin.readline

t = int(input())
arr = [0] * 41
arr[0] = [1, 0]; arr[1] = [0, 1]
for i in range(2, 41):
    arr[i] = [arr[i-1][1],sum(arr[i-1])]
for i in range(t):
    N = int(input())
    print(*arr[N])
    