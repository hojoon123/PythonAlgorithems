a, b = map(int, input().split())
p = list(map(int, input().split()))
c = a * b
for i in p:
    print(i - c, end=' ')