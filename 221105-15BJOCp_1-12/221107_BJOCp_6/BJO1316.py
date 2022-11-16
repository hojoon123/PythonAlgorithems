a = int(input())
cnt = a
for i in range(a):
    b = input()
    for j in range(len(b)-1):
        if b[j] == b[j+1]:
            pass
        elif b[j] in b[j+1:]:
            cnt-=1
            break
print(cnt)
'''
소문자
예제 입력 1 
3
happy
new
year
예제 출력 1 
3
'''