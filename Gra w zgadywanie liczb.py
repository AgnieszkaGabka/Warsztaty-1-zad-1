# Prosta gra konsolowa, w której komputer losuje liczbę z przedziału od 1 do 100, a użytkownik ją zgaduje. Po każdej
# próbie dostaje odpowiedź, czy podana liczba jest za mała, czy za duża.
import random

dobrze = False
x = random.randint(1, 11)


while not dobrze:
    try:
        y = int(input("Guess the number 1 - 10: "))
        if x == y:
            print("You won!")
            dobrze = True
        elif x > y:
            print("Too small!")
        else:
            print("Too big!")
    except (TypeError, ValueError):
        print("Its not a number!")

print(gra())
