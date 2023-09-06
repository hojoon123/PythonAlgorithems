import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    global visited
    q = deque()
    q.append((1,0))

    while q:
        now, clip = q.popleft()
        
        if now == s:
            print(visited[(now,clip)])
            break
        
        if (now,now) not in visited.keys():
            visited[(now,now)] = visited[(now,clip)] + 1
            q.append((now,now))
        
        if (now + clip,clip) not in visited.keys():
            visited[(now + clip,clip)] = visited[(now,clip)] + 1
            q.append((now + clip, clip))
        
        if (now - 1, clip) not in visited.keys():
            visited[(now - 1, clip)] = visited[(now,clip)] + 1
            q.append((now - 1, clip))   

if __name__ == '__main__':
    s = int(input())
    visited = dict()
    visited[(1,0)] = 0
    bfs()

'''
화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
화면에 있는 이모티콘 중 하나를 삭제한다.
첫째 줄에 S (2 ≤ S ≤ 1000)
이모티콘을 S개 만들기 위해 필요한 시간의 최솟값을 출력
예제 입력 1 
2
예제 출력 1 
2
예제 입력 2 
4
예제 출력 2 
4
'''