from crud_bel_bieren import *

def toon_functies(): #kan ook in file die geïmporteerd wordt
    print("1: toon alle bieren")
    print("2: voeg bbier toe")
    print("3: verwijder bier")
    print("4: sorteer op alcoholpercentage")
    print("5: toon sterke bieren")
    print("6: pas percentage aan")
    print("7: update data")

toon_functies()
keuze = input("Geef je keuze: ")
while keuze.lower() != "stop":
    if keuze == "1":
        print(tabulate(data, headers=headers, tablefmt='grid'))
    elif keuze == "2":
        nieuw_bier_toevoegen()
    elif keuze == "3":
        verwijder_bier()
    elif keuze == "4":
        sorteer_bieren_op_percentage()
    elif keuze == "5":
        toon_bieren_boven_8perc()
    elif keuze == "6":
        pas_alcoholpercentage_aan()
    elif keuze == "7":
        schrijf_data_weg()

    keuze = input("Geef je keuze: ")


