"""
Muj pokus o 1D piskvorky
"""
from random import randint

def vyhodnot(herni_pole):
    if "xxx" in herni_pole:
        return "x"
    elif "ooo" in herni_pole:
        return "o"
    elif "-" not in herni_pole:
        return "!"
    else:
        return "-"


def tah(pole, cislo_policka, symbol):
    if pole[cislo_policka] != "-":
        raise ValueError("Hrajes na zaplnene policko")
    return pole[:cislo_policka] + symbol + pole[cislo_policka+1:]

def tah_hrace(pole):
    while True:
        hrana_pozice = input("Na kolikatou pozici chces hrat?")
        hrana_pozice = int(hrana_pozice) - 1
        if pole[hrana_pozice] == "-":
            break
    return tah(pole, hrana_pozice, "x")

def tah_pocitace(pole):
    pozice = -1
    while pozice < 0 or pozice >= len(pole) or pole[pozice] != "-":
        pozice = randint(0, len(pole) - 1)
    return tah(pole, pozice, "o")
"""
vypnuto jen kvuli testovani
def piskvorky1d():
    pole = '-' * 20
    i = 0
    while True:
        if i % 2 == 0:
            pole = tah_hrace(pole)
        else:
            pole = tah_pocitace(pole)
        print(pole)

        if vyhodnot(pole) == 'o':
            print('Vyhrál počítač.')
        elif vyhodnot(pole) == 'x':
            print('Vyhrál jsi.')
        elif vyhodnot(pole) == '!':
            print('Remíza!')

        if vyhodnot(pole) != '-':
            break

        i += 1

piskvorky1d()
"""
