from crud_gitaren import *

toon_functies_gitaren()
keuze = input("Geef je keuze: ")
while keuze.lower() != "stop":
    if keuze == "1":
        print(tabulate(data, headers=headers, tablefmt='grid'))
    elif keuze == "2":
        nieuwe_gitaar_toevoegen()
    elif keuze == "3":
        verwijder_gitaar()
    elif keuze == "4":
        sorteer_vintage_gitaren_op_bouwjaar_opl()
    elif keuze == "5":
        toon_vintage_gitaren_type_x()
    elif keuze == "6":
        pas_staat_aan()
    elif keuze == "7":
        schrijf_data_weg()

    toon_functies_gitaren()
    keuze = input("Geef je keuze: ")


