import subprocess
import sys

def visualizza_menu():
    print("\n" + "=" * 30)
    print("Benvenuto in MEG OMEGA")
    print("=" * 30)
    print("1. Accedi al programma")
    print("2. Esci")
    print("=" * 30)

def accedi_al_programma():
    print("Accesso al programma in corso...")
    try:
        subprocess.run([sys.executable, "intro.py"], check=True)
    except subprocess.CalledProcessError:
        print("Accesso negato.")
    except FileNotFoundError:
        print("File corrotto o mancante. Controllare validità credenziali.")
        print("Ogni accesso non consentito non sarà perdonato.")

def main():
    while True:
        visualizza_menu()
        scelta = input("Inserisci il numero dell'opzione desiderata: ")
        
        if scelta == "1":
            accedi_al_programma()
        elif scelta == "2":
            print("Grazie per aver usato MEG OMEGA. Arrivederci!")
            break
        else:
            print("Opzione non valida. Per favore, scegli 1 o 2.")

if __name__ == "__main__":
    main()
