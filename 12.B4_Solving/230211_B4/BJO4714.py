import sys
input = sys.stdin.readline

def check():
    while 1:
        w = float(input())
        if w == -1:
            break
        print("Objects weighing {:.2f} on Earth will weigh {:.2f} on the moon.".format(w, w*0.167))
    
if __name__ == '__main__':
    check()
    

'''
예제 입력 1 
100.0
12.0
0.12
120000.0
-1.0
예제 출력 1 
Objects weighing 100.00 on Earth will weigh 16.70 on the moon.
Objects weighing 12.00 on Earth will weigh 2.00 on the moon.
Objects weighing 0.12 on Earth will weigh 0.02 on the moon.
Objects weighing 120000.00 on Earth will weigh 20040.00 on the moon.
'''