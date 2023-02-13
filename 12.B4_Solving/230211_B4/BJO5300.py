import sys
input = sys.stdin.readline

def check(n):
    arr =  []
    for i in range(1, n + 1):
        arr.append(str(i))
        if int(i) % 6 == 0:
            arr.append('Go!')
    if arr[-1] != 'Go!':
        arr.append('Go!')
    
    print(*arr)
if __name__ == '__main__':
    n = int(input())
    check(n)
    

'''
예제 입력 1 
10
예제 출력 1 
1 2 3 4 5 6 Go! 7 8 9 10 Go!
예제 입력 2 
18
예제 출력 2 
1 2 3 4 5 6 Go! 7 8 9 10 11 12 Go! 13 14 15 16 17
'''