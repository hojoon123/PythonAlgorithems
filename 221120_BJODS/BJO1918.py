import sys
input = sys.stdin.readline

cal = list(input().rstrip())
tmp , tmp2, stack = [], [], []

while cal:
    if cal[0].isalnum(): #알파벳일 때
        stack.append(cal.pop(0))
        while tmp:
            stack.append(tmp.pop())
    elif cal[0] == '(': # 괄호를 만나면 다음 괄호까지 따로 계산함 일반적으로 괄호 안에 + - 만
        cal.pop(0)      # 보통 넣으니까 일단 두개만 생각하고 넣어봄
        while cal[0] != ')':
            if cal[0].isalnum(): #알파벳일 때
                stack.append(cal.pop(0))
                while tmp2:
                    stack.append(tmp2.pop())
                    
            elif cal[0] == "+":
                tmp2.append(cal.pop(0))
            elif cal[0] == "-":
                tmp2.append(cal.pop(0))
                
        else:
            while tmp:
                stack.append(tmp.pop())
            cal.pop(0)
    
    
    elif cal[0] == "+":
        tmp.append(cal.pop(0))
    elif cal[0] == "-":
        tmp.append(cal.pop(0))
    elif cal[0] == "*":
        while stack[-1].isalnum() == False: #소문자가 아닐 때
            tmp.append(stack.pop())
        tmp.append(cal.pop(0))
    elif cal[0] == "/":
        while stack[-1].isalnum() == False: #소문자가 아닐 때
            tmp.append(stack.pop())
        tmp.append(cal.pop(0))
print(''.join(stack))
'''
예제 문제는 다 맞췄는데, 시간초과가 떠버림. 근데 코드보면 ㅋㅋ 시간초과 안 나올수가 없긴하네
아 항흐날ㅇ느랑날ㅇ느ㅏ라ㅡ아른아르낭ㄹ 3시간 걸렸는데 아ㅡㄹ알아르알 진짜 힘들당
빠이팅 빠이팅 알고리즘 마스터 가즈아
첫 골드2 문제 일단 시간초과지만 할 수 있다는 것 자체에 의의를 두고 기쁜 마음으로
남의 코드를 확인하자!
ABC+*
표기식은 알파벳 대문자와 +, -, *, /, (, )
예제 입력 1 
A*(B+C)
예제 출력 1 
ABC+*
'''