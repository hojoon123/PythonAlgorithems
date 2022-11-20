import sys
input = sys.stdin.readline

n = int(input())
cal = list(input().rstrip()) #후위표기식
stack = []; numbers = []
for i in range(n): numbers.append(float(input()))


for s in range(len(cal)):
    if cal[s].isalnum(): #알파벳일 때
        stack.append(numbers[ord(cal[s])-65]) #아스키코드를 활용함
    elif cal[s] == "+":
        stack.append(stack.pop(-2)+stack.pop())
    elif cal[s] == "-":
        stack.append(stack.pop(-2)-stack.pop())
    elif cal[s] == "*":
        stack.append(stack.pop(-2)*stack.pop())
    elif cal[s] == "/":
        stack.append(stack.pop(-2)/stack.pop())
        
print("{:.2f}".format(stack[0]))
'''
계산 결과를 소숫점 둘째 자리까지 출력
예제 입력 1 
5
ABC*+DE/-
1
2
3
4
5
예제 출력 1 
6.20
'''