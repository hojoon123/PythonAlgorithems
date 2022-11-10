n, m = map(int,input().split())

arr=[[0 for j in range(m)] for i in range(n)]
for k in range(2):
    for i in range(n):
        a = list(map(int,input().split()))
        for j in range(m):
                arr[i][j] += a[j]
                if k == 1:
                    print(arr[i][j], end=" ")
  

'''
첫 줄 행렬 M * N
둘부터 N개의 줄 M개의 원소 A 다 넣으면
다음줄 부터 N개의 줄 M개의 원소 B
A+B 출력
예제 입력 1 
3 3
1 1 1
2 2 2
0 1 0
3 3 3
4 4 4
5 5 100
예제 출력 1 
4 4 4
6 6 6
5 6 100
'''