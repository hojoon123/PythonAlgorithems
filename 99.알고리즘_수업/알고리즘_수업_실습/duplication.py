import sys
import time
input = sys.stdin.readline

# 중복 탐색
def duplication_Search(a):
    for cur_num in range(n):
        for next in range(cur_num + 1, n):
            if items[cur_num] == items[next]:
                return False # 있음
    return True # 없음

# 2진수 변환 비트 수 계산
def get_bit_num(n):
    cnt = 1
    while n > 1:
        cnt = cnt + 1
        n = n // 2
    return cnt

# 2진수 8진수 10진수 변환


if __name__ == "__main__":
    a, n = map(int,input().split())
    items = list(map(int,input().split()))
    
    start = time.time()
    print(duplication_Search(a))
    end = time.time()
    print(f"duplication 실행시간{end - start}")
    
    start = time.time()
    print(get_bit_num(n))
    end = time.time()
    print(f"get_bit_num 실행시간{end - start}")