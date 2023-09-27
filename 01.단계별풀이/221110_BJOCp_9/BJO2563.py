n = int(input())
arr = [[0] * 101 for i in range(101)]
result = 0
for k in range(n):
    a, b = map(int,input().split())
    
    for i in range(a, a+10):
        for j in range(b, b+10):
            arr[i][j] = 1
for k in arr:
    result += k.count(1)
print(result)            
'''
색종이 10x10
도화지 100x100
첫 줄 색종이 수
둘째 줄부터 한 줄에 하나씩 색종이를 붙인 위치
공백으로 구분 두 개의 자연수로 주어짐
첫 수 왼쪽변과 도화지 왼쪽벽 사이의 거리
두 수 아래쪽변과 도화지 아래쪽벽 사이의 거리
예제 입력 1 
3
3 7
15 7
5 2
예제 출력 1 
260
'''