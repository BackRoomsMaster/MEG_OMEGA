import time
import random
import sys
import subprocess
import json
import os

def stampa_lentamente(testo, ritardo=0.03):
    for carattere in testo:
        sys.stdout.write(carattere)
        sys.stdout.flush()
        time.sleep(ritardo)
    print()

def simulazione_analisi(tipo_analisi):
    print(f"\nAvvio {tipo_analisi}...")
    for i in range(10):
        time.sleep(0.3)
        print("." * (i + 1))
    stampa_lentamente(f"{tipo_analisi} completata.")

def genera_file_backrooms():
    try:
        result = subprocess.run([sys.executable, "generate_backrooms_files.py"], 
                                capture_output=True, text=True, check=True)
        return result.stdout.strip().split('\n')
    except subprocess.CalledProcessError as e:
        stampa_lentamente(f"Errore durante la generazione dei file: {e}")
        stampa_lentamente(f"Output di errore: {e.stderr}")
        return []
    except FileNotFoundError:
        stampa_lentamente("File generate_backrooms_files.py non trovato.")
        return []

def leggi_file_agente(nome_file):
    percorso_file = os.path.join("backrooms_data", nome_file)
    with open(percorso_file, "r") as f:
        return json.load(f)

def analisi_predittiva():
    stampa_lentamente("Inizializzazione modello predittivo...")
    time.sleep(1)
    stampa_lentamente("Caricamento dati dalle Backrooms...")
    file_generati = genera_file_backrooms()
    if not file_generati:
        stampa_lentamente("Impossibile procedere con l'analisi. Dati non disponibili.")
        return
    
    stampa_lentamente(f"Analisi di {len(file_generati)} file dalle Backrooms...")
    simulazione_analisi("Analisi predittiva")
    accuratezza = random.uniform(85, 99)
    stampa_lentamente(f"Analisi completata con un'accuratezza del {accuratezza:.2f}%")
    stampa_lentamente("Dati degli agenti analizzati:")
    for file in file_generati[:5]:  # Mostra solo i primi 5 file
        agente = leggi_file_agente(file)
        stampa_lentamente(f"- {agente['nome']}: Livello {agente['livello']}, Status: {agente['status']}")

def visualizzazione_dati():
    stampa_lentamente("Preparazione dati per la visualizzazione...")
    file_generati = genera_file_backrooms()
    if not file_generati:
        stampa_lentamente("Impossibile procedere con la visualizzazione. Dati non disponibili.")
        return
    
    num_file = min(5, len(file_generati))
    stampa_lentamente(f"Visualizzazione di {num_file} file dalle Backrooms:")
    for file in file_generati[:num_file]:
        agente = leggi_file_agente(file)
        stampa_lentamente(f"- Agente: {agente['nome']}")
        stampa_lentamente(f"  Ultimo livello noto: {agente['livello']}")
        stampa_lentamente(f"  Status: {agente['status']}")
        time.sleep(0.5)
    stampa_lentamente("Visualizzazione dati completata.")

def analisi_dati():
    stampa_lentamente("Modulo di Analisi Dati attivato.")
    while True:
        print("\n" + "=" * 30)
        print("MEG OMEGA - Analisi Dati")
        print("=" * 30)
        print("1. Analisi predittiva")
        print("2. Visualizzazione dati")
        print("3. Torna al menu principale")
        
        scelta = input("\nSeleziona un'opzione: ")
        
        if scelta == "1":
            analisi_predittiva()
        elif scelta == "2":
            visualizzazione_dati()
        elif scelta == "3":
            stampa_lentamente("Uscita dal modulo di Analisi Dati...")
            break
        else:
            print("Opzione non valida. Riprova.")

if __name__ == "__main__":
    analisi_dati()
