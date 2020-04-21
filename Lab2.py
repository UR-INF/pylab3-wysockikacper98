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


#Zadanie 6















