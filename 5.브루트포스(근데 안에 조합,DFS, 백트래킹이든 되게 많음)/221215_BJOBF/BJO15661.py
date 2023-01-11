import sys
from itertools import combinations
input = sys.stdin.readline
 
N = int(input())
 
 
arr = [list(map(int,input().split())) for _ in range(N)]
row = [sum(i) for i in arr]
col = [sum(i) for i in zip(*arr)]
new_arr = [i+ j for i, j in zip(row, col)]
total_sum = sum(new_arr)//2
result = float('inf')
for num in range(1,N//2+1):
    for combi in combinations(new_arr,num):
        result = min(result,abs(total_sum-sum(combi)))
        if result == 0:
            print(result)
            exit()
print(result)
                
'''
1 2 1 3 1 4
1 2 
돌면서 i가 같을 때 제외 
arr[i][j] + arr[j][i]
N(4 ≤ N ≤ 20, N은 짝수)
예제 입력 1 
4
0 1 2 3
4 0 5 6
7 1 0 2
3 4 5 0
예제 출력 1 
0
'''