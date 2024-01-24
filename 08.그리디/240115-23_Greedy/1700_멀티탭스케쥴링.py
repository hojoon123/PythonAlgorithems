import sys
import heapq
input = sys.stdin.readline

def solve(n, k, seq):
    plug = set()
    cnt = 0
    if n >= k:
        return 0
    
    for idx, num in enumerate(seq):
        plug.add(num)
        if len(plug) > n:
            cnt += 1
            latest_used = find_latest(idx, plug, seq, k)
            plug.discard(latest_used)
            
    return cnt

# 마지막에 나오는 애 찾아서 퇴출
def find_latest(idx, plug, seq, k):
    result = 0
    max_idx = -1
    for num in plug:
        try:
            num_idx = seq[idx:].index(num)
        except:
            num_idx = k
        if max_idx < num_idx:
            result, max_idx = num, num_idx

    return result


def main():
    n, k = map(int,input().split())
    use_seq = list(map(int,input().split()))
    print(solve(n, k, use_seq))
    
if __name__ == "__main__":
    main()
