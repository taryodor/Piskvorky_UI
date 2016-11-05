import random

def test_mezy_kozy(pole, zajmovy_symbol):
    global tah_rozhodnut
    i = 0
    while i < len(pole) - 2:
        if pole[i] == zajmovy_symbol and pole[i + 2] == zajmovy_symbol and pole[i + 1] == "-":
            tah_rozhodnut = True
            return i + 1
            break
        i = i + 1

def tah_ai(pole, symbol_ai, symbol_eny):
    #AI pro tah pocitace
    #zacneme definicema seznamu
    seznam_hranych_ai_pozic = []
    seznam_hranych_eny_pozic = []
    pozice_ai_tahu = 0
    #Definice veledulezite boolean promenne
    global tah_rozhodnut
    tah_rozhodnut = False

    if len(pole) < 6:
        raise ValueError("Takhle kratke hraci pole si strcte do muslimske ctvrti.")

    if symbol_ai not in pole and symbol_eny not in pole:#kontrola, ze hraci pole je prazdne
        if len(pole) == 6:
            return 2
        else:
            return random.choice((2, len(pole) - 4)) #2 tj. treti od zacatku a len-4 tj. treti od konce
            #kdyz bude pole moc kratke na poradne hrani, neva stale je toto nejlepsi volba

    for i in range(0,len(pole)):#ulozeni hranych tahu pro dalsi vyhodnoceni,
        #mozna do budoucna zrusim, uvidime, jestli to vyuziji
        if pole[i] == symbol_ai:
            seznam_hranych_ai_pozic.append(i)
        elif pole[i] == symbol_eny:
            seznam_hranych_eny_pozic.append(i)

    if len(seznam_hranych_ai_pozic) > 1 and tah_rozhodnut == False:
        pozice_ai_tahu = test_mezy_kozy(pole, symbol_ai)
        return pozice_ai_tahu

    if len(seznam_hranych_eny_pozic) > 1 and tah_rozhodnut == False:
        pozice_ai_tahu = test_mezy_kozy(pole, symbol_eny)
        return pozice_ai_tahu

    return pozice_ai_tahu


#print(tah_ai("---x-x---xo-o--", "x", "o"))
