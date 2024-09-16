import sys
import time
import subprocess

def stampa_lentamente(testo, ritardo=0.03):
    for carattere in testo:
        sys.stdout.write(carattere)
        sys.stdout.flush()
        time.sleep(ritardo)
    print()

def accedi_intercettazioni():
    stampa_lentamente("Accesso al sistema di intercettazioni...")
    try:
        subprocess.run([sys.executable, "talk.py"], check=True)
    except subprocess.CalledProcessError:
        stampa_lentamente("Errore durante l'accesso alle intercettazioni.")
    except FileNotFoundError:
        stampa_lentamente("File talk.py non trovato. Verifica la sua presenza nella directory corrente.")

def comunicazioni():
    stampa_lentamente("Modulo di Comunicazioni attivato.")
    while True:
        print("\n" + "=" * 30)
        print("MEG OMEGA - Comunicazioni")
        print("=" * 30)
        print("1. Accedi a intercettazioni")
        print("2. Torna al menu principale")
        
        scelta = input("\nSeleziona un'opzione: ")
        
        if scelta == "1":
            accedi_intercettazioni()
        elif scelta == "2":
            stampa_lentamente("Uscita dal modulo di Comunicazioni...")
            break
        else:
            print("Opzione non valida. Riprova.")

if __name__ == "__main__":
    comunicazioni()
