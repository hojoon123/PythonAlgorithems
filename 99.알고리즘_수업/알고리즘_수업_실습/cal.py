import matplotlib.pyplot as plt
import time
import sys
sys.setrecursionlimit(10**6)

def cal(x):
    # 각 x 값에 대한 실행 시간 측정 및 저장
    execution_times_1 = []
    execution_times_2 = []
    for i in x:
        start_time = time.time()
        fac_1(i)
        end_time = time.time()
        execution_time = end_time - start_time
        execution_times_1.append(execution_time)
        
        start_time = time.time()
        fac_2(i)
        end_time = time.time()
        execution_time = end_time - start_time
        execution_times_2.append(execution_time)
    result = []
    result.append(execution_times_1)
    result.append(execution_times_2)
    return result

def fac_1(n):
    if n == 0:
        return 1
    else :
        return n * fac_1(n - 1)

def fac_2(n):
    result = 1
    for k in range(n,0,-1):
        result = result * k
    return result

if __name__ == "__main__":
    # x 값 범위 설정 (예: 0에서 10까지)
    user_input = int(input())
    x = range(user_input)  # 0부터 10까지의 x 값
    res = cal(x)
    y_1 = res[0]
    y_2 = res[1]
    # 그래프 그리기
    plt.plot(x, y_1, marker='o', linestyle='-', color='r')
    plt.plot(x, y_2, marker='o', linestyle='-', color='b')

    # 그래프에 제목과 축 레이블 추가
    plt.title('Factorial Function Execution Time')
    plt.xlabel('x')
    plt.ylabel('Execution Time : Factorial(x)')

    # 그래프 보여주기
    plt.grid(True)  # 그리드 표시
    plt.show()
    
