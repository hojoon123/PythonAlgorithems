import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# O(n)
def str_match(t, p):
    lt = len(t)
    lp = len(p)
    for start in range(lt - lp + 1):
        cur = 0
        while cur < lp and p[cur] == t[start + cur]:
            cur = cur + 1
        if cur == lp:
            return start
    return -1
    
if __name__ == "__main__": # 메인문입니다.
    txt = str(input().rstrip())
    patton = str(input().rstrip())
    
    print(str_match(txt, patton))