import sys

a = int(input())
for i in range(a):
    b =list(map(int,sys.stdin.readline().split()))
    print("Case #%d: %d + %d = %d" %((i+1),b[0],b[1],sum(b)))