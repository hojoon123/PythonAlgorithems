import sys
input = sys.stdin.readline
N = str(input().rstrip())
res = 0
if len(N) == 1:
    print(N)
    exit()
for i in range(len(N)):
    if i == len(N)-1:
        res += (int(N) - (10 ** i) + 1) * (i+1)
    else:
        res += 9 * (10 ** i) * (i+1)
print(res)


'''
5000
0 1 2 3
예제 입력 1 
5
예제 출력 1 
5
예제 입력 2 
15
예제 출력 2 
21
'''