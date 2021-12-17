# Prosta gra konsolowa, w której komputer losuje liczbę z przedziału od 1 do 100, a użytkownik ją zgaduje. Po każdej
# próbie dostaje odpowiedź, czy podana liczba jest za mała, czy za duża.
import random

good = False
x = random.randint(1, 11) #losowanie liczby miedzy 1 a 10


while not good: #dopóki gracz nie zgadnie liczby komputera, wykonaj poniższe działania
    try:
        y = int(input("Guess the number 1 - 10: ")) #poproś o wpisanie zgadywanej liczby
        if x == y:
            print("You won!") #jeśli się zgadza, zwróć odpowiedź
            good = True
            break
        elif x > y:
            print("Too small!") # jeśli za mała, zwróć odpowiedż
        else:
            print("Too big!") #jeśli za duża, zwróć odpowiedź
    except (TypeError, ValueError):
        print("Its not a number!") #jeśli gracz wpisze błędne dane, zwróć odpowiedź


