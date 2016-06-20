import random
#super implementacja rzutu kostka, zeby tylko ruszylo
def rzut():
    return random.randrange(6)+1

def runda():
    wynik_gracza= rzut() + rzut()
    wynik_cpu= rzut() + rzut()
    return (wynik_gracza, wynik_cpu)

def gra():
    #na poczatku gry nikt nie ma punktow
    suma_gracza= 0
    suma_cpu= 0
    #range(3) = 0,1,2
    for i in range(3):
        g, c= runda()
        suma_gracza=suma_gracza+g
        suma_cpu=suma_cpu+c
    if suma_gracza > suma_cpu: return "Gracz"
    if suma_gracza < suma_cpu: return "CPU"
    if suma_gracza == suma_cpu: return "Remis"

def main():
    wynik_glowny=gra()
    print("Wynik gry: %s" % wynik_glowny)
    if wynik_glowny == "Remis":
        wynik_dogrywki= gra()
        while wynik_dogrywki == "Remis":
            wynik_dogrywki= gra()
        print("Dogrywka: %s" % wynik_dogrywki)

main()

