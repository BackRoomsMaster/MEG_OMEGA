import time
import sys
import subprocess

def stampa_lentamente(testo, ritardo=0.03):
    for carattere in testo:
        sys.stdout.write(carattere)
        sys.stdout.flush()
        time.sleep(ritardo)
    print()

def esegui_modulo(nome_file):
    try:
        subprocess.run([sys.executable, nome_file], check=True)
    except subprocess.CalledProcessError:
        stampa_lentamente(f"Errore durante l'esecuzione di {nome_file}")
    except FileNotFoundError:
        stampa_lentamente(f"File {nome_file} non trovato. Contattare l'amministratore.")

def menu_principale():
    while True:
        print("\n" + "=" * 30)
        print("MEG OMEGA - Menu Principale")
        print("=" * 30)
        print("1. Analisi Dati")
        print("2. Comunicazioni")
        print("3. Manutenzione Sistema")
        print("4. Database")
        print("5. Richiedi Supporto")
        print("6. Logout")
        
        scelta = input("\nInserisci il numero dell'opzione desiderata: ")
        
        if scelta == "1":
            esegui_modulo("analisi_dati.py")
        elif scelta == "2":
            esegui_modulo("comunicazioni.py")
        elif scelta == "3":
            esegui_modulo("manutenzione_sistema.py")
        elif scelta == "4":
            esegui_modulo("database.py")
        elif scelta == "5":
            esegui_modulo("supporto.py")
        elif scelta == "6":
            stampa_lentamente("Logout in corso. Arrivederci, operatore.")
            break
        else:
            print("Opzione non valida. Riprova.")

if __name__ == "__main__":
    menu_principale()
