import sys


n = list(str(input()))
for i in range(len(n)):
    n[i] = int(n[i])
n.sort(reverse=True)
for j in n:
    print(j,end="")
    

'''
N이 주어진다. N은 1,000,000,000
내림차순으로 정렬한 수를 출력
예제 입력 1 
2143
예제 출력 1 
4321
'''