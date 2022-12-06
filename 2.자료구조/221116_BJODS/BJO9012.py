import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    a = list(map(str,input().rstrip()))
    stack = []
    if len(a) % 2 == 0:# 먼저 짝수가 아니면 끝내고 시작이 (이 아니면 끝냄 시간 차이는 약 6% 
        if a[0] == '(':# 확실히 시간 절약을 하기 위해서라면 필요한 4줄이지만, 가독성이 많이 안좋아짐
            for j in a:
                if j =='(':
                    stack.append(j)
                else:
                    if stack:
                        stack.pop()
                    else:
                        print("NO")
                        break
            else:
                if not stack:
                    print("YES")
                else:
                    print("NO")
        else:
            print("NO")
    else:
        print("NO")

'''
if a[i] == a[i+1]
    a.remove(a[0])
    a.remove(a[-1])
else:
    if a
    a.remove(a[0])
    a.remove(a[1])
 입력 T
 괄호 문자열이 한 줄
 괄호 문자열의 길이는 2 이상 50 이하
 출력
 입력 괄호 문자열이 올바른 괄호 문자열(VPS)이면 “YES”, 아니면 “NO”
예제 입력 1 
6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(
예제 출력 1 
NO
NO
YES
NO
YES
NO
'''