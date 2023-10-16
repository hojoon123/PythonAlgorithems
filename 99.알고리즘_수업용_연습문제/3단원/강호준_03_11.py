import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# A가 늘수록 오래걸림
def bf_ab(s):
    cnt = 0
    for start in range(len(s)):
        if s[start] == 'A':
            for end in s[start + 1:]:
                if end == 'B':
                    cnt += 1
    else:
        return cnt
    
# O(n)
def custom_ab(s):
    cnt = 0
    add_num = 0
    for current in s:
        if current == 'A':
            add_num += 1
        elif current == 'B':
            cnt += add_num
    else:
        return cnt
    
if __name__ == "__main__": # 메인문입니다.
    user_input = str(input().rstrip())
    print(bf_ab(user_input))
    print(custom_ab(user_input))
