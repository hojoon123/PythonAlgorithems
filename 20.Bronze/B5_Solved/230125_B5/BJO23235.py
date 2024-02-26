from sys import stdin
input = stdin.readline

def check(cnt):
    for i in range(1, cnt + 1):
        print("Case {0}: Sorting... done!".format(i))
    
if __name__ == '__main__':
    cnt = 0
    while 1:
        n = list(map(int,input().split()))
        if n[0] == 0:
            break
        cnt += 1
    check(cnt)
        
    
    
'''
예제 입력 1 
5 21 44 48 48 64
6 8 19 22 49 53 62
8 5 9 14 17 24 25 27 61
4 13 21 28 35
5 31 38 44 49 60
0
예제 출력 1 
Case 1: Sorting... done!
Case 2: Sorting... done!
Case 3: Sorting... done!
Case 4: Sorting... done!
Case 5: Sorting... done!
'''