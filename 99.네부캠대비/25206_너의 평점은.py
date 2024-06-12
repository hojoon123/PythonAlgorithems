import sys
from collections import deque
input = sys.stdin.readline

def magic():
    pass
    
def main():
    score = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5,
             "D0":1.0,"F":0.0}
    sum_s = 0
    tmp = 0
    for i in range(20):
        n, a, s = map(str,input().split())
        if s == "P":
            continue
        sum_s += float(a) * score[s]
        tmp += float(a)
    ans = sum_s / tmp
    print(ans)
if __name__ == "__main__":
    main()
    