import sys
input = sys.stdin.readline


n = int(input().rstrip())
words = []
for _ in range(n): words.append(input().rstrip())
dict = {}

for word in words:
  square_root = len(word) - 1
  for c in word:
    if c in dict:
      dict[c] += pow(10, square_root)
    else:
      dict[c] = pow(10, square_root)
      
    square_root -= 1 


dict = sorted(dict.values(), reverse=True)


result,m = 0,9


for value in dict:
  result += value * m
  m -= 1

print(result)


'''

첫째 줄에 단어의 개수 N(1 ≤ N ≤ 10)
모든 단어에 포함되어 있는 알파벳은 최대 10개이고, 수의 최대 길이는 8
예제 입력 1 
2
AAA
AAA
예제 출력 1 
1998
'''