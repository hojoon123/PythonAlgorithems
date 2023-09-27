from sys import stdin
from collections import deque
input = stdin.readline

def re_check(x):
    #메모리 절약한 코드 전부 넣을 필요 없이 하나씩 넣어서 역추적하면 엄청 절약 가능
    data = []
    tmp = x
    
    for i in range(cnt[x] + 1):
        data.append(tmp)
        tmp = arr[tmp]

    print(' '.join(map(str,data[::-1])))
        

def bfs(n):
    q = deque()
    q.append(n)
    
    while q:
        x = q.popleft()
        
        if x == k:
            print(cnt[x])
            re_check(x)
            return
        for nx in (x - 1, x + 1, 2 * x):
            if 0 <= nx <= max and not cnt[nx]:
                cnt[nx] = cnt[x] + 1
                q.append(nx)
                arr[nx] = x

if __name__ == '__main__':
    n, k = map(int,input().split())
    max = 10 ** 5
    cnt = [0] * (max + 1)
    arr = [0] * (max + 1)
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