import sys
input = sys.stdin.readline

s = list(input().rstrip())
i = 0
start = 0

while i < len(s):
    if s[i] =='<':
        while s[i] != '>':
            i += 1
        i += 1
        
    elif s[i].isalnum():
        start = i
        while i < len(s) and s[i].isalnum():
            i += 1
        tmp = s[start : i]
        tmp.reverse()
        s[start : i] = tmp
    else:
        i += 1
print(''.join(s))

'''
<> 안의 문자열은 뒤집히지 않음 
첫째 줄에 문자열 S가 주어진다. S의 길이는 100,000 이하
첫째 줄에 문자열 S의 단어를 뒤집어서 출력
예제 입력 1 
baekjoon online judge
예제 출력 1 
noojkeab enilno egduj
<open>tag<close>
예제 출력 2 
<open>gat<close>
'''