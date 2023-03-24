from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    input()
    a = 0
    for i in [*sorted(map(int,input().split()))]:
        if a+1 < i:
            break
        a+=i
    print(a+1)
    


'''
합으로 만들 수 없는 가장 작은 수
예제 입력 1 
3
5 1 2
예제 출력 1 
4
'''