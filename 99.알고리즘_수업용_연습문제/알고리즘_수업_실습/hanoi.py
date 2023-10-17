import sys
import matplotlib.pyplot as plt
import time
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


# 하노이 탑 구현
def hanoi_tower(n, fr, tmp, to):
    if n == 1:
        #print(f"원판 1: {fr} --> {to}")
        res = 0

    else:
        hanoi_tower(n - 1, fr, to, tmp)
        #print(f"원판 {n}: {fr} --> {to} ")
        hanoi_tower(n - 1, tmp, fr, to)
        
if __name__ == "__main__":
    n = int(input())
    fr, tmp, to = 'A', 'B', 'C'
    
    for i in range(1,n + 1):
        start = time.time()
        hanoi_tower(n, fr, tmp, to)
        end = time.time()
        print(f"hanoi_tower 실행시간{end - start}")
    plt.plot([i for i in range(1, n + 1)], )