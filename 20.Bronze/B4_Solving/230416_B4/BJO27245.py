import sys
input = sys.stdin.readline

def check(n, l, h):
    if n > l:
        tmp = l
        tmp2 = n
    else:
        tmp = n
        tmp2 = l
        
    if tmp // h >= 2:
        pass
    else:
        print('bad')
        return
    if tmp // tmp2 >= 2:
        print('bad')
        return
    print('good')
    return
    
if __name__ == '__main__':
    n = int(input())
    l = int(input())
    h = int(input())
    check(n, l, h)
        
    

'''
w/ h >= 2
l/ h >= 2
w / l < 2
가로와 세로 중 더 짧은 쪽의 길이와 높이의 비는 2 이상이어야 합니다.
가로와 세로 중 더 긴 쪽의 길이와 짧은 쪽의 길이의 비는 2를 초과하면 안 됩니다.
A와 B의 비는 A/B를 의미합니다.
방의 가로 길이, 세로 길이, 높이를 의미하는 3개의 정수 w, l, h가 한 줄에 하나씩 주어집니다.
예제 입력 1 
4000
6000
3000
예제 출력 1 
bad
'''