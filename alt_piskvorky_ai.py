import random

def alt_piskvorky_ai(pole, ai_symbol, eny_symbol, volno_symbol):
    seznam_priorizovane_pole = []
    seznam_sedmicek = []
    seznam_sestek = []
    seznam_petek = []
    seznam_ctyrek = []
    seznam_trojek = []
    seznam_dvojek = []
    seznam_jednicek = []

    for i in range(0, len(pole)):#nejdriv testuju priority 1 a dva, tj. volne pozice resp. hratelne 3. poz od kraje
        seznam_priorizovane_pole.append(0)#jen se ujistim, ze pole bude mit tolik znaku, kolik potrebuji,
        #a ze zadny nebude mit prioritu > 0
        if pole[i] == volno_symbol:
            seznam_priorizovane_pole[i] = 1
        if pole[i-2]==volno_symbol and pole[i-1]==volno_symbol and i==2 and pole[i+1]==volno_symbol and pole[i+2]!=eny_symbol:
            seznam_priorizovane_pole[i] = 2
        if i>1:
            if pole[i-2]!=eny_symbol and pole[i-1]==volno_symbol and i==len(pole)-3 and pole[i+1]==volno_symbol and pole[i+1]==volno_symbol:
                seznam_priorizovane_pole[i] = 2

        #ted jdu na prior. 3 tj. prilozeni k me pozici, vyroba 1/2diry
        if i>1 and i<len(pole)-1:#samostatna pozice s mojim symbolem vlevo
            if pole[i]==volno_symbol and pole[i+1]==volno_symbol and pole[i-2]==volno_symbol and pole[i-1]==ai_symbol:
                seznam_priorizovane_pole[i] = 3
        if i>0 and i<len(pole)-2:#samostatna pozice s mojim symbolem vpravo
            if pole[i-1]==volno_symbol and pole[i]==volno_symbol and pole[i+1]==ai_symbol and pole[i+2]==volno_symbol:
                seznam_priorizovane_pole[i] = 3
        #vpravo od pozice se da hrat
        if i>0 and i<len(pole)-1:
            if pole[i-1]==ai_symbol and pole[i]==volno_symbol and pole[i+1]==volno_symbol:
                seznam_priorizovane_pole[i] = 3
        #vlevo od pozice se da hrat
        if i>1 and i<len(pole)-1:
            if pole[i-1]==volno_symbol and pole[i]==volno_symbol and pole[i+1]==ai_symbol:
                seznam_priorizovane_pole[i] = 3
        #ted jdu vyrobyt jednodiru od me pozice vpravo
        if i>1 and i<len(pole):
            if pole[i-2]==ai_symbol and pole[i-1]==volno_symbol and pole[i]==volno_symbol:
                seznam_priorizovane_pole[i] = 3
        #ted jdu vyrobyt jednodiru od me pozice vlevo
        if i<len(pole)-2:
            if pole[i]==volno_symbol and pole[i+1]==volno_symbol and pole[i+2]==ai_symbol:
                seznam_priorizovane_pole[i] = 3

        #Vyroba dvoudiry od eny pozice vlevo
        if i>0 and i<len(pole)-3:
            if pole[i-1]!=eny_symbol and pole[i]==volno_symbol and pole[i+1]==volno_symbol and pole[i+2]==volno_symbol and pole[i+3]==eny_symbol:
                seznam_priorizovane_pole[i] = 3
        #Vyroba dvoudiry od eny pozice vpravo
        if i>3 and i<len(pole)-1:
            if pole[i+1]!=eny_symbol and pole[i]==volno_symbol and pole[i-1]==volno_symbol and pole[i-2]==volno_symbol and pole[i-3]==eny_symbol:
                seznam_priorizovane_pole[i] = 3

        #blokace eny volne pozice vlevo
        if i<len(pole)-2:
            if pole[i]==volno_symbol and pole[i+1]==eny_symbol and pole[i+2]==volno_symbol:
                seznam_priorizovane_pole[i] = 4
        #blokace eny volne pozice vlevo
        if i>1 and i<len(pole):
            if pole[i-2]==volno_symbol and pole[i-1]==eny_symbol and pole[i]==volno_symbol:
                seznam_priorizovane_pole[i] = 4

        #oblozeni me volne pozice vlevo
        if i>0 and i<len(pole)-2:
            if pole[i-1]==volno_symbol and pole[i]==volno_symbol and pole[i+1]==ai_symbol and pole[i+2]==volno_symbol:
                seznam_priorizovane_pole[i] = 5
        #oblozeni me volne pozice vpravo
        if i>1 and i<len(pole)-1:
            if pole[i-2]==volno_symbol and pole[i-1]==ai_symbol and pole[i]==volno_symbol and pole[i+1]==volno_symbol:
                seznam_priorizovane_pole[i] = 5

        #blokace eny dvoupozice vlevo
        if i<len(pole)-2:
            if pole[i]==volno_symbol and pole[i+1]==eny_symbol and pole[i+2]==eny_symbol:
                seznam_priorizovane_pole[i] = 6
        #blokace eny dvoupozice vpravo
        if i>1:
            if pole[i-2]==eny_symbol and pole[i-1]==eny_symbol and pole[i]==volno_symbol:
                seznam_priorizovane_pole[i] = 6

        #blokace eny mezy kozy
        if i>0 and i<len(pole):
            if pole[i-1]==eny_symbol and pole[i]==volno_symbol and pole[i+1]==eny_symbol:
                seznam_priorizovane_pole[i] = 6

        #Moje hrani mezy kozy
        if i>0 and i<len(pole):
            if pole[i-1]==ai_symbol and pole[i]==volno_symbol and pole[i+1]==ai_symbol:
                seznam_priorizovane_pole[i] = 7

        #dokonceni me dvoupozice vlevo
        if i<len(pole)-2:
            if pole[i]==volno_symbol and pole[i+1]==ai_symbol and pole[i+2]==ai_symbol:
                seznam_priorizovane_pole[i] = 7
        #dokonceni me dvoupozice vpravo
        if i>1:
            if pole[i-2]==ai_symbol and pole[i-1]==ai_symbol and pole[i]==volno_symbol:
                seznam_priorizovane_pole[i] = 7

        #to je tady nakonec proto, abych na zabranych mistech mel nuly...
        if pole[i]==ai_symbol or pole[i]==eny_symbol:
            seznam_priorizovane_pole[i] = 0

    for j in range(0,len(seznam_priorizovane_pole)):
        if seznam_priorizovane_pole[j]==7:
            seznam_sedmicek.append(j)
        elif seznam_priorizovane_pole[j]==6:
            seznam_sestek.append(j)
        elif seznam_priorizovane_pole[j]==5:
            seznam_petek.append(j)
        elif seznam_priorizovane_pole[j]==4:
            seznam_ctyrek.append(j)
        elif seznam_priorizovane_pole[j]==3:
            seznam_trojek.append(j)
        elif seznam_priorizovane_pole[j]==2:
            seznam_dvojek.append(j)
        elif seznam_priorizovane_pole[j]==1:
            seznam_jednicek.append(j)

    if len(seznam_sedmicek)>0:
        return random.choice(seznam_sedmicek)
    elif len(seznam_sestek)>0:
        return random.choice(seznam_sestek)
    elif len(seznam_petek)>0:
        return random.choice(seznam_petek)
    elif len(seznam_ctyrek)>0:
        return random.choice(seznam_ctyrek)
    elif len(seznam_trojek)>0:
        return random.choice(seznam_trojek)
    elif len(seznam_dvojek)>0:
        return random.choice(seznam_dvojek)
    elif len(seznam_jednicek)>0:
        return random.choice(seznam_jednicek)

print(alt_piskvorky_ai("--oo----x-xx--o-o--", "o", "x", "-"))
