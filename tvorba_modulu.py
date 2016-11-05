"""if len(seznam_hranych_ai_pozic) > 1:
#Check na insta-win mezi kozy
check_mezy_kozy(seznam_hranych_ai_pozic, symbol_ai)

    j = 0
    while seznam_hranych_ai_pozic[j] < len(pole) - 2 :
        #nepotrebuji mezi-kozy check u hodnot na kraji pole
        if pole[seznam_hranych_ai_pozic[j] + 2] == symbol_ai and pole[seznam_hranych_ai_pozic[j]+1] == "-":
            #check, jestli ob jednu prazdnou hodnotu neni stejne zadani - tj. mezi kozy
            pozice_ai_tahu = seznam_hranych_ai_pozic[j] + 1
            #jestlize je, tak to vrhnu presne mezi kozy, abych vyhral
            return pozice_ai_tahu
            break
        j = j + 1


if len(seznam_hranych_ai_pozic) > 1:
#Check na insta-win mezi kozy
    j = 0
    while seznam_hranych_ai_pozic[j] < len(pole) - 2 and j < len(pole) - 2:
        #nepotrebuji mezi-kozy check u hodnot na kraji pole
        if pole[seznam_hranych_ai_pozic[j] + 2] == symbol_ai and pole[seznam_hranych_ai_pozic[j] + 1 ] == "-":
            #check, jestli ob jednu prazdnou hodnotu neni stejne zadani - tj. mezi kozy
            pozice_ai_tahu = seznam_hranych_ai_pozic[j] + 1
            #jestlize je, tak to vrhnu presne mezi kozy, abych vyhral
            return pozice_ai_tahu
            break
        j = j + 1

#Puvodni
def check_mezy_kozy(seznam_hranych_who_pozic, symbol_who):
    localni_promenna = 0
    while seznam_hranych_who_pozic[localni_promenna] < len(pole) - 2:
        if pole[seznam_hranych_who_pozic[localni_promenna] + 2] == symbol_who and pole[seznam_hranych_who_pozic[localni_promenna] + 1] == "-":
            vracena_hodnota = seznam_hranych_who_pozic[localni_promenna] + 1
            break
        localni_promenna = localni_promenna + 1
    return vracena_hodnota
"""
#Upravena
def check_mezy_kozy(seznam_hranych_who_pozic, symbol_who):
    localni_promenna = 0
    while localni_promenna < len(pole) - 2:
        if pole[localni_promenna] == symbol_who and pole[localni_promenna + 2] == symbol_who and pole[localni_promenna] + 1] == "-":
            vracena_hodnota = pole[localni_promenna] + 1
            global tah_rozhodnut
            tah_rozhodnut = True
            break
        localni_promenna = localni_promenna + 1
    return vracena_hodnota
