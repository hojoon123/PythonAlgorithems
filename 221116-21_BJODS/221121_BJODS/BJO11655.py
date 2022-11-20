import sys
input = sys.stdin.readline

s = list(input().rstrip())
ans = []
while s:
    if s[0].isalpha(): 
        if ord(s[0]) >= 97: #소문자
            tmp = ord(s.pop(0))+13
            if tmp > 122:
                tmp -= 26
            ans.append(chr(tmp))
        else: #대문자
            tmp = ord(s.pop(0))+13
            if tmp > 90:
                tmp -= 26
            ans.append(chr(tmp))
        
    else:# 공백 숫자
        ans.append(s.pop(0))
print(''.join(ans))
'''
소문자 97 122
대문자 65 90
공백 32
숫자 48 57
첫째 줄에 알파벳 대문자, 소문자, 공백, 숫자로만 이루어진 문자열 S
예제 입력 1 
Baekjoon Online Judge
예제 출력 1 
Onrxwbba Bayvar Whqtr
'''