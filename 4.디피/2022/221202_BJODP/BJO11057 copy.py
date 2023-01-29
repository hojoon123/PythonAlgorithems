import sys
input = sys.stdin.readline

n = int(input())
num = [1]*10

for i in range(n-1):
    for j in range(1, 10):
        num[j] += num[j-1]

print(sum(num)%10007)

#for i in range(N+1):
    

'''
1 ≤ N ≤ 1,000
10007로 나눈 나머지를 출력
예제 입력 1 
1
2
3
예제 출력 1 
10
55
220
'''