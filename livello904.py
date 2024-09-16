import random
import time

def stampa_lentamente(testo, ritardo=0.03):
    for carattere in testo:
        print(carattere, end='', flush=True)
        time.sleep(ritardo)
    print()

def calcola_successo(probabilita):
    return random.random() < probabilita

def genera_resoconto(successo, dettagli_successo, dettagli_fallimento):
    if successo:
        return f"MISSIONE RIUSCITA: {dettagli_successo}"
    else:
        return f"MISSIONE FALLITA: {dettagli_fallimento}"

def gestisci_richiesta(tipo_richiesta):
    stampa_lentamente(f"\nRichiesta di {tipo_richiesta} ricevuta dal Livello 904 - Dark Metro.")
    stampa_lentamente("Inizializzazione protocollo di risposta...")
    time.sleep(1)

    if tipo_richiesta == "Soccorso":
        return gestisci_soccorso()
    elif tipo_richiesta == "Rifornimenti":
        return gestisci_rifornimenti()
    elif tipo_richiesta == "Informazioni":
        return fornisci_informazioni()
    elif tipo_richiesta == "Intervento":
        return gestisci_intervento()
    elif tipo_richiesta == "Collasso":
        return gestisci_collasso()
    else:
        return "Errore: Tipo di richiesta non riconosciuto."

def gestisci_soccorso():
    stampa_lentamente("Richiesta di soccorso nella Dark Metro. Situazione critica.")
    stampa_lentamente("Opzioni disponibili:")
    stampa_lentamente("1. Inviare squadra di estrazione rapida (Probabilità di successo: 60%)")
    stampa_lentamente("2. Fornire istruzioni per nascondersi dai sacerdoti oscuri (Probabilità di successo: 40%)")
    stampa_lentamente("3. Tentare di negoziare con i sacerdoti oscuri (Probabilità di successo: 20%)")

    scelta = input("Seleziona un'opzione (1-3): ")

    if scelta == "1":
        successo = calcola_successo(0.6)
        return genera_resoconto(successo,
            "La squadra di estrazione è riuscita a recuperare i sopravvissuti. Tre agenti feriti, ma tutti sono tornati vivi. I sacerdoti oscuri hanno subito perdite significative.",
            "La squadra di estrazione è stata sopraffatta. Due agenti morti, tre dispersi. I sopravvissuti sono stati catturati dai sacerdoti oscuri.")
    elif scelta == "2":
        successo = calcola_successo(0.4)
        return genera_resoconto(successo,
            "I sopravvissuti sono riusciti a eludere i sacerdoti oscuri seguendo le istruzioni. Hanno trovato un passaggio sicuro e sono in attesa di estrazione.",
            "I sacerdoti oscuri hanno scoperto i nascondigli. Metà dei sopravvissuti catturati, gli altri dispersi nella Dark Metro.")
    elif scelta == "3":
        successo = calcola_successo(0.2)
        return genera_resoconto(successo,
            "Negoziazione riuscita. I sacerdoti oscuri hanno accettato di rilasciare i sopravvissuti in cambio di artefatti antichi. Situazione temporaneamente stabile.",
            "Negoziazione fallita. I sacerdoti oscuri hanno interpretato il tentativo come un'offesa. Rituali di sacrificio accelerati, situazione critica.")
    else:
        return "Opzione non valida. La richiesta di soccorso rimane in sospeso."

def gestisci_rifornimenti():
    stampa_lentamente("Richiesta di rifornimenti nella Dark Metro. Consegna rischiosa.")
    stampa_lentamente("Opzioni disponibili:")
    stampa_lentamente("1. Inviare drone di consegna stealth (Probabilità di successo: 70%)")
    stampa_lentamente("2. Nascondere rifornimenti in vari punti della metro (Probabilità di successo: 50%)")
    stampa_lentamente("3. Tentare una consegna diretta mascherata da offerta ai sacerdoti (Probabilità di successo: 30%)")

    scelta = input("Seleziona un'opzione (1-3): ")

    if scelta == "1":
        successo = calcola_successo(0.7)
        return genera_resoconto(successo,
            "Il drone ha consegnato con successo i rifornimenti. I sopravvissuti hanno ricevuto cibo, acqua e equipaggiamento di sopravvivenza senza essere rilevati.",
            "Il drone è stato intercettato e distrutto dai sacerdoti oscuri. Rifornimenti persi e posizione dei sopravvissuti potenzialmente compromessa.")
    elif scelta == "2":
        successo = calcola_successo(0.5)
        return genera_resoconto(successo,
            "Rifornimenti nascosti con successo. I sopravvissuti hanno recuperato l'80% dei pacchetti senza incidenti.",
            "Solo il 30% dei rifornimenti recuperati. Alcuni nascondigli scoperti dai sacerdoti, aumentando la loro vigilanza.")
    elif scelta == "3":
        successo = calcola_successo(0.3)
        return genera_resoconto(successo,
            "Consegna accettata dai sacerdoti. Rifornimenti distribuiti ai sopravvissuti sotto forma di 'offerte rifiutate'. Copertura mantenuta.",
            "Sacerdoti sospettosi. Consegna confiscata, agente di consegna catturato. Situazione dei sopravvissuti peggiorata.")
    else:
        return "Opzione non valida. La richiesta di rifornimenti rimane in sospeso."

def fornisci_informazioni():
    info = [
        "La Dark Metro si estende per 904 km di tunnel, con 66 stazioni conosciute.",
        "I sacerdoti oscuri sono sensibili alla luce ultravioletta. Equipaggiamento UV può offrire protezione.",
        "Esistono 7 aree sicure nascoste, accessibili solo attraverso sequenze specifiche di porte.",
        "Le luci della metro seguono un codice basato sui numeri primi. Decifrarlo può prevedere i movimenti dei sacerdoti.",
        "I treni fantasma appaiono ogni 33 minuti, ma solo nelle stazioni con numeri palindromi.",
        "Alcuni graffiti nelle stazioni sono in realtà mappe criptate dei livelli superiori e inferiori.",
        "L'acqua che gocciola dal soffitto in certi punti ha proprietà curative, ma in altri è altamente tossica.",
        "I sacerdoti oscuri non possono entrare in aree dove suona musica classica. Questo fenomeno è ancora inspiegabile.",
        "Esistono portali nascosti che collegano la Dark Metro ad altri livelli, attivabili solo in specifiche condizioni lunari.",
        "Alcuni sopravvissuti hanno sviluppato la capacità di vedere nel buio dopo lunghe esposizioni alla Dark Metro."
    ]
    return "\n".join(random.sample(info, 3))

def gestisci_intervento():
    stampa_lentamente("Richiesta di intervento nella Dark Metro. Situazione critica.")
    stampa_lentamente("Opzioni disponibili:")
    stampa_lentamente("1. Inviare squadra di assalto per eliminare i sacerdoti oscuri (Probabilità di successo: 40%)")
    stampa_lentamente("2. Attivare sistema di illuminazione d'emergenza per disorientare i sacerdoti (Probabilità di successo: 60%)")
    stampa_lentamente("3. Rilasciare agenti chimici per indurre allucinazioni nei sacerdoti (Probabilità di successo: 50%)")

    scelta = input("Seleziona un'opzione (1-3): ")

    if scelta == "1":
        successo = calcola_successo(0.4)
        return genera_resoconto(successo,
            "Operazione riuscita. 60% dei sacerdoti oscuri eliminati, gli altri in fuga. Controllo temporaneo stabilito su 3 settori della Dark Metro.",
            "Assalto fallito. Squadra decimata, sacerdoti rafforzati. Hanno acquisito equipaggiamento militare avanzato.")
    elif scelta == "2":
        successo = calcola_successo(0.6)
        return genera_resoconto(successo,
            "Illuminazione attivata con successo. Sacerdoti disorientati e in ritirata. Finestra di 3 ore per operazioni di salvataggio.",
            "Malfunzionamento del sistema. Solo il 30% delle luci attivate. Sacerdoti arrabbiati, aumentata l'aggressività.")
    elif scelta == "3":
        successo = calcola_successo(0.5)
        return genera_resoconto(successo,
            "Agenti chimici efficaci. Sacerdoti in stato confusionale. Opportunità per infiltrazioni e salvataggi nei prossimi 5 giorni.",
            "Reazione imprevista agli agenti chimici. Sacerdoti potenziati e più pericolosi. Situazione fuori controllo.")
    else:
        return "Opzione non valida. La richiesta di intervento rimane in sospeso."

def gestisci_collasso():
    stampa_lentamente("Allarme di collasso nel Livello 904 - Dark Metro!")
    stampa_lentamente("Opzioni disponibili:")
    stampa_lentamente("1. Attivare protocollo di sigillamento per contenere il collasso (Probabilità di successo: 80%)")
    stampa_lentamente("2. Tentare di stabilizzare il livello con tecnologia sperimentale (Probabilità di successo: 40%)")
    stampa_lentamente("3. Evacuare immediatamente, abbandonando il livello al suo destino (Probabilità di successo: 60%)")

    scelta = input("Seleziona un'opzione (1-3): ")

    if scelta == "1":
        successo = calcola_successo(0.8)
        return genera_resoconto(successo,
            "Sigillamento riuscito. Dark Metro isolata. Collasso contenuto al 95%. Perdite minime, ma il livello è ora inaccessibile.",
            "Sigillamento parziale. 40% del livello collassato prima del completamento. Fuga di entità oscure nei livelli adiacenti.")
    elif scelta == "2":
        successo = calcola_successo(0.4)
        return genera_resoconto(successo,
            "Stabilizzazione miracolosamente riuscita. Livello 904 ristrutturato e parzialmente purificato. Nuove aree sicure create.",
            "Catastrofe tecnologica. Collasso accelerato, creata anomalia spazio-temporale. Dark Metro fusa con altri tre livelli.")
    elif scelta == "3":
        successo = calcola_successo(0.6)
        return genera_resoconto(successo,
            "Evacuazione completata. 70% del personale e dei sopravvissuti estratti. Dark Metro abbandonata e collassata.",
            "Evacuazione caotica. Solo il 30% evacuato con successo. Molti dispersi o catturati dai sacerdoti durante la fuga.")
    else:
        return "Opzione non valida. Il collasso continua senza intervento."

if __name__ == "__main__":
    # Test
    print(gestisci_richiesta("Soccorso"))
