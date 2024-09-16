import os
import json
import datetime

APPUNTI_FILE = "appunti_database.json"

def carica_appunti():
    if os.path.exists(APPUNTI_FILE):
        with open(APPUNTI_FILE, "r") as file:
            return json.load(file)
    return []

def salva_appunti(appunti):
    with open(APPUNTI_FILE, "w") as file:
        json.dump(appunti, file, indent=2)

def aggiungi_appunto():
    titolo = input("Inserisci il titolo dell'appunto: ")
    contenuto = input("Inserisci il contenuto dell'appunto: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    nuovo_appunto = {
        "titolo": titolo,
        "contenuto": contenuto,
        "timestamp": timestamp
    }
    
    appunti = carica_appunti()
    appunti.append(nuovo_appunto)
    salva_appunti(appunti)
    print("Appunto salvato con successo.")

def visualizza_appunti():
    appunti = carica_appunti()
    if not appunti:
        print("Nessun appunto trovato.")
        return

    for i, appunto in enumerate(appunti, 1):
        print(f"\n{i}. Titolo: {appunto['titolo']}")
        print(f"   Data: {appunto['timestamp']}")
        print(f"   Contenuto: {appunto['contenuto'][:50]}...")  # Mostra solo i primi 50 caratteri

def elimina_appunto():
    appunti = carica_appunti()
    if not appunti:
        print("Nessun appunto da eliminare.")
        return

    visualizza_appunti()
    try:
        indice = int(input("\nInserisci il numero dell'appunto da eliminare: ")) - 1
        if 0 <= indice < len(appunti):
            appunto_eliminato = appunti.pop(indice)
            salva_appunti(appunti)
            print(f"Appunto '{appunto_eliminato['titolo']}' eliminato con successo.")
        else:
            print("Numero non valido.")
    except ValueError:
        print("Input non valido. Inserisci un numero.")

def database():
    while True:
        print("\n" + "=" * 30)
        print("MEG OMEGA - Database Personale")
        print("=" * 30)
        print("1. Aggiungi appunto")
        print("2. Visualizza appunti")
        print("3. Elimina appunto")
        print("4. Torna al menu principale")

        scelta = input("\nSeleziona un'opzione: ")

        if scelta == "1":
            aggiungi_appunto()
        elif scelta == "2":
            visualizza_appunti()
        elif scelta == "3":
            elimina_appunto()
        elif scelta == "4":
            print("Uscita dal database personale...")
            break
        else:
            print("Opzione non valida. Riprova.")

if __name__ == "__main__":
    database()
