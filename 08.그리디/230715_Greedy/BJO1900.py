import sys
input = sys.stdin.readline
      


if __name__ =="__main__":
    n=int(input())
    user=[]
    for i in range(n):
        power,ring=map(int,input().split())
        user.append([power,ring,i+1])
        
        
    user.sort(key=lambda x:(x[1]-1)/x[0])
    user.reverse()

    for i in range(n):
        print(user[i][2])


'''
이긴사람이 제일 적은 사람이 제일 앞 
power + ring * otherPower
첫째 줄에 단어의 개수 N(1 ≤ N ≤ 10)
예제 입력 1 
3
10 3
18 4
15 5
예제 출력 1 
3
1
2
'''