import csv
from tabulate import tabulate

# Vervang 'belgische_bieren.csv' door het pad naar jouw CSV-bestand
bestand = 'belgische_bieren.csv'

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
        print("Het CSV-bestand is leeg. Voeg een nieuw bier toe om te beginnen.")

    # Voeg de bestaande rijen toe aan de data-lijst
    for row in reader:
        data.append(row)

# Toon de bestaande gegevens, als die er zijn
if data:
    print("Huidige lijst met bieren:")
    print(tabulate(data, headers=headers, tablefmt='fancy_grid'))
else:
    print("Er zijn nog geen gegevens van bieren beschikbaar.")

# Als het bestand leeg is, vraag de headers aan de gebruiker
if not headers:
    aantal_kolommen = int(input("Het bestand is leeg. Hoeveel kolommen wil je toevoegen? "))
    for i in range(aantal_kolommen):
        kolomnaam = input(f"Voer de naam van kolom {i + 1} in: ")
        headers.append(kolomnaam)
        
# Functie om een nieuw bier toe te voegen
def nieuw_bier_toevoegen():
    nieuw_bier = []
    print("\nVoer de gegevens in voor een nieuw bier:")
    for header in headers:
        waarde = input(f"Voer {header} in: ")
        nieuw_bier.append(waarde)

    # Voeg het nieuwe bier toe aan de data
    data.append(nieuw_bier)

    # Toon de bijgewerkte gegevens
    print("\nBijgewerkte lijst met bieren:")
    print(tabulate(data, headers=headers, tablefmt='grid'))
    
# Functie om een bier te verwijderen
def verwijder_bier():
    print("\nHuidige lijst met bieren:")
    print(tabulate(data, headers=headers, tablefmt='grid'))

    # Kies op basis van een kolom om een bier te verwijderen
    zoekterm = input(f"Voer de naam die je wenst te verwijderen: ")

    # Zoek naar de juiste rij om te verwijderen
    index_te_verwijderen = None
    for i, row in enumerate(data):
        if zoekterm in row:  # We zoeken naar een rij die de zoekterm bevat
            index_te_verwijderen = i
            break

    if index_te_verwijderen is not None:
        print(f"bier gevonden en verwijderd: {data[index_te_verwijderen]}")
        del data[index_te_verwijderen]  # Verwijder het bier
    else:
        print("Geen bier gevonden met de opgegeven waarde.")

    # Toon de bijgewerkte gegevens
    print("\nBijgewerkte lijst met bieren:")
    print(tabulate(data, headers=headers, tablefmt='grid'))
    
# Functie om het alcoholpercentage van een bier aan te passen
def pas_alcoholpercentage_aan():
    print("\nHuidige lijst met bieren:")
    print(tabulate(data, headers=headers, tablefmt='grid'))

    # Vraag de naam van het bier wiens alcoholpercentage je wilt aanpassen
    zoekterm = input(f"Voer de naam in van het bier waarvan je het alcoholpercentage wilt aanpassen: ")

    # Zoek het bier
    index_te_aanpassen = None
    for i, row in enumerate(data):
        if zoekterm in row:  # We zoeken naar een rij die de zoekterm bevat
            index_te_aanpassen = i
            break

    if index_te_aanpassen is not None:
        # Vraag het nieuwe alcoholpercentage
        nieuw_alcoholpercentage = input("Voer het nieuwe alcoholpercentage in: ")

        # Neem aan dat de alcoholpercentage-kolom de laatste kolom is; pas dit aan indien nodig
        alcoholpercentage_index = headers.index("alcoholpercentage")

        # Pas het alcoholpercentage aan rij/kolom
        data[index_te_aanpassen][alcoholpercentage_index] = nieuw_alcoholpercentage
        print(f"alcoholpercentage van {data[index_te_aanpassen][0]} is aangepast naar: {nieuw_alcoholpercentage}")
    else:
        print("Geen bier gevonden met de opgegeven waarde.")

    # Toon de bijgewerkte gegevens
    print("\nBijgewerkte lijst met bieren:")
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
    
def sorteer_bieren_op_percentage():
    percentage_index = headers.index("alcoholpercentage")

    # Sorteer de data op basis van de alcoholpercentage-kolom (hoog naar laag)
    gesorteerde_data = sorted(data, key=lambda x: float(x[percentage_index]), reverse=True)

    # Toon de gesorteerde gegevens
    print("\nGesorteerde lijst met bieren op alcoholpercentage (hoog naar laag):")
    print(tabulate(gesorteerde_data, headers=headers, tablefmt='grid'))

def toon_bieren_boven_8perc():
    print("\nAlle bieren (huidige lijst):")
    print(tabulate(data, headers=headers, tablefmt='grid'))

    # Controleer of de kolom 'alcoholpercentage' bestaat
    if "alcoholpercentage" in headers:
        alcoholpercentage_index = headers.index("alcoholpercentage")
        alcoholpercentage_bieren = [row for row in data if float(row[alcoholpercentage_index]) >= 8]

        if alcoholpercentage_bieren:
            print("\nBieren met alcoholpercentage >= 8 %:")
            print(tabulate(alcoholpercentage_bieren, headers=headers, tablefmt='grid'))
        else:
            print("\nEr zijn geen mannelijke bieren in de lijst.")
    else:
        print("\nKolom 'alcoholpercentage' bestaat niet in de gegevens. Controleer de CSV-headers.")


#nieuw_bier_toevoegen()
#verwijder_bier()
#pas_alcoholpercentage_aan()
#schrijf_data_weg()
#sorteer_bieren_op_percentage()
#toon_bieren_boven_8perc()