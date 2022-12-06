import sys
input = sys.stdin.readline

s = list(map(str,input().rstrip()))
cs = len(s)

for _ in range(int(input())):
    a = list(input().split())
    order = a[0]
    
    if order == 'L':
        if cs > 0:
            cs -= 1
    elif order == 'D':
        if cs < len(s):
            cs += 1
    elif order == 'B':
        if cs > 0:
            s.remove(s[cs-1])
    elif order == 'P':
        s.insert(cs,a[1])
        cs += 1

print(''.join(s))
'''
L	커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
D	커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
B	커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 
문자는 그대로임
P $	$라는 문자를 커서 왼쪽에 추가함
초기에 편집기에 입력되어 있는 문자열 len(문자열) < 100,000
명령어의 개수를 나타내는 정수 M(1 ≤ M ≤ 500,000)
단, 명령어가 수행되기 전에 커서는 문장의 맨 뒤에 위치
첫째 줄에 모든 명령어를 수행하고 난 후 편집기에 입력되어 있는 문자열을 출력
예제 입력 1 
abcd
3
P x
L
P y
예제 출력 1 
abcdyx
'''