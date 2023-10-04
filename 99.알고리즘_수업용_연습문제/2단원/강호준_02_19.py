from sys import stdin
input = stdin.readline

# 5 / 1,2  2.5 / 1,2 1.25 1,2 / 0.725
# 2배씩 늘어남 5는 근데 1개니까 1빼기 
# 2**4 - 1
def asterisk(i):
    if i > 1:
        asterisk(i/2)
        asterisk(i/2)
    print("*", end='') 

if __name__ == "__main__": # 메인문입니다.
    user_input = int(input())
    asterisk(user_input)
    
'''
asterisk(5) = 15
'''    