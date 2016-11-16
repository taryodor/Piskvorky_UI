import random

def overeni_pole_4_podminky(i, mensi_nez_i, pole, omezeni_pole , i1, i2, i3, i4, p1, p2, p3, p4):
    #funkce nahrazujici if se ctyrma podminkama, rozsah i>mensi_nez_i,len-omezeni_pole,
    lokalni_seznam = []
    if i>mensi_nez_i and i<len(pole)+omezeni_pole:
        if pole[i1]==p1 and pole[i2]==p2 and pole[i3]==p3 and pole[i4]==p4:
            lokalni_seznam.append(i)
            x=random.choice(lokalni_seznam)
            return x

def overeni_pole_3_podminky(i, mensi_nez_i, pole, omezeni_pole , i1, i2, i3, p1, p2, p3):
    #funkce nahrazujici if se trema podminkama, rozsah i>mensi_nez_i,len-omezeni_pole
    lokalni_seznam = []
    if i>mensi_nez_i and i<len(pole)+omezeni_pole:
        if pole[i1]==p1 and pole[i2]==p2 and pole[i3]==p3:
            lokalni_seznam.append(i)
            x=random.choice(lokalni_seznam)
            return x

def overeni_pole_5_podminek_1_not(i, mensi_nez_i, pole, omezeni_pole , i1, i2, i3, i4, i5, p1, p2, p3, p4, p5):
    #funkce nahrazujici if se trema podminkama, rozsah i>mensi_nez_i,len-omezeni_pole
    lokalni_seznam = []
    if i>mensi_nez_i and i<len(pole)+omezeni_pole:
        if pole[i1]!=p1 and pole[i2]==p2 and pole[i3]==p3 and pole[i4]==p4 and pole[i5]==p5:
            lokalni_seznam.append(i)
            x=random.choice(lokalni_seznam)
            return x

def alt_ai(pole, ai_symbol):
    #Aby moje nadrazena AI fungovala i v podradnym algoritmu nasich koucu, musim tady udelat
    #tuhle deklaraci, nebo jak to nazvat. Proste jde o to, aby pocitac vedel kdo je kdo
    # je to takovy Identify Friend-Foe
    if ai_symbol == "x":
        eny_symbol = "o"
    elif ai_symbol == "o":
        eny_symbol = "x"
    volno_symbol = "-"

    #Tady si vytvorim dvourozmerny seznam pro ukladani priorit hrani, cim vyssi 1. rozmer, tim spis by to progam mel hrat
    #Na konci algoritmu si nahodne vyberu ze seznamu s nejvyssi nalezenou prioritou
    seznam_priorit = []
    for i in range(8):
        seznam_priorit.append([])

    if len(pole) < 5:
        return None

    for i in range(0, len(pole)):#nejdriv testuju priority 1 a dva, tj. volne pozice resp. hratelne 3. poz od kraje
        #jen se ujistim, ze priorizovane pole bude mit tolik znaku, kolik potrebuji,
        if pole[i] == volno_symbol:
            seznam_priorit[1].append(i)
        if pole[i-2] == volno_symbol and pole[i-1]==volno_symbol and i==2 and pole[i+1]==volno_symbol and pole[i+2]!=eny_symbol:
            seznam_priorit[2].append(i)
        if i>1:
            if pole[i-2]!=eny_symbol and pole[i-1]==volno_symbol and i==len(pole)-3 and pole[i+1]==volno_symbol and pole[i+1]==volno_symbol:
                seznam_priorit[2].append(i)

        #Jdu na prior. 3 tj. prilozeni k me pozici, vyroba 1/2diry
        seznam_priorit[3].append(overeni_pole_4_podminky(i, 1, pole, -1, i, i+1, i-2, i-1, volno_symbol, volno_symbol, volno_symbol, ai_symbol))
        seznam_priorit[3].append(overeni_pole_4_podminky(i, 0, pole, -2, i-1, i, i+1, i+2, volno_symbol, volno_symbol, ai_symbol, volno_symbol))
        #vpravo+vlevo od pozice se da hrat
        seznam_priorit[3].append(overeni_pole_3_podminky(i, 0, pole, -1, i-1, i, i+1, ai_symbol, volno_symbol, volno_symbol))
        seznam_priorit[3].append(overeni_pole_3_podminky(i, 1, pole, -1, i-1, i, i+1, volno_symbol, volno_symbol, ai_symbol))
        #vyrobyt jednodiru od me pozice vpravo+vlevo
        seznam_priorit[3].append(overeni_pole_3_podminky(i, 1, pole, 0, i-2, i-1, i, ai_symbol, volno_symbol, volno_symbol))
        seznam_priorit[3].append(overeni_pole_3_podminky(i, -1, pole, -2, i, i+1, i+2, volno_symbol, volno_symbol, ai_symbol))
        #Vyroba dvoudiry od eny pozice vlevo+vpravo
        seznam_priorit[3].append(overeni_pole_5_podminek_1_not(i, 0, pole, -3, i-1, i, i+1, i+2, i+3, eny_symbol, volno_symbol, volno_symbol, volno_symbol, eny_symbol))
        seznam_priorit[3].append(overeni_pole_5_podminek_1_not(i, 3, pole, -1, i+1, i, i-1, i-2, i-3, eny_symbol, volno_symbol, volno_symbol, volno_symbol, eny_symbol))
        #blokace eny volne pozice vlevo+vpravo
        seznam_priorit[4].append(overeni_pole_3_podminky(i, -1, pole, -2, i, i+1, i+2, volno_symbol, eny_symbol, volno_symbol))
        seznam_priorit[4].append(overeni_pole_3_podminky(i, 1, pole, 0, i-2, i-1, i, volno_symbol, eny_symbol, volno_symbol))
        #oblozeni me volne pozice vlevo+vpravo
        seznam_priorit[5].append(overeni_pole_4_podminky(i, 0, pole, -2, i-1, i, i+1, i+2, volno_symbol, volno_symbol, ai_symbol, volno_symbol))
        seznam_priorit[5].append(overeni_pole_4_podminky(i, 1, pole, -1, i-2, i-1, i, i+1, volno_symbol, ai_symbol, volno_symbol, volno_symbol))
        #blokace eny dvoupozice vlevo+vpravo
        seznam_priorit[6].append(overeni_pole_3_podminky(i, -1, pole, -2, i, i+1, i+2, volno_symbol, eny_symbol, eny_symbol))
        seznam_priorit[6].append(overeni_pole_3_podminky(i, 1, pole, 1, i-2, i-1, i, eny_symbol, eny_symbol, volno_symbol))
        #blokace eny mezy kozy
        seznam_priorit[6].append(overeni_pole_3_podminky(i, 0, pole, -1, i-1, i, i+1, eny_symbol, volno_symbol, eny_symbol))
        #ai hrani mezy kozy
        seznam_priorit[7].append(overeni_pole_3_podminky(i, 0, pole, -1, i-1, i, i+1, ai_symbol, volno_symbol, ai_symbol))
        #dokonceni me dvoupozice vlevo+vpravo
        seznam_priorit[7].append(overeni_pole_3_podminky(i, -1, pole, -2, i, i+1, i+2, volno_symbol, ai_symbol, ai_symbol))
        seznam_priorit[7].append(overeni_pole_3_podminky(i, 1, pole, +1, i-2, i-1, i, ai_symbol, ai_symbol, volno_symbol))

    #Odstraneni None pozic zpusobenych nepodminenym volanim overovacich funkci
    for m in range(len(seznam_priorit)):
        while  None in seznam_priorit[m]:
            seznam_priorit[m].remove(None)

    #Na zaver vyberu pozice s nejvetsi prioritou a hraju tam
    for k in range(len(seznam_priorit)-1,-1,-1):
        if len(seznam_priorit[k]) > 0:
            return random.choice(seznam_priorit[k])

def tah_pocitace(hraci_pole, hrany_symbol):
    #Snad spravne napsana funkce, ktera bude volana podradnym kapitalistickym kodem nasich
    #koucu :-)
    #Tato funkce prijimace neopracovane pole a symbol, kterym ma hrat
    #Vraci opracovane pole
    kam_s_nim = alt_ai(hraci_pole, hrany_symbol)
    if kam_s_nim == None:
        return hraci_pole
    else:
        return hraci_pole[:kam_s_nim] + hrany_symbol + hraci_pole[kam_s_nim+1:]



#print(tah_pocitace("-----o-o---xx", "o"))
