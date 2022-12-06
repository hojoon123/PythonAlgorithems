a, b = map(str,input().split())
a,b = a[::-1], b[::-1]
a,b = int(a),int(b)
if(a > b):
    print(a)
else:
    print(b)
'''
거꾸로 읽는다
그 중 큰 수 출력
예제 입력 1 
734 893
예제 출력 1 
437
'''