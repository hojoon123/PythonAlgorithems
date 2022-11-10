a = int(input())
line = 1
while a > line:
    a -= line
    line += 1
if line % 2 == 0:
    b = a
    c = line - a + 1
else:
    b = line - a + 1
    c = a
print(b,'/',c, sep='')

'''
짝수 라인 분자- 분모+
홀수 라인 분모- 분자+
예제 입력 1 
1
예제 출력 1 
1/1
'''