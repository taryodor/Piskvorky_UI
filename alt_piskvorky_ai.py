import random

def alt_piskvorky_ai(pole, ai_symbol, eny_symbol, volno_symbol):
    seznam_priorit = []
    for i in range(8):
        seznam_priorit.append([])

    for i in range(0, len(pole)):#nejdriv testuju priority 1 a dva, tj. volne pozice resp. hratelne 3. poz od kraje
        #jen se ujistim, ze pole bude mit tolik znaku, kolik potrebuji,
        #seznam_priorit[0].append(i)
        if pole[i] == volno_symbol:
            seznam_priorit[1].append(i)
        if pole[i-2] == volno_symbol and pole[i-1]==volno_symbol and i==2 and pole[i+1]==volno_symbol and pole[i+2]!=eny_symbol:
            seznam_priorit[2].append(i)
        if i>1:
            if pole[i-2]!=eny_symbol and pole[i-1]==volno_symbol and i==len(pole)-3 and pole[i+1]==volno_symbol and pole[i+1]==volno_symbol:
                seznam_priorit[2].append(i)

        #ted jdu na prior. 3 tj. prilozeni k me pozici, vyroba 1/2diry
        if i>1 and i<len(pole)-1:#samostatna pozice s mojim symbolem vlevo
            if pole[i]==volno_symbol and pole[i+1]==volno_symbol and pole[i-2]==volno_symbol and pole[i-1]==ai_symbol:
                seznam_priorit[3].append(i)
        if i>0 and i<len(pole)-2:#samostatna pozice s mojim symbolem vpravo
            if pole[i-1]==volno_symbol and pole[i]==volno_symbol and pole[i+1]==ai_symbol and pole[i+2]==volno_symbol:
                seznam_priorit[3].append(i)
        #vpravo od pozice se da hrat
        if i>0 and i<len(pole)-1:
            if pole[i-1]==ai_symbol and pole[i]==volno_symbol and pole[i+1]==volno_symbol:
                seznam_priorit[3].append(i)
        #vlevo od pozice se da hrat
        if i>1 and i<len(pole)-1:
            if pole[i-1]==volno_symbol and pole[i]==volno_symbol and pole[i+1]==ai_symbol:
                seznam_priorit[3].append(i)
        #ted jdu vyrobyt jednodiru od me pozice vpravo
        if i>1 and i<len(pole):
            if pole[i-2]==ai_symbol and pole[i-1]==volno_symbol and pole[i]==volno_symbol:
                seznam_priorit[3].append(i)
        #ted jdu vyrobyt jednodiru od me pozice vlevo
        if i<len(pole)-2:
            if pole[i]==volno_symbol and pole[i+1]==volno_symbol and pole[i+2]==ai_symbol:
                seznam_priorit[3].append(i)
        #Vyroba dvoudiry od eny pozice vlevo
        if i>0 and i<len(pole)-3:
            if pole[i-1]!=eny_symbol and pole[i]==volno_symbol and pole[i+1]==volno_symbol and pole[i+2]==volno_symbol and pole[i+3]==eny_symbol:
                seznam_priorit[3].append(i)
        #Vyroba dvoudiry od eny pozice vpravo
        if i>3 and i<len(pole)-1:
            if pole[i+1]!=eny_symbol and pole[i]==volno_symbol and pole[i-1]==volno_symbol and pole[i-2]==volno_symbol and pole[i-3]==eny_symbol:
                seznam_priorit[3].append(i)

        #blokace eny volne pozice vlevo
        if i<len(pole)-2:
            if pole[i]==volno_symbol and pole[i+1]==eny_symbol and pole[i+2]==volno_symbol:
                seznam_priorit[4].append(i)
        #blokace eny volne pozice vlevo
        if i>1 and i<len(pole):
            if pole[i-2]==volno_symbol and pole[i-1]==eny_symbol and pole[i]==volno_symbol:
                seznam_priorit[4].append(i)

        #oblozeni me volne pozice vlevo
        if i>0 and i<len(pole)-2:
            if pole[i-1]==volno_symbol and pole[i]==volno_symbol and pole[i+1]==ai_symbol and pole[i+2]==volno_symbol:
                seznam_priorit[5].append(i)
        #oblozeni me volne pozice vpravo
        if i>1 and i<len(pole)-1:
            if pole[i-2]==volno_symbol and pole[i-1]==ai_symbol and pole[i]==volno_symbol and pole[i+1]==volno_symbol:
                seznam_priorit[5].append(i)

        #blokace eny dvoupozice vlevo
        if i<len(pole)-2:
            if pole[i]==volno_symbol and pole[i+1]==eny_symbol and pole[i+2]==eny_symbol:
                seznam_priorit[6].append(i)
        #blokace eny dvoupozice vpravo
        if i>1:
            if pole[i-2]==eny_symbol and pole[i-1]==eny_symbol and pole[i]==volno_symbol:
                seznam_priorit[6].append(i)
        #blokace eny mezy kozy
        if i>0 and i<len(pole):
            if pole[i-1]==eny_symbol and pole[i]==volno_symbol and pole[i+1]==eny_symbol:
                seznam_priorit[6].append(i)

        #Moje hrani mezy kozy
        if i>0 and i<len(pole):
            if pole[i-1]==ai_symbol and pole[i]==volno_symbol and pole[i+1]==ai_symbol:
                seznam_priorit[7].append(i)
        #dokonceni me dvoupozice vlevo
        if i<len(pole)-2:
            if pole[i]==volno_symbol and pole[i+1]==ai_symbol and pole[i+2]==ai_symbol:
                seznam_priorit[7].append(i)
        #dokonceni me dvoupozice vpravo
        if i>1:
            if pole[i-2]==ai_symbol and pole[i-1]==ai_symbol and pole[i]==volno_symbol:
                seznam_priorit[7].append(i)

    #Tak a na zaver vyberu pozice s nejvetsi prioritou a hraju tam
    for k in range(len(seznam_priorit)-1,-1,-1):
        if len(seznam_priorit[k]) > 0:
            return random.choice(seznam_priorit[k])

print(alt_piskvorky_ai("--oo----x-xx--o-o--", "o", "x", "-"))
