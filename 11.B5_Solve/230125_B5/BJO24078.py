from sys import stdin
input = stdin.readline

def check(n):
    print(n % 21)
    
if __name__ == '__main__':
    n = int(input())
    check(n)
        
    
    
'''
X を 21 で割った余りを出力せよ．
'''