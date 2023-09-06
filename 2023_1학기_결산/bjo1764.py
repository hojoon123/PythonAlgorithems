import sys
input = sys.stdin.readline

n, m = map(int,input().split())
dut = set()
for i in range(n):
    dut.add(str(input().rstrip()))

bo = set()
for i in range(m):
    bo.add(str(input().rstrip()))

result = list(dut & bo)

print(len(result))
result.sort()
for nick in result:
    print(nick)