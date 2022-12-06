import sys
input = sys.stdin.readline

n = int(input())
a = []
for i in range(n):
    b = list(map(int,input().split()))
    a.append(b)
a.sort()
for i in range(len(a)):
    print(a[i][0], end = " ")
    print(a[i][1])

'''
좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬
점의 개수 N
둘째 줄 i번점의 위치 xi와 yi
(-100,000 ≤ xi, yi ≤ 100,000)
 항상 정수 위치가 같은 두 점은 없다
예제 입력 1 
5
3 4
1 1
1 -1
2 2
3 3
예제 출력 1 
1 -1
1 1
2 2
3 3
3 4
'''