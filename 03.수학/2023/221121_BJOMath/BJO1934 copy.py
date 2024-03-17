import sys
input = sys.stdin.readline

def gcd(x, y):  #최대공약수 구하기
  if y == 0:
    return x
  else:
    return gcd(y, x%y)
  
def lcm(x, y):  ## 최소공배수 구하기
  result = (x*y) // gcd(x,y)
  return result

t = int(input())

for i in range(t):
    n = list(map(int,input().split()))
    print(lcm(n[0],n[1]))


'''
예제 입력 1 
3
1 45000
6 10
13 17
예제 출력 1 
45000
30
221
'''