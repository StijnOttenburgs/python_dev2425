"""1.	Lees alle data
2.	Voeg een voortuig toe
3.	Verwijder voertuig op basis van id
4.	Pas huurprijs aan
5.	Sorteer op basis van huurprijs a-z laagste eerst
6.	Filter alle voertuigen met brandstof x
7.	Update data
8.	Schrijf een controller in een while"""


import csv
from tabulate import tabulate

# Vervang 'voertuigen.csv' door het pad naar jouw CSV-bestand
bestand = 'voertuigen.csv'

# Maak een lege lijst voor de data en headers
data = []
headers = []

# Open het CSV-bestand en lees het in
with open(bestand, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)

    try:
        # Lees de header (kolomnamen) in
        headers = next(reader)
    except StopIteration:
        # Als het bestand leeg is, geef een melding en ga verder
        print("Het CSV-bestand is leeg. Voeg een nieuw voertuig toe om te beginnen.")

    # Voeg de bestaande rijen toe aan de data-lijst
    for row in reader:
        data.append(row)

# Toon de bestaande gegevens, als die er zijn
if data:
    print("Huidige lijst met voertuigen:")
    print(tabulate(data, headers=headers, tablefmt='fancy_grid'))
else:
    print("Er zijn nog geen gegevens van voertuigen beschikbaar.")

# Als het bestand leeg is, vraag de headers aan de gebruiker
if not headers:
    aantal_kolommen = int(input("Het bestand is leeg. Hoeveel kolommen wil je toevoegen? "))
    for i in range(aantal_kolommen):
        kolomnaam = input(f"Voer de naam van kolom {i + 1} in: ")
        headers.append(kolomnaam)
        
# Functie om een nieuw voertuig toe te voegen
def nieuw_voertuig_toevoegen():
    nieuw_voertuig = []
    print("\nVoer de gegevens in voor een nieuw voertuig:")
    for header in headers:
        waarde = input(f"Voer {header} in: ").capitalize()
        nieuw_voertuig.append(waarde)

    # Voeg het nieuwe voertuig toe aan de data
    data.append(nieuw_voertuig)

    # Toon de bijgewerkte gegevens
    print("\nBijgewerkte lijst met voertuigen:")
    print(tabulate(data, headers=headers, tablefmt='grid'))
    
# Functie om een voertuig te verwijderen
def verwijder_voertuig():
    print("\nHuidige lijst met voertuigen:")
    print(tabulate(data, headers=headers, tablefmt='grid'))

    # Kies op basis van een kolom om een voertuig te verwijderen
    zoekterm = input(f"Voer de id van het voertuig dat je wenst te verwijderen: ")

    # Zoek naar de juiste rij om te verwijderen
    index_te_verwijderen = None
    for i, row in enumerate(data):
        if zoekterm in row:  # We zoeken naar een rij die de zoekterm bevat
            index_te_verwijderen = i
            break

    if index_te_verwijderen is not None:
        print(f"voertuig gevonden en verwijderd: {data[index_te_verwijderen]}")
        del data[index_te_verwijderen]  # Verwijder het voertuig
    else:
        print("Geen voertuig gevonden met de opgegeven waarde.")

    # Toon de bijgewerkte gegevens
    print("\nBijgewerkte lijst met voertuigen:")
    print(tabulate(data, headers=headers, tablefmt='grid'))
    
# Functie om de huurprijs van een voertuig aan te passen
def pas_huurprijs_aan():
    print("\nHuidige lijst met voertuigen:")
    print(tabulate(data, headers=headers, tablefmt='grid'))

    # Vraag de naam van het voertuig wiens huurprijs je wilt aanpassen
    zoekterm = input(f"Voer de id in van het voertuig waarvan je het huurprijs wilt aanpassen: ")

    # Zoek het voertuig
    index_te_aanpassen = None
    for i, row in enumerate(data):
        if zoekterm in row:  # We zoeken naar een rij die de zoekterm bevat
            index_te_aanpassen = i
            break

    if index_te_aanpassen is not None:
        # Vraag het nieuwe huurprijs
        nieuw_huurprijs = input("Voer het nieuwe huurprijs in: ")

        # Neem aan dat de huurprijs-kolom de laatste kolom is; pas dit aan indien nodig
        huurprijs_index = headers.index("huurprijs")

        # Pas het huurprijs aan rij/kolom
        data[index_te_aanpassen][huurprijs_index] = nieuw_huurprijs
        print(f"huurprijs van {data[index_te_aanpassen][0]} is aangepast naar: {nieuw_huurprijs}")
    else:
        print("Geen voertuig gevonden met de opgegeven waarde.")

    # Toon de bijgewerkte gegevens
    print("\nBijgewerkte lijst met voertuigen:")
    print(tabulate(data, headers=headers, tablefmt='grid'))

# Functie om de data naar het CSV-bestand weg te schrijven
def schrijf_data_weg():
    with open(bestand, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Schrijf de headers
        writer.writerow(headers)

        # Schrijf alle personeelsgegevens
        writer.writerows(data)
    print("\nDe bijgewerkte gegevens zijn succesvol opgeslagen in het bestand.")
    
def sorteer_voertuigen_op_huurprijs_opl():
    percentage_index = headers.index("huurprijs")

    # Sorteer de data op basis van de huurprijs-kolom (hoog naar laag)
    gesorteerde_data = sorted(data, key=lambda x: float(x[percentage_index]))

    # Toon de gesorteerde gegevens
    print("\nGesorteerde lijst met voertuigen op huurprijs (laag naar hoog):")
    print(tabulate(gesorteerde_data, headers=headers, tablefmt='grid'))

def toon_voertuigen_met_x_brandstof():
    print("\nAlle voertuigen (huidige lijst):")
    print(tabulate(data, headers=headers, tablefmt='grid'))

    # Controleer of de kolom 'brandstof' bestaat
    if "brandstof" in headers:
        keuze_brandstof = input("Geef de brandstof waarop je wil filteren: ").capitalize()
        brandstof_index = headers.index("brandstof")
        brandstof_voertuigen = [row for row in data if row[brandstof_index] == keuze_brandstof]

        if brandstof_voertuigen:
            print(f"\nvoertuigen met brandstof {keuze_brandstof}:")
            print(tabulate(brandstof_voertuigen, headers=headers, tablefmt='grid'))
        else:
            print(f"\nEr zijn geen {keuze_brandstof.lower()} voertuigen in de lijst.")
    else:
        print("\nKolom 'brandstof' bestaat niet in de gegevens. Controleer de CSV-headers.")

def toon_functies_auto():
    print("1: toon alle auto's")
    print("2: voeg auto toe")
    print("3: verwijder auto")
    print("4: sorteer op huurprijs (oplopend)")
    print("5: filter data op specifieke brandstof")
    print("6: pas huurprijs aan")
    print("7: update data")




#nieuw_voertuig_toevoegen()
#verwijder_voertuig()
#pas_huurprijs_aan()
#schrijf_data_weg()
#sorteer_voertuigen_op_huurprijs_opl()
#toon_voertuigen_met_x_brandstof()
