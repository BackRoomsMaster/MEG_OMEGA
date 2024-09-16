import time
import sys
import subprocess

def stampa_lentamente(testo, ritardo=0.03):
    for carattere in testo:
        sys.stdout.write(carattere)
        sys.stdout.flush()
        time.sleep(ritardo)
    print()

def barra_progresso(durata):
    for i in range(101):
        sys.stdout.write('\r')
        sys.stdout.write("[%-100s] %d%%" % ('='*i, i))
        sys.stdout.flush()
        time.sleep(durata/100)
    print()

def introduzione():
    stampa_lentamente("Inizializzazione di MEG OMEGA in corso...")
    barra_progresso(3)
    
    stampa_lentamente("\nCaricamento moduli principali:")
    time.sleep(0.5)
    stampa_lentamente("- Modulo di Analisi Dati")
    time.sleep(0.5)
    stampa_lentamente("- Modulo di Comunicazioni")
    time.sleep(0.5)
    stampa_lentamente("- Modulo di Manutenzione Sistema")
    barra_progresso(2)
    
    stampa_lentamente("\nConfigurazione protocolli di sicurezza...")
    time.sleep(1)
    stampa_lentamente("Crittografia avanzata attivata.")
    time.sleep(0.5)
    
    stampa_lentamente("\nSincronizzazione database in corso...")
    barra_progresso(2)
    
    stampa_lentamente("\nMEG OMEGA è ora operativo.")
    stampa_lentamente("Ricorda: ogni azione sarà registrata e analizzata.")
    stampa_lentamente("La sicurezza è la nostra priorità.")
    
    time.sleep(1)
    stampa_lentamente("\nAvvio interfaccia principale...")
    time.sleep(2)
    
    # Avvio di omega_alpha.py
    try:
        subprocess.run([sys.executable, "omega_alpha.py"], check=True)
    except subprocess.CalledProcessError:
        stampa_lentamente("Errore critico. Terminazione forzata.")
    except FileNotFoundError:
        stampa_lentamente("File di sistema mancante. Contattare l'amministratore.")

if __name__ == "__main__":
    introduzione()
