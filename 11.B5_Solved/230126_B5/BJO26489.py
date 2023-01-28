from sys import stdin
#input = stdin.readline

def check():
    cnt = 0
    while 1:
        try:
            s = str(input())
            cnt += 1
        except:
            break
    return cnt
        
    
if __name__ == '__main__':
    print(check())
        
    

'''
예제 입력 1 
gum gum for jay jay
gum gum for jay jay
gum gum for jay jay
gum gum for jay jay
gum gum for jay jay
gum gum for jay jay
gum gum for jay jay
gum gum for jay jay
gum gum for jay jay
gum gum for jay jay
gum gum for jay jay
예제 출력 1 
11
'''