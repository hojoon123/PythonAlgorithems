import sys
input = sys.stdin.readline

s = list(str(input().rstrip()))
i = 0
iron = 0
tmp = 0
result = 0  
while i < len(s):
    if s[i] == '(':
        i += 1
        while s[i] == '(':
            i += 1
            iron += 1
        else: # '('를 만나고')'를 만남 즉 레이저
            i += 1
            if tmp != iron:
                result += (iron-tmp)*2
                if tmp != 0:
                    result += tmp
            else:
                result += iron
            tmp = iron
            
    else:   # '(' 를 만나지 않고 바로 ')' 만 올 때 막대 길이 하나 빼주기
        iron -= 1 
        i += 1
        tmp = iron
print(result)
'''
해보고 느낀점 실버2 문제라고 했다. 솔직히 푸는데 크게 어려움은 없었다. (사실 1시간 넘게 걸렸다)
일단 문제 자체는 시행착오를 거치며 조건을 추가해서 작성하였다.
그러다 보니 코드가 매우 원시적이고 더럽고 가독성 구리고 그냥 못했다.
솔직히 내가 작성한 코드지만, 이거 좀 진짜 넘 별로다.... 작성하면서도 아 이렇게 복잡해지면
좀 에반데...싶었지만 일단 끝까지 풀었다. 작성한 코드는 대략 30줄 걸린 시간은 96ms 다.
솔직히 자료구조 문제인데 무지성으로 풀었기에, 자료구조를 활용해서 사용한 코드를 보았다
cpoy에 있는 코드인데, 어마어마하게 좋은 가독성을 보며 진짜... 공부를 더 열심히 해야겠다고 느꼈다..
'''