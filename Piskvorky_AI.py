import random
#Chybi dodelat detektor dvoudiry a radny protitah (udelej jako dalsi seznam)
#NA dvoudirovy utok musis odpovedet jedine zabranim vydalenejsi diry, jinak jsi v pr...
#Ma smysl delat dvoudirovy utok?CHci to zkusit...
def test_dve_vedle_sebe(pole, zajmovy_symbol):
    global tah_rozhodnut
    i = 0
    while i < len(pole) - 1:
        if pole[i] == zajmovy_symbol and pole[i + 1] == zajmovy_symbol:
            if i + 1 < len(pole) - 1 and pole[i + 2] == "-":
            #Tato podminka je tu proto, aby mi nepretekal zasobnik s polem
                tah_rozhodnut = True
                print("i+2")
                return i + 2
                break
            elif pole[i - 1] == "-" and i - 1 >= 0:
                tah_rozhodnut = True
                print("i-1")
                print("i je ", i)
                return i - 1
                break
        i = i + 1

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
    seznam_volnych_pozic = []
    seznam_oboustrane_hratelnych_ai_pozic = []
    seznam_levostrane_hratelnych_ai_pozic = []
    seznam_pravostrane_hratelnych_ai_pozic = []
    pozice_ai_tahu = 0
    #Definice veledulezite boolean promenne
    global tah_rozhodnut
    tah_rozhodnut = False

    if len(pole) < 6:
        raise ValueError("Takhle kratke hraci pole si strcte do muslimske ctvrti.")

    if symbol_ai not in pole and symbol_eny not in pole:#kontrola, ze hraci pole je prazdne
        if len(pole) == 6:
            tah_rozhodnut = True
            return 2
        else:
            tah_rozhodnut = True
            return random.choice((2, len(pole) - 4)) #2 tj. treti od zacatku a len-4 tj. treti od konce
            #kdyz bude pole moc kratke na poradne hrani, neva stale je toto nejlepsi volba

    for i in range(0,len(pole)):#ulozeni hranych tahu pro dalsi vyhodnoceni,
        #mozna do budoucna zrusim, uvidime, jestli to vyuziji
        if pole[i] == symbol_ai:
            seznam_hranych_ai_pozic.append(i)
            if (i > 0 and i < len(pole) - 2 and pole[i - 1] == "-" and pole[i + 1] == "-"):
                seznam_oboustrane_hratelnych_ai_pozic.append(i)
            if (i > 1 and i < len(pole) - 1 and pole[i - 1] == "-" and pole[i - 2] == "-"):
                seznam_levostrane_hratelnych_ai_pozic.append(i)
            if (i < len(pole) - 2 and pole[i + 1] == "-" and pole[i + 2] == "-"):
                seznam_pravostrane_hratelnych_ai_pozic.append(i)
        elif pole[i] == symbol_eny:
            seznam_hranych_eny_pozic.append(i)
        elif pole[i] == "-":
            seznam_volnych_pozic.append(i)
    print("obou: {}, levo: {}, pravo: {}".format( seznam_oboustrane_hratelnych_ai_pozic, seznam_levostrane_hratelnych_ai_pozic, seznam_pravostrane_hratelnych_ai_pozic))

    #Tady jdeme testovat, zdali nejsme jen jeden tah od vyhry, resp. prohry
    #Mezy kozy
    if len(seznam_hranych_ai_pozic) > 1 and tah_rozhodnut == False:
        pozice_ai_tahu = test_mezy_kozy(pole, symbol_ai)
        print("1")
        if tah_rozhodnut == True:
            return pozice_ai_tahu
    if len(seznam_hranych_ai_pozic) > 1 and tah_rozhodnut == False:
        pozice_ai_tahu = test_dve_vedle_sebe(pole, symbol_ai)
        print("2")
        if tah_rozhodnut == True:
            return pozice_ai_tahu
    if len(seznam_hranych_eny_pozic) > 1 and tah_rozhodnut == False:
        pozice_ai_tahu = test_mezy_kozy(pole, symbol_eny)
        print("3")
        if tah_rozhodnut == True:
            return pozice_ai_tahu
    if len(seznam_hranych_eny_pozic) > 1 and tah_rozhodnut == False:
        pozice_ai_tahu = test_dve_vedle_sebe(pole, symbol_eny)
        print("4")
        if tah_rozhodnut == True:
            return pozice_ai_tahu

#jdeme na prvni tah na krajni pozice
    if len(seznam_hranych_eny_pozic) == 1 and len(seznam_hranych_ai_pozic) == 0:
        #eny hraje na 1./2. pozici
        if seznam_hranych_eny_pozic[0] == 0 or seznam_hranych_eny_pozic[0] == 1:
            pozice_ai_tahu = seznam_hranych_eny_pozic[0] + 2
            tah_rozhodnut = True
            print("11")
            return pozice_ai_tahu
        if seznam_hranych_eny_pozic[0] == len(pole) - 1 or seznam_hranych_eny_pozic[0] == len(pole) - 2:
            pozice_ai_tahu = seznam_hranych_eny_pozic[0] - 2
            tah_rozhodnut = True
            print("12")
            return pozice_ai_tahu
        #eny hraje na 3./4.pozici
        if seznam_hranych_eny_pozic[0] == 2 or seznam_hranych_eny_pozic[0] == 3:
            pozice_ai_tahu = seznam_hranych_eny_pozic[0] + 1
            tah_rozhodnut = True
            print("13")
            return pozice_ai_tahu
        if seznam_hranych_eny_pozic[0] == len(pole) - 3 or seznam_hranych_eny_pozic[0] == len(pole) - 4:
            pozice_ai_tahu = seznam_hranych_eny_pozic[0] - 1
            tah_rozhodnut = True
            print("14")
            return pozice_ai_tahu
    #Neni vybrana zadna strategie, volim nahodnou pozici
        #Pokud mam nekde osamoceny znak, hraju jej

    if len(seznam_oboustrane_hratelnych_ai_pozic) > 0:
        return random.choice(seznam_oboustrane_hratelnych_ai_pozic) - 1
    elif len(seznam_levostrane_hratelnych_ai_pozic) > 0:
        return random.choice(seznam_levostrane_hratelnych_ai_pozic) - 1
    elif len(seznam_pravostrane_hratelnych_ai_pozic) > 0:
        return random.choice(seznam_pravostrane_hratelnych_ai_pozic) + 1


#Tady budu volat utocici funkci, ktera nejdriv vybere vhodne misto

    return random.choice(seznam_volnych_pozic)


print("tah bude: ", tah_ai("gggi---gigi---hi--gigg", "i", "g"))
