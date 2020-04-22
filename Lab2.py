# fragmenty dotyczące rozwiązania poszczególnych zadań proszę oddzielić odpowiednimi komentarzami

from builtins import print
from array import *

# Zadanie 2
# Napisz skrypt wypełniający tablicę znakami, a następnie wyświet znaki w kolejności odwrotnej do wprowadzania. Dane wprowadzane z klawiatury


# dlugosc = int(input("Podaj długość wczytywaniej tablicy: "))
# tablica = array("i")
# for i in range(dlugosc):
#     temp = int(input("Tab["+str(i)+"] = "))
#     tablica.append(temp)
#
# print(tablica[::-1])


# Zadanie 3
# Wypełniający tablicę liczbami losowymi rzeczywistymi z przedziału (-5,5). Wartość tablicy zapisz do pliku result.txt


# import random
# tablica = []
# for i in range(10):
#     tablica.append(random.randint(-5, 5))
#
# file = open("result.txt", "a")
# file.write(str(tablica) + "\n")
# file.close()


# Zadanie 4
# Napisz funkcję tworzącą tablicę dwuwymiarową (5x5) która zostanie wypełniona kwadratami liczb z komórek z wiersza wcześniejszego. Pierwszy wiersz wypełniony wartościami 2,3,4,5,6.
# Do utworzenia tablicy dwuwymiarowej wykorzystaj bibiotekę NumPy.

# import numpy as np
#
# array = np.zeros(shape=(5, 5))
# array[0, 0:] = [2, 3, 4, 5, 6]
# for i in range(1, 5):
#     for j in range(5):
#         array[i, j] = array[i-1, j]**2
#
#
# print(array)

# Zadanie 5
# Napisz funkcję, która jako parametr przyjmuje lokalizację pliku tekstowego który zawiera dowolny tekst i zwraca histogram
# znaków występujących w tym napisie (czyli pary znak-liczba wystąpień). Wynikiem powinien być słownik. Przykład:
# >>> histogram("document.txt") dokument zawiera tekst: Ala ma kota {'t': 1, 'a': 3, 'l': 1, 'A': 1, 'k': 1, 'm': 1, 'o': 1}


# def histogram(lokalizacja):
#     file = open(lokalizacja, "r")
#     slownik = {}
#     while True:
#         litera = file.read(1).upper() #bez funkcji upper() funcja będzie zliczała osobno wielkie i duże litery
#         if not litera:
#             break
#         if not litera.isalpha():
#             continue
#         elif litera in slownik:
#             slownik[litera] += 1
#         else:
#             slownik[litera] = 1
#
#     print(slownik)
#     file.close()
#
#
# histogram("document.txt")


# Zadanie 6
# Napisz następujące funkcje niezbędne do implementacji gry w pokera pięciokartowego dobieranego:
# deck() - zwraca listę reprezentującą talię kart w kolejności od najmłodszej do najstarszej. Każda karta posiada 2 atrybuty, będące łańcuchem tekstowym:
# rangę - możliwe wartości: '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'D', 'K', 'A' (karty od 2 do 10 oraz walet, dama, król, as)
#
# kolor - możliwe wartości:
#
# 🔹c - ♣ trefl (clubs)
#
# 🔹d - ♣ karo (diamonds)
#
# 🔹h - ♥ kier (hearts)
#
# 🔹s - ♠ pik (spades)
#
# Każdym elementem listy powinna być krotka, będąca parą (ranga, kolor). Przykładowo as pik:
#
# 🂡
# reprezentowany będzie jako ('A', 's'). Lista powinna zawierać 52 elementy (13 rang * 4 kolory).
#
# shuffle_deck(deck) - przyjmuje listę kart, zwraca karty potasowane (permutacja). Skorzystaj z:
#
# deal(deck, n) - przyjmuje talię kart (deck) oraz liczbę graczy (n), zwraca n-elementową listę 5-elementowych list z kartami rozdanymi graczom. Każda 5-elementowa lista kart gracza zawiera 5 krotek reprezentujących kartę.

import random


def deck():
    ranga = '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'D', 'K', 'A'
    kolorFigury = '♣', '♦', '♥', '♠'  # jeśli grafika nie wyświetla sie prawidłowo należy zakomentować tą linię oraz usunąć komentarz z linii poniżej
    # kolorFigury= 'C', 'D', 'H', 'S'
    lista = []
    for i in kolorFigury:
        for j in ranga:
            lista.append([i, j])
    return lista


def shuffle_deck(lista):
    random.shuffle(lista)
    return lista


def deal(lista, n):
    dealList = []
    hand = []
    for i in range(n):
        for j in range(5):
            hand.append(lista.pop())
        dealList.append(hand)
        hand = []
    return dealList


# print(deck())
# print(shuffle_deck(deck()))
print(deal(shuffle_deck(deck()), 3))
