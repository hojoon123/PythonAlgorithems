import sys

input = sys.stdin.readline

# 입력받은 거 '점수 + 보너스 + 옵션' 형태로 넣어서 3번 던진 거 하나씩 넣음음
def splitScore():
    DT = [tmp[0],'','']
    num_li = '0123456789'
    idx = 0
    for i in range(1, len(tmp)):
        if tmp[i] in num_li:
            if tmp[i-1] != '1':
                idx += 1
        DT[idx] += tmp[i]
    return DT

# 계산함
def calScore(dividedDT):
    point = []
    idx = 0
    options = '*#'
    
    for i in dividedDT:
        if i[1] != '0':
            point.append(int(i[0]))
            
        else:
            point.append(10)
        
    for score in dividedDT:
        if score[1] == 'D':
            point[idx] = point[idx] ** 2
        elif score[1] == 'T':
            point[idx] = point[idx] ** 3  
            
        if score[-1] in options:
            if score[-1] == '*':
                if idx != 0:
                    point[idx - 1] *= 2
                    point[idx] *= 2
                else:
                    point[idx] *= 2
                    
            else:
                point[idx] = -point[idx]
        
        idx += 1
    print(dividedDT)
    print(point)
    return sum(point)
if __name__ == "__main__":
    tmp = list(map(str,input().rstrip()))
    dividedDT = splitScore()
    print(calScore(dividedDT))
    
'''
score / bonus / option 문자열형태
ex) 1S 2D* 3T

0 <= score <= 10

bonus S(single) **1 / D(double)  **2 / T(triple) **3

option * or # or null
*의 경우 n번째와 n-1 번째 점수 2배
#의 경우 n번째 점수 -로 적용

ps) 첫번째 판의 경우 n만 2배
* 중첩 가능

*와 # 중첩 가능
이 경우 -로 적용되는 점수 2배
무조건 # 이후 *가 오는 경우에 적용 됨.

3번의 기회
1번당 0 < score < 10


'''