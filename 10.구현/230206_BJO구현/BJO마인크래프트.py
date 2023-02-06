import sys
from collections import Counter
input = sys.stdin.readline

if __name__ == '__main__':
    n, m, b = map(int,input().split())
    ground = []
    for i in range(n):
        ground += map(int, input().split())
    height, time = 0, 10 ** 9
    
    min_h = min(ground)
    max_h = max(ground)
    _sum = sum(ground)
    ground = dict(Counter(ground))
    
    for i in range(min_h, max_h + 1):
        if _sum + b >= i * n * m:
            cur_time = 0
            for key in ground:
                if key > i:
                    cur_time += (key - i) * ground[key] * 2
                elif key < i:
                    cur_time += (i - key) * ground[key]
                    
            if cur_time <= time:
                time = cur_time
                height = i
    print(time, height)
'''
제일 개수 많은 거 체크하고 dist를 만들어서 차이값 넣기
dist가 +면 2초 + (b + 1) - 면 1초 + (b - 1)
첨에 가장 많은 것의 len 때리고 하다가 b가 부족하다면
전체적으로 1개씩 줄이고 다시 하기

좌표 (i, j)의 가장 위에 있는 블록을 제거하여 인벤토리에 넣는다. 2초
인벤토리에서 블록 하나를 꺼내어 좌표 (i, j)의 가장 위에 있는 블록 위에 놓는다. 1초
예제 입력 1 
3 4 99
0 0 0 0
0 0 0 0
0 0 0 1
예제 출력 1 
2 0


예제 입력 2 
3 4 1
64 64 64 64
64 64 64 64
64 64 64 63
예제 출력 2 
1 64
'''