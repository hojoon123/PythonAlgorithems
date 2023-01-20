from sys import stdin
from collections import deque
input = stdin.readline
#메모리 초과로 실패한 코드 생각해보니 메모리를 엄청나게 많이 쳐먹을 것 같다
def bfs(n):
    q = deque()
    q.append(n)
    cnt[n].append(n)
    
    while q:
        x = q.popleft()
        
        if x == k:
            print(len(cnt[x]) - 1)
            print(*cnt[x])
            return
        for nx in (x - 1, x + 1, 2 * x):
            if 0 <= nx <= max and not cnt[nx]:
                cnt[nx].extend(cnt[x])
                cnt[nx].append(nx)
                q.append(nx)

if __name__ == '__main__':
    n, k = map(int,input().split())
    max = 10 ** 5
    cnt = [[] for i in range(max + 1)]
    bfs(n)
'''
1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동
첫째 줄에 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.
둘째 줄에 어떻게 이동해야 하는지 공백으로 구분해 출력한다.
예제 입력 1 
5 17
예제 출력 1 
4
5 10 9 18 17
예제 입력 2 
5 17
예제 출력 2 
4
5 4 8 16 17
'''