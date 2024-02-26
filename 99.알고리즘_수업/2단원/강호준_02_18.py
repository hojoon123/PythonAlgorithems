from sys import stdin
input = stdin.readline

# n = 5 5부터 0까지 -1씩 재귀 / 매개변수 + 재귀값 --> 반환값
def sum(n):
    print(n)
    if n < 1:
        return 0
    else:
        return n + sum(n-1)

if __name__ == "__main__": # 메인문입니다.
    user_input = int(input())
    print(sum(user_input))
'''
sum(5)
5
4
3
2
1
0

반환값 : 15
'''    