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

# Vervang 'vintage_gitaren.csv' door het pad naar jouw CSV-bestand
bestand = 'vintage_gitaren.csv'

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
        print("Het CSV-bestand is leeg. Voeg een nieuwe gitaar toe om te beginnen.")

    # Voeg de bestaande rijen toe aan de data-lijst
    for row in reader:
        data.append(row)

# Toon de bestaande gegevens, als die er zijn
if data:
    print("Huidige lijst met vintage gitaren:")
    print(tabulate(data, headers=headers, tablefmt='fancy_grid'))
else:
    print("Er zijn nog geen gegevens van vintage gitaren beschikbaar.")

# Als het bestand leeg is, vraag de headers aan de gebruiker
if not headers:
    aantal_kolommen = int(input("Het bestand is leeg. Hoeveel kolommen wil je toevoegen? "))
    for i in range(aantal_kolommen):
        kolomnaam = input(f"Voer de naam van kolom {i + 1} in: ")
        headers.append(kolomnaam)
        
# Functie om een nieuwe gitaar toe te voegen
def nieuwe_gitaar_toevoegen():
    nieuwe_gitaar = []
    print("\nVoer de gegevens in voor een nieuwe gitaar:")

    # Automatisch ID genereren
    try:
        # Zoek de index van de ID-kolom
        id_index = headers.index("ID")

        # Bepaal het hoogste bestaande ID in de data
        bestaande_ids = [int(row[id_index]) for row in data if row[id_index].isdigit()]
        nieuw_id = max(bestaande_ids, default=0) + 1
    except ValueError:
        print("Er is geen kolom genaamd 'ID'. Zorg dat de ID-kolom bestaat.")
        return

    # Voeg het nieuwe ID toe aan de nieuwe gitaar
    nieuwe_gitaar.append(str(nieuw_id))

    for header in headers[1:]:
        waarde = input(f"Voer {header} in: ").capitalize()
        nieuwe_gitaar.append(waarde)

    # Voeg de nieuwe gitaar toe aan de data
    data.append(nieuwe_gitaar)

    # Toon de bijgewerkte gegevens
    print("\nBijgewerkte lijst met vintage gitaren:")
    print(tabulate(data, headers=headers, tablefmt='grid'))
    
# Functie om een gitaar te verwijderen
def verwijder_gitaar():
    print("\nHuidige lijst met vintage gitaren:")
    print(tabulate(data, headers=headers, tablefmt='grid'))

    try:
        id_index = headers.index("id")  # Gebruik de kolomnaam "id" (pas dit aan als nodig)
    except ValueError:
        try:
            id_index = headers.index("ID")  # Gebruik de kolomnaam "id" (pas dit aan als nodig)
        except ValueError:
            print("Er is geen kolom genaamd 'id'. Zorg dat de kolom bestaat.")
            return

    # Kies op basis van een kolom om een gitaar te verwijderen
    zoekterm = input(f"Voer de id van het gitaar dat je wenst te verwijderen: ")

    # Zoek naar de juiste rij om te verwijderen
    index_te_verwijderen = None
    for i, row in enumerate(data):
        if zoekterm == row[id_index]:  # We zoeken naar een rij die de zoekterm bevat
            index_te_verwijderen = i
            break

    if index_te_verwijderen is not None:
        print(f"Gitaar gevonden en verwijderd: {data[index_te_verwijderen]}")
        del data[index_te_verwijderen]  # Verwijder de gitaar
    else:
        print("Geen gitaar gevonden met de opgegeven waarde.")

    # Toon de bijgewerkte gegevens
    print("\nBijgewerkte lijst met vintage gitaren:")
    print(tabulate(data, headers=headers, tablefmt='grid'))
    
# Functie om de huurprijs van een gitaar aan te passen
def pas_staat_aan():
    print("\nHuidige lijst met vintage gitaren:")
    print(tabulate(data, headers=headers, tablefmt='grid'))

    try:
        id_index = headers.index("id")  # Gebruik de kolomnaam "id" (pas dit aan als nodig)
    except ValueError:
        try:
            id_index = headers.index("ID")  # Gebruik de kolomnaam "id" (pas dit aan als nodig)
        except ValueError:
            print("Er is geen kolom genaamd 'id'. Zorg dat de kolom bestaat.")
            return

    # Vraag de id van de gitaar waarvan je de staat wil aanpassen
    zoekterm = input(f"Voer de id in van het gitaar waarvan je de staat wilt aanpassen: ")

    # Zoek het gitaar
    index_te_aanpassen = None
    for i, row in enumerate(data):
        if zoekterm == row[id_index]:  # We zoeken naar een rij die de zoekterm bevat
            index_te_aanpassen = i
            break

    if index_te_aanpassen is not None:
        # Vraag de correcte staat van de gitaar
        nieuwe_staat = input("Voer de nieuwe staat in: ")

        # Neem aan dat de huurprijs-kolom de laatste kolom is; pas dit aan indien nodig
        staat_index = headers.index("Staat")

        # Pas de staat aan rij/kolom
        data[index_te_aanpassen][staat_index] = nieuwe_staat
        print(f"Staat van gitaar met id {data[index_te_aanpassen][0]} is aangepast naar: {nieuwe_staat}")
    else:
        print("Geen gitaar gevonden met de opgegeven waarde.")

    # Toon de bijgewerkte gegevens
    print("\nBijgewerkte lijst met vintage gitaren:")
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
    
def sorteer_vintage_gitaren_op_bouwjaar_opl():
    bouwjaar_index = headers.index("Bouwjaar")

    # Sorteer de data op basis van de Bouwjaar-kolom (hoog naar laag)
    gesorteerde_data = sorted(data, key=lambda x: int(x[bouwjaar_index]))

    # Toon de gesorteerde gegevens
    print("\nGesorteerde lijst met vintage_gitaren op bouwjaar (laag naar hoog):")
    print(tabulate(gesorteerde_data, headers=headers, tablefmt='grid'))

def toon_vintage_gitaren_type_x():
    print("\nAlle gitaren (huidige lijst):")
    print(tabulate(data, headers=headers, tablefmt='grid'))

    # Controleer of de kolom 'Type' bestaat
    if "Type" in headers:
        keuze_type = input("Geef het type waarop je wil filteren (Elektrisch/Akoestisch): ").capitalize()
        type_index = headers.index("Type")
        type_gitaren = [row for row in data if row[type_index] == keuze_type]

        if type_gitaren:
            print(f"\nGitaren met type '{keuze_type}':")
            print(tabulate(type_gitaren, headers=headers, tablefmt='grid'))
        else:
            print(f"\nEr zijn geen {keuze_type.lower()} gitaren in de lijst.")
    else:
        print("\nKolom 'Type' bestaat niet in de gegevens. Controleer de CSV-headers.")

def toon_functies_gitaren():
    print("1: toon alle vintage gitaren")
    print("2: voeg gitaar toe")
    print("3: verwijder gitaar")
    print("4: sorteer op bouwjaar (oplopend)")
    print("5: filter data op specifiek type")
    print("6: pas staat aan")
    print("7: update data")




#nieuwe_gitaar_toevoegen()
#verwijder_gitaar()
#pas_staat_aan()
#schrijf_data_weg()
#sorteer_vintage_gitaren_op_bouwjaar_opl()
#toon_vintage_gitaren_type_x()