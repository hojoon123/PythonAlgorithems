from sys import stdin
input = stdin.readline

def check(k):
    for i in range(k):
        quest = input().rstrip()
        if quest.isdigit():
            print(dict[int(quest)])
        else:
            print(dict[quest])

if __name__ == '__main__':
    n, k = map(int,input().split())
    dict = {}
    for i in range(1, n + 1):
        p = input().rstrip()
        dict[i] = p
        dict[p] = i
    check(k)
        

'''
예제 입력 1 
26 5
Bulbasaur
Ivysaur
Venusaur
Charmander
Charmeleon

Charizard
Squirtle
Wartortle
Blastoise
Caterpie

Metapod
Butterfree
Weedle
Kakuna
Beedrill

Pidgey
Pidgeotto
Pidgeot
Rattata
Raticate

Spearow
Fearow
Ekans
Arbok
Pikachu

Raichu

25
Raichu
3
Pidgey
Kakuna
예제 출력 1 
Pikachu
26
Venusaur
16
14
'''