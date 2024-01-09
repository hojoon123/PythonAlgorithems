import sys
input = sys.stdin.readline

def minimize(s):
    num = []
    
    for i in s:
        cur_num = 0
        n = i.split('+')
        for j in n:
            cur_num += int(j)
            
        num.append(cur_num)
        
    result = num[0] # 첫 수
    
    for i in range(1,len(num)):
        result -= num[i]
    return result
            
        

if __name__ == '__main__':
    s = input().split('-')
    print(minimize(s))


'''
예제 입력 1 
55-50+40
예제 출력 1 
-35
예제 입력 2 
10+20+30+40
예제 출력 2 
100
예제 입력 3 
00009-00009
예제 출력 3 
0
'''