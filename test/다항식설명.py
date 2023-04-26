# 클래스로 구현.
class Polynomial :
    # 아래에서 최고 차수 2  x^2: 5 / x^1: -3  / x^0: 12 를 입력받았다는 기준으로 설명
    def __init__( self ):
        self.coef= []

    # 최고 차수를 구하기 위해서 맞음
    # 보면 입력할 때 최고 차수를 2로 하면
    # x^2 x^1 x^0 총 3개를 입력 받아서
    # 입력받은 배열의 길이에 1을 빼줘서 2를 받음
    def degree(self) :
        return len(self.coef) - 1

    # 연산 과정을 보여주기 위해서 만든 함수임
    def display(self, msg="f(x) = "):
        print("  ", msg, end='')
        # 최고 차수를 deg에 넣음
        deg = self.degree()

        #ㅇㅇ 맞음 최고차수 부터 0까지 1씩 빼면서 돌림
        for n in range(deg, 0, -1) :
            # 디스플레이를 보여주기 위해서 소수점 1의 자리까지와 x^%d로 차수를 표시
            # deg가 2라면 n은 2, 1 순서대로 반복
            # 배열에서 coef[2] coef[1] 꺼내서 붙임
            print("%5.1f x^%d + " % (self.coef[n], n), end='')
        # x^0은 따로 꺼내서 coef[0]으로 해줬음. x^0을 출력하지 않고 숫자만 출력하고 싶은 것 같음
        print("%4.1f"%self.coef[0])

    # 다항식 더하기
    def add(self, b):
        # 먼저 클래스 인스턴스 생성
        p = Polynomial()
        # 아래 테스트 케이스 c = a.add(b)
        # 여기선 a가 self b가 b임
        # 테스트 케이스 기준으로 read_poly() 마지막에 뒤집어 줬으니 거꾸로 들어가 있음
        # a는 최고차수 2에 순서대로 12.0 + -3.0 x^1 + 5.0 x^2
        # b는 최고차수 3에 순서대로 -4.0 + 0.0 x^1 + -6.0 x^2 + 2.0 x^3
        # a.degree() 하면 2 / b.degree() 하면 3
        
        
        # 해당 테스트 케이스는 여기로 빠지지 않음.
        # 일단 여기는 가정으로 3 2 가 들어갔다고 하고 설명
        # p.coef에는 a의 배열이 들어가 있음 처음에
        # a.add(b) 해서 p.coef는 a.coef라고 생각하면 됨.
        # 그래서 a 배열의 차수가 더 크다. 즉 a 배열의 길이가 더 길고 들어가 있는게 많아서
        # 그냥 coef 각 차수 마다 b에 있는 차수 더하면 됨.
        # 아래의 a, b는 가정임. 내가 임의로 설정함
        # a는 최고차수 3에 순서대로 -4.0 + 0.0 x^1 + -6.0 x^2 + 2.0 x^3
        # b는 최고차수 2에 순서대로 12.0 + -3.0 x^1 + 5.0 x^2
        if self.degree() > b.degree() :
            # 만약에 a의 최고차수가 b보다 크다는 가정이라면 ex ) 3 2 
            # b의 최고차수 개수 2에 + 1 만큼 반복 3
            # add함수에서 생성한 인스턴스 배열 coef에 b 인스턴스 배열 coef를 더함
            # 앞에서부터 x^0 x^1 x^2 이렇게 들어감
            for i in range(b.degree()+1) :
                p.coef[i] += b.coef[i]
                
                
        #b가 더 크니까 else로 빠짐짐
        else :
            # a는 최고차수 2에 순서대로 12.0 + -3.0 x^1 + 5.0 x^2
            # b는 최고차수 3에 순서대로 -4.0 + 0.0 x^1 + -6.0 x^2 + 2.0 x^3
            # a에 b를 더해야 하는데 a의 coef 배열엔 12.0 + -3.0 x^1 + 5.0 x^2 총 3개
            # 반면 b는 4개가 들어가 있어서 그냥 자리수에 더하려고 하면 인덱스 범위 오류 뜸
            # 그래서 a의 coef배열의 개수도 b의 coef 배열이랑 개수를 맞춰주어야 해서
            # a의 coef 배열을 b로 바꿔버리고 a를 더하는거임.
            p.coef = list(b.coef)
            # 여기는 b로 바꾼 coef 배열에 a의 배열의 값을 더해주는 반복문
            for i in range(self.degree()+1) :
                p.coef[i] += self.coef[i]
        return p

    # 다항식 값을 계산하는 함수
    def eval(self, x):
        # result 먼저 선언 float 형으로
        result = 0.0
        
        #반복문 돌면서 계수에다가 x만큼 제곱해줌 
        #아래의 테스트 케이스에선 2로 해서 2제곱으로 결과가 나옴
        for i in range(self.degree()+1) :
            result += self.coef[i] * (x**i)
        return result

    # 뺄셈, 곱셈 관련 함수 추가할 것

def read_poly():
    # 클래스 인스턴스 생성
    p = Polynomial()
    
    # 다항식 최고 차수 입력 받기
    deg = int(input("다항식의 최고 차수를 입력하시오: "))
    
    # 최고 차수 만큼 반복해서 계수를 입력받는거임.
    for n in range(deg+1) :
        # coef라는 변수를 설정해준거임. 아래 p.coef랑은 관련없음 
        # 이름이 coef 말고 다른 걸로 바뀌어도 괜찮음.
        # deg가 2면 3번 반복해서 x^2 계수 x^1 계수 x^0 의 계수 총 3개 받아옴.
        coef = float(input(  "\tx^%d의 계수 : " % (deg-n)))
        
        #인스턴스 생성자에서 정의한 coef 배열에 변수 coef를 넣어줌 변수 coef는 마찬가지로
        # coef말고 tmp등 다른 이름으로 바꿔줄 수 있음.
        p.coef.append(coef)
    # coef 배열에 x^2 x^1 부터 들어가게 됨.
    # 이렇게 뒤집어주지 않으면 나중에 연산할 때 문제가 발생할 수 있음.
    # 예를 들어서 최고차수가 2와 3인 다항식을 더할 때,
    # ex)  x^2 x^1 x^0    / x^3 x^2 x^1 x^0
    # 연산을 순서대로 하기 때문에 x^2 + x^3 이렇게 해버림
    # 이걸 방지하기 위해서 뒤집어서 x^0의 계수가 먼저 오게 하면
    # x^0 + x^0 / x^1 + x^1 / x^2 + x^2 / x^3
    # 이렇게 순서에 맞게 연산함.
    p.coef.reverse()
    # 생성한 인스턴스를 리턴해줌
    return p

# 테스트 코드.... 뺄셈, 곱셈 추가할 것
a = read_poly()
print(" ")
b = read_poly()
c = a.add(b)

a.display("A(x) = ")
b.display("B(x) = ")
c.display("C(x) = ")
print(" C(2) = ", c.eval(2))
