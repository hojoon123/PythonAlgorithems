import sys
input = sys.stdin.readline

s = list(input().split())
answer = 0
st = []

for i in range(len(s)):
    if s[i] == '(':
        st.append('(')

    else:
        if s[i-1] == '(': #레이저니?
            st.pop()
            answer += len(st)

        else:
            st.pop() 
            answer += 1 

print(answer)
'''
내가 짠 코드보다 3억배 정도 좋음..
(((()(()()))(())()))(()())
예제 출력 2 
24
예제 입력 1 
()(((()())(())()))(())
예제 출력 1 
17
'''