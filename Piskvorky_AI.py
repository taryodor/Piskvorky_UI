import random #Potrebuji pro random.choice

def test_dve_vedle_sebe_hrat_vlevo(pole, zajmovy_symbol):
    #Test pole na pritomnost dvou danych symbolu, ktere maji vpravo hratelnou pozici
    #U ENY doupozic je jedno, jestli jsou hratelen z obou stran, protoze to znamena prohru...
    global tah_rozhodnut
    for i in range(1, len(pole) - 1):
        if pole[i - 1] == '-' and pole[i] == zajmovy_symbol and pole[i + 1] == zajmovy_symbol:
            tah_rozhodnut = True
            return i - 1

def test_dve_vedle_sebe_hrat_vpravo(pole, zajmovy_symbol):
    #Test pole na pritomnost dvou danych symbolu, ktere maji vpravo hratelnou pozici
    #U ENY doupozic je jedno, jestli jsou hratelen z obou stran, protoze to znamena prohru...
    global tah_rozhodnut
    for i in range(0, len(pole) - 2):
        if pole[i] == zajmovy_symbol and pole[i + 1] == zajmovy_symbol and pole[i + 2] == "-":
            tah_rozhodnut = True
            return i + 2

def test_mezy_kozy(pole, zajmovy_symbol):
    #Test pole na pritomnost dvou zajmovych symbolu ob mezeru
    global tah_rozhodnut
    i = 0
    while i < len(pole) - 2:
        if pole[i] == zajmovy_symbol and pole[i + 2] == zajmovy_symbol and pole[i + 1] == "-":
            tah_rozhodnut = True
            return i + 1
            break
        i = i + 1

def test_samostatne_symboly(pole, zajmovy_symbol):
    #Test na zajmove symboly, ktery ma z obou stran volno
    lokalni_seznam = []
    for i in range(1,len(pole) - 1):
        if pole[i] == zajmovy_symbol and pole[i - 1] == "-" and pole[i + 1] == "-":
            lokalni_seznam.append(i)
    return lokalni_seznam

def test_samostatne_symboly_hrat_vpravo(pole, zajmovy_symbol):
    #Test na zajmovy symbol, ktery ma vpravo dve mezery a vlevo jednu
    lokalni_seznam = []
    for i in range(1,len(pole) - 2):
        if pole[i] == zajmovy_symbol and pole[i - 1] == "-" and pole[i + 1] == "-" and pole[i + 2] == "-":
            lokalni_seznam.append(i)
    return lokalni_seznam

def test_samostatne_symboly_hrat_vlevo(pole, zajmovy_symbol):
    #Test na zajmovy symbol, ktery ma vlevo dve mezery a vpravo jednu
    lokalni_seznam = []
    for i in range(2,len(pole) - 1):
        if pole[i] == zajmovy_symbol and pole[i - 2] == "-" and pole[i - 1] == "-" and pole[i + 1] == "-":
            lokalni_seznam.append(i)
    return lokalni_seznam

def test_levostrane_hratelnych_dvouder(pole, zajmovy_symbol, eny_symbol):
    #Test na detekci vhodnych podminek k hrani dvoudiry ohranicenou zprava
    lokalni_seznam = []
    for i in range(1, len(pole) - 4):
        if pole[i + 3] == eny_symbol and pole[i + 2] == "-" and pole[i + 1] == "-" and pole[i] == "-" and pole[i - 1] == "-":
            lokalni_seznam.append(i)
    return lokalni_seznam

def test_pravostrane_hratelnych_dvouder(pole, zajmovy_symbol, eny_symbol):
    #Test na detekci vhodnych podminek k hrani dvoudiry ohranicenou zleva
    lokalni_seznam = []
    for i in range(3, len(pole) - 2):
        if pole[i - 3] == eny_symbol and pole[i - 2] == "-" and pole[i - 1] == "-" and pole[i] == "-" and pole[i + 1] == "-":
            lokalni_seznam.append(i)
    return lokalni_seznam

def test_na_typ_pozice(pole, zajmovy_symbol):
    #Testovani kazde pozice pole na pritomnost zajmoveho symbolu
    lokalni_seznam = []
    for i in range(0,len(pole)):
        if pole[i] == zajmovy_symbol:
            lokalni_seznam.append(i)
    return lokalni_seznam

def tah_ai(pole, symbol_ai):
    # je to takovy Identify Friend-Foe
    if symbol_ai == "x":
        symbol_eny = "o"
    elif symbol_ai == "o":
        symbol_eny = "x"
    volno_symbol = "-"
    #AI pro tah pocitace
    #zacneme definicema seznamu
    seznam_hranych_ai_pozic = []
    #Seznam, kam ukladam vsechny pozice s ai symbolem
    seznam_hranych_eny_pozic = []
    #Seznam, kam ukladam vsechny pozice s eny symbolem
    seznam_volnych_pozic = []
    #Seznam, kam ukladam vsechny volne pozice
    pokusny = []

    seznam_oboustranych_ai_pozic_hrat_vlevo = []
    #Seznam, kam ukladam prioritne hrane pozice s ai symbolem, kterej maji vlevo dve volna a vpravo jedno
    #tj. kdyz budu hrat vlevo od nich, nemohu prohrat
    seznam_oboustranych_ai_pozic_hrat_vpravo = []
    #Stejne jako vyse, ale hrajeme vpravo

    seznam_oboustranych_eny_pozic_hrat_vlevo = []
    seznam_oboustranych_eny_pozic_hrat_vpravo = []
    seznam_levostrane_hratelnych_ai_dvouder = []
    seznam_pravostrane_hratelnych_ai_dvouder = []
    #Hratelne dvoudiry jsou mista, kam se vyplati utocit.
    #Da se prodpokladat, ze s takovym tahem bude mit jednodussi programek starosti

    pozice_ai_tahu = 0
    #!Potrebuji vubec toto?
    global tah_rozhodnut
    #Definice veledulezite globalni boolean promenne
    tah_rozhodnut = False

    if len(pole) < 5:
        return None
        #raise ValueError("Takhle kratke hraci pole si strcte do muslimske ctvrti.")
        #Toto je, to by neproslo hodnocenim koucu
        #Nema smysl se otravovat s prilis kratkym polem. Howgh. pozn. zjisti si spelling Howgh.
    if symbol_ai not in pole and symbol_eny not in pole:
        #kontrola, ze hraci pole je prazdne
        if len(pole) == 5:
	    #Jelikoz mam spatne tuto podminku, vychazeli mi divne veci.
            #Predelej podminku a bude se menit i minimalni pouzitela delka pole...
            tah_rozhodnut = True
            return 2
        else:
            tah_rozhodnut = True
            return random.choice((2, len(pole) - 3))
            #2 tj. treti od zacatku a len-4 tj. treti od konce
            #kdyz bude pole moc kratke na poradne hrani, neva stale je toto nejlepsi volba

    #ulozeni hranych tahu pro dalsi vyhodnoceni,
    seznam_levostrane_hratelnych_ai_dvouder = test_levostrane_hratelnych_dvouder(pole, symbol_ai, symbol_eny)
    seznam_pravostrane_hratelnych_ai_dvouder = test_pravostrane_hratelnych_dvouder(pole, symbol_ai, symbol_eny)
    seznam_oboustranych_ai_pozic_hrat_vlevo = test_samostatne_symboly_hrat_vlevo(pole, symbol_ai)
    seznam_oboustranych_ai_pozic_hrat_vpravo = test_samostatne_symboly_hrat_vpravo(pole, symbol_ai)
    seznam_oboustranych_eny_pozic_hrat_vlevo = test_samostatne_symboly_hrat_vlevo(pole, symbol_eny)
    seznam_oboustranych_eny_pozic_hrat_vpravo = test_samostatne_symboly_hrat_vpravo(pole, symbol_eny)
    seznam_hranych_ai_pozic = test_na_typ_pozice(pole, symbol_ai)
    seznam_hranych_eny_pozic = test_na_typ_pozice(pole, symbol_eny)
    seznam_volnych_pozic = test_na_typ_pozice(pole, "-")

    #Tady jdeme testovat, zdali nejsme jen jeden tah od vyhry, resp. prohry
    #Mezy kozy AI - ma prednost, chci spis vyhrat, nez oddalit prohru
    if len(seznam_hranych_ai_pozic) > 1 and tah_rozhodnut == False:
        pozice_ai_tahu = test_mezy_kozy(pole, symbol_ai)
        if tah_rozhodnut == True:
            return pozice_ai_tahu

    if len(seznam_hranych_ai_pozic) > 1 and tah_rozhodnut == False:
        pozice_ai_tahu = test_dve_vedle_sebe_hrat_vlevo(pole, symbol_ai)
        if tah_rozhodnut == True:
            return pozice_ai_tahu
    if len(seznam_hranych_ai_pozic) > 1 and tah_rozhodnut == False:
        pozice_ai_tahu = test_dve_vedle_sebe_hrat_vpravo(pole, symbol_ai)
        if tah_rozhodnut == True:
            return pozice_ai_tahu

    #Mezy kozy ENY - odvraceni katastrofy
    if len(seznam_hranych_eny_pozic) > 1 and tah_rozhodnut == False:
        pozice_ai_tahu = test_mezy_kozy(pole, symbol_eny)
        if tah_rozhodnut == True:
            return pozice_ai_tahu

    #NAsleduje test na pritomnost a nasledne odehrani eny dvoupozic
    if len(seznam_hranych_eny_pozic) > 1 and tah_rozhodnut == False:
        pozice_ai_tahu = test_dve_vedle_sebe_hrat_vlevo(pole, symbol_eny)
        if tah_rozhodnut == True:
            return pozice_ai_tahu
    if len(seznam_hranych_eny_pozic) > 1 and tah_rozhodnut == False:
        pozice_ai_tahu = test_dve_vedle_sebe_hrat_vpravo(pole, symbol_eny)
        if tah_rozhodnut == True:
            return pozice_ai_tahu

#jdeme na odpoved na prvni tah na krajni pozici
    if len(seznam_hranych_eny_pozic) == 1 and len(seznam_hranych_ai_pozic) == 0:
        #eny hraje na 1./2. pozici
        if seznam_hranych_eny_pozic[0] == 0 or seznam_hranych_eny_pozic[0] == 1:
            pozice_ai_tahu = seznam_hranych_eny_pozic[0] + 2
            tah_rozhodnut = True
            return pozice_ai_tahu
        if seznam_hranych_eny_pozic[0] == len(pole) - 1 or seznam_hranych_eny_pozic[0] == len(pole) - 2:
            pozice_ai_tahu = seznam_hranych_eny_pozic[0] - 2
            tah_rozhodnut = True
            return pozice_ai_tahu
        #eny hraje na 3./4.pozici
        if seznam_hranych_eny_pozic[0] == 2 or seznam_hranych_eny_pozic[0] == 3:
            pozice_ai_tahu = seznam_hranych_eny_pozic[0] + 1
            tah_rozhodnut = True
            return pozice_ai_tahu
        if seznam_hranych_eny_pozic[0] == len(pole) - 3 or seznam_hranych_eny_pozic[0] == len(pole) - 4:
            pozice_ai_tahu = seznam_hranych_eny_pozic[0] - 1
            tah_rozhodnut = True
            return pozice_ai_tahu
    #Neni vybrana zadna strategie, volim nahodnou pozici
        #Pokud mam nekde osamoceny znak, hraju jej

    if len(seznam_pravostrane_hratelnych_ai_dvouder) > 0:
        return random.choice(seznam_pravostrane_hratelnych_ai_dvouder)
    elif len(seznam_levostrane_hratelnych_ai_dvouder) > 0:
        return random.choice(seznam_levostrane_hratelnych_ai_dvouder)
    elif len(seznam_oboustranych_eny_pozic_hrat_vlevo) > 0:
        return random.choice(seznam_oboustranych_eny_pozic_hrat_vlevo) - 1
    elif len(seznam_oboustranych_eny_pozic_hrat_vpravo) > 0:
        return random.choice(seznam_oboustranych_eny_pozic_hrat_vpravo) + 1
    elif len(seznam_volnych_pozic) > 0:
        return random.choice(seznam_volnych_pozic)
    else:
        return None
        #raise ValueError("Neni kam hrat, melouni.")
        #Toto ne, to by neproslo testem koucu
    #Toto je jen pro pripad, ze progrma nenajde misto, kam by mel hrat, tak to vrzne na nahodnou volnou pozici

def tah_pocitace(hraci_pole, hrany_symbol):
    #Tato funkce prijimace neopracovane pole a symbol, kterym ma hrat
    #Vraci opracovane pole
    kam_s_nim = tah_ai(hraci_pole, hrany_symbol)
    if kam_s_nim == None:
        return hraci_pole
    else:
        return hraci_pole[:kam_s_nim] + hrany_symbol + hraci_pole[kam_s_nim+1:]


#print("tah bude: ", tah_pocitace("------------x-x---oo--o---o-o---", "o"))
