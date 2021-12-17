# Prosta gra konsolowa, w której komputer losuje liczbę z przedziału od 1 do 100, a użytkownik ją zgaduje. Po każdej
# próbie dostaje odpowiedź, czy podana liczba jest za mała, czy za duża.
import random

dobrze = False
x = random.randint(1, 11)


while not dobrze: #dopóki gracz nie zgadnie liczby komputera, wykonaj poniższe działania
    try:
        y = int(input("Guess the number 1 - 10: ")) #poproś o wpisanie zgadywanej liczby
        if x == y:
            print("You won!") #jeśli się zgadza, zwróć odpowiedź
            dobrze = True
        elif x > y:
            print("Too small!") # jeśli za mała, zwróć odpowiedż
        else:
            print("Too big!") #jeśli za duża, zwróć odpowiedź
    except (TypeError, ValueError):
        print("Its not a number!") #jeśli gracz wpisze błędne dane, zwróć odpowiedź

print(gra())
