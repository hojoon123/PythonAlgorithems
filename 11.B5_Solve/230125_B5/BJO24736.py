from sys import stdin
input = stdin.readline

def check(n, m, score):
    for i in range(5):
        n[i] = n[i] * score[i]
        m[i] = m[i] * score[i]
    print(sum(n), sum(m))
    
if __name__ == '__main__':
    n = list(map(int,input().split()))
    m = list(map(int,input().split()))
    score = [6, 3, 2, 1, 2]
    check(n, m, score)
        
    

'''
6 3 2 1 2
예제 입력 1 
1 3 0 0 1
3 1 1 1 1
예제 출력 1 
17 26

'''