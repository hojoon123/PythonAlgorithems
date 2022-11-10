import sys

a = int(input())
for i in range(a):
    b =list(map(int,sys.stdin.readline().split()))
    print(sum(b))