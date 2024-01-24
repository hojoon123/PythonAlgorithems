from sys import stdin
input = stdin.readline

def check(n):
    for i in range(n):
        arr = list(map(int,input().split()))
        if arr[0] * arr[1] > arr[2] * arr[3] :
            print("TelecomParisTech")
        elif arr[0] * arr[1] < arr[2] * arr[3] :
            print("Eurecom")
        else :
            print("Tie")
    
if __name__ == '__main__':
    n = int(input())
    check(n)
        
    

'''
예제 입력 1 
2
3 2 4 2
536874368 268792221 598 1204
예제 출력 1 
Eurecom
TelecomParisTech
'''