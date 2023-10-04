import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 2 ** (n + 1) - 1
def sub(n):
    return 2 ** (n+1) - 1
    
if __name__ == "__main__": # 메인문입니다.
    user_input = int(input())
    print(sub(user_input))
'''
sub(3)과 같이 호출할 때 sub가 호출되는 전체 횟수 구하기
2 ** (n + 1) - 1
'''    