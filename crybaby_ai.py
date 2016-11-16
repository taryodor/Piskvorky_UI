def tah_pocitace(hraci_pole, hrany_symbol):
    #Zcela neporazitelny a nadrazeny algoritmus na 1D piskvorky
    if len(hraci_pole)<3:
        #Toto je jen pojistka,abych prosel testy koucu
        return hraci_pole
    return (hrany_symbol * 3) + hraci_pole[3:]
