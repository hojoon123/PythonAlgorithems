from sys import stdin
input = stdin.readline

def check(len_top, top_list):
    receive_top_list = [0]
    for i in range(1,len_top):
        for j in range(i,-1,-1):
            if top_list[j-1] > top_list[i]:
                receive_top_list.append(j)
                break
        else:
            receive_top_list.append(0)
                
    return (" ".join(map(str, receive_top_list)))

if __name__ == '__main__':
    n = int(input())
    tops = list(map(int,input().split()))
    result = check(n, tops)
    print(result)
    
        

'''
예제 입력 1 
5
6 9 5 7 4
예제 출력 1 
0 0 2 2 4
'''