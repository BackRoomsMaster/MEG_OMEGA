import random
import importlib

LIVELLI = [904, 100, 400, 611]
TIPI_RICHIESTA = ["Soccorso", "Rifornimenti", "Informazioni", "Intervento", "Collasso"]

def genera_richieste():
    richieste = []
    for _ in range(3):
        livello = random.choice(LIVELLI)
        tipo_richiesta = random.choice(TIPI_RICHIESTA)
        richieste.append((livello, tipo_richiesta))
    return richieste

def gestisci_richiesta(livello, tipo_richiesta):
    try:
        modulo = importlib.import_module(f"livello{livello}")
        return modulo.gestisci_richiesta(tipo_richiesta)
    except ImportError:
        return f"Errore: Modulo per il livello {livello} non trovato."
    except AttributeError:
        return f"Errore: Il modulo del livello {livello} non ha la funzione gestisci_richiesta."

def supporto():
    print("\nGenerazione richieste di supporto in corso...")
    richieste = genera_richieste()
    
    while True:
        print("\n" + "=" * 30)
        print("MEG OMEGA - Supporto")
        print("=" * 30)
        for i, (livello, tipo) in enumerate(richieste, 1):
            print(f"{i}. Livello {livello}: Richiesta di {tipo}")
        print("4. Torna al menu principale")

        scelta = input("\nSeleziona una richiesta da gestire (1-3) o 4 per uscire: ")
        
        if scelta in ["1", "2", "3"]:
            indice = int(scelta) - 1
            livello, tipo = richieste[indice]
            risposta = gestisci_richiesta(livello, tipo)
            print(f"\nRisposta alla richiesta del Livello {livello}:")
            print(risposta)
            input("\nPremi Invio per continuare...")
        elif scelta == "4":
            print("Uscita dal modulo di Supporto...")
            break
        else:
            print("Opzione non valida. Riprova.")

if __name__ == "__main__":
    supporto()
