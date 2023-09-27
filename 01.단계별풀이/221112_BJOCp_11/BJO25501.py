import sys
input = sys.stdin.readline
def recursion(s, l, r):
    global cnt
    cnt +=1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)


for i in range(int(input())):
    cnt = 0
    a = input().rstrip()
    print(isPalindrome(a),cnt)

'''
isPalindrome 함수의 반환값과 recursion 함수의 호출 횟수를 한 줄에 공백으로 구분하여 출력
예제 입력 1 
5
AAA
ABBA
ABABA
ABCA
PALINDROME
예제 출력 1 
1 2
1 3
1 3
0 2
0 1
'''