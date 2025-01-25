from crud_auto import *

toon_functies_auto()
keuze = input("Geef je keuze: ")
while keuze.lower() != "stop":
    if keuze == "1":
        print(tabulate(data, headers=headers, tablefmt='grid'))
    elif keuze == "2":
        nieuw_voertuig_toevoegen()
    elif keuze == "3":
        verwijder_voertuig()
    elif keuze == "4":
        sorteer_voertuigen_op_huurprijs_opl()
    elif keuze == "5":
        toon_voertuigen_met_x_brandstof()
    elif keuze == "6":
        pas_huurprijs_aan()
    elif keuze == "7":
        schrijf_data_weg()

    toon_functies_auto()
    keuze = input("Geef je keuze: ")


