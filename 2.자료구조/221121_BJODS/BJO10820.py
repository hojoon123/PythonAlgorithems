import sys


while 1:
    try:
        ans = [0] * 4
        s = list(input())
        for i in s:
            if 97 <= ord(i) <= 122: #소문자
                ans[0] += 1
                
            elif 65 <= ord(i) <= 90: #대문자
                ans[1] += 1
                
            elif ord(i) == 32: #공백
                ans[3] += 1
                
            else: #숫자
                ans[2] += 1
        print(*ans)
    except EOFError:
        break

''''
EOFError 입력값이 없을 때 뜨는 에러
소문자, 대문자, 숫자, 공백의 개수를 공백으로 구분해 출력
예제 입력 1 
This is String
SPACE    1    SPACE
 S a M p L e I n P u T     
0L1A2S3T4L5I6N7E8
예제 출력 1 
10 2 0 2
0 10 1 8
5 6 0 16
0 8 9 0
'''