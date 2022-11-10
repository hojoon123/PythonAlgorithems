class Cal():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def Sum(self):
        result = self.a + self.b
        return result
    def Sub(self):
        result = self.a - self.b
        return result
    def Mul(self):
        result = self.a * self.b
        return result
    def Div(self):
        result = self.a / self.b
        return result
    def Remainder(self):
        result = self.a % self.b
        return result

a,b =map(int, input().split())

result=Cal(a,b)
print(result.Sum())
print(result.Sub())
print(result.Mul())
print(int(result.Div()))
print(result.Remainder())
