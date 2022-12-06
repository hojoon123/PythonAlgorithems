import sys
input = sys.stdin.readline

n = int(input())
a = []
for i in range(n):
    b = list(map(int,input().split()))
    a.append(b)
a.sort(key = lambda x : (x[1],x[0]))
for x,y in a:
    print(x,y) 

'''
표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬
점의 개수 N
둘째 줄 i번점의 위치 xi와 yi
(-100,000 ≤ xi, yi ≤ 100,000)
 항상 정수 위치가 같은 두 점은 없다
예제 입력 1 
5
0 4
1 2
1 -1
2 2
3 3
예제 출력 1 
1 -1
1 2
2 2
3 3
0 4
'''