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
    stampa_lentamente(f"\nRichiesta di {tipo_richiesta} ricevuta dal Livello 100 - Spiaggia Infinita.")
    stampa_lentamente("Analisi della situazione in corso...")
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
    stampa_lentamente("Richiesta di soccorso sulla Spiaggia Infinita. Ombre ostili rilevate.")
    stampa_lentamente("Opzioni disponibili:")
    stampa_lentamente("1. Inviare squadra di recupero con equipaggiamento anti-ombra (Probabilità di successo: 65%)")
    stampa_lentamente("2. Guidare i sopravvissuti verso un punto di estrazione sicuro (Probabilità di successo: 50%)")
    stampa_lentamente("3. Utilizzare esca luminosa per distrarre le ombre (Probabilità di successo: 40%)")

    scelta = input("Seleziona un'opzione (1-3): ")

    if scelta == "1":
        successo = calcola_successo(0.65)
        return genera_resoconto(successo,
            "La squadra ha recuperato con successo i sopravvissuti. L'equipaggiamento anti-ombra ha respinto efficacemente le entità ostili.",
            "La squadra è stata sopraffatta dalle ombre. Metà dell'equipaggio disperso, sopravvissuti ancora intrappolati.")
    elif scelta == "2":
        successo = calcola_successo(0.5)
        return genera_resoconto(successo,
            "I sopravvissuti hanno raggiunto il punto di estrazione. Evacuazione completata con perdite minime.",
            "Solo il 30% dei sopravvissuti è arrivato al punto di estrazione. Gli altri sono stati catturati dalle ombre.")
    elif scelta == "3":
        successo = calcola_successo(0.4)
        return genera_resoconto(successo,
            "L'esca luminosa ha funzionato. Le ombre sono state distratte, permettendo un'evacuazione silenziosa.",
            "L'esca ha attirato più ombre del previsto. La situazione è peggiorata, richiedendo un intervento di emergenza.")
    else:
        return "Opzione non valida. La richiesta di soccorso rimane in sospeso."

def gestisci_rifornimenti():
    stampa_lentamente("Richiesta di rifornimenti sulla Spiaggia Infinita. Condizioni ambientali instabili.")
    stampa_lentamente("Opzioni disponibili:")
    stampa_lentamente("1. Paracadutare rifornimenti in contenitori impermeabili (Probabilità di successo: 70%)")
    stampa_lentamente("2. Stabilire un avamposto di rifornimento nascosto (Probabilità di successo: 55%)")
    stampa_lentamente("3. Inviare sottomarino con rifornimenti attraverso l'oceano anomalo (Probabilità di successo: 45%)")

    scelta = input("Seleziona un'opzione (1-3): ")

    if scelta == "1":
        successo = calcola_successo(0.7)
        return genera_resoconto(successo,
            "Rifornimenti consegnati con successo. I contenitori impermeabili hanno protetto le provviste dalle condizioni ambientali estreme.",
            "Forte vento ha deviato i paracadute. Solo il 40% dei rifornimenti recuperati, il resto perso nell'oceano.")
    elif scelta == "2":
        successo = calcola_successo(0.55)
        return genera_resoconto(successo,
            "Avamposto stabilito e mimetizzato. Fornirà rifornimenti stabili per i prossimi 3 mesi.",
            "Avamposto scoperto dalle ombre. Rifornimenti compromessi e personale in pericolo.")
    elif scelta == "3":
        successo = calcola_successo(0.45)
        return genera_resoconto(successo,
            "Sottomarino arrivato con successo. Rifornimenti consegnati e nuova rotta sicura stabilita.",
            "Sottomarino scomparso nell'oceano anomalo. Persi rifornimenti e equipaggio. Rotta considerata troppo pericolosa.")
    else:
        return "Opzione non valida. La richiesta di rifornimenti rimane in sospeso."

def fornisci_informazioni():
    info = [
        "La Spiaggia Infinita si estende per migliaia di chilometri in tutte le direzioni.",
        "Le ombre sembrano essere più attive durante le 'notti', che durano in media 36 ore.",
        "L'acqua dell'oceano ha proprietà anomale, inclusa la capacità di alterare la percezione del tempo.",
        "Sono stati osservati fenomeni di miraggio che mostrano città impossibili all'orizzonte.",
        "La sabbia della spiaggia cambia colore in base all'umore collettivo dei presenti.",
        "Alcune zone della spiaggia presentano gravità alterata, permettendo salti impossibili.",
        "Le ombre sembrano essere attratte da forti emozioni negative.",
        "Sono stati scoperti bunker sotterranei risalenti a civiltà sconosciute.",
        "L'oceano occasionalmente 'restituisce' oggetti e persone scomparse da altri livelli.",
        "Le tempeste sulla Spiaggia Infinita possono durare settimane e alterare la realtà circostante."
    ]
    return "\n".join(random.sample(info, 3))

def gestisci_intervento():
    stampa_lentamente("Richiesta di intervento sulla Spiaggia Infinita. Minaccia ambientale rilevata.")
    stampa_lentamente("Opzioni disponibili:")
    stampa_lentamente("1. Dispiegare barriere energetiche per contenere l'anomalia (Probabilità di successo: 60%)")
    stampa_lentamente("2. Inviare team di ricerca per studiare e neutralizzare la minaccia (Probabilità di successo: 50%)")
    stampa_lentamente("3. Attivare protocollo di alterazione climatica locale (Probabilità di successo: 40%)")

    scelta = input("Seleziona un'opzione (1-3): ")

    if scelta == "1":
        successo = calcola_successo(0.6)
        return genera_resoconto(successo,
            "Barriere energetiche attivate con successo. Anomalia contenuta in un'area di 10 km quadrati.",
            "Barriere instabili. Anomalia in espansione, effetti imprevedibili si stanno manifestando oltre il perimetro.")
    elif scelta == "2":
        successo = calcola_successo(0.5)
        return genera_resoconto(successo,
            "Team di ricerca ha identificato la fonte dell'anomalia. Processo di neutralizzazione in corso.",
            "Team di ricerca scomparso. Ultimi rapporti indicano una mutazione dell'anomalia in risposta allo studio.")
    elif scelta == "3":
        successo = calcola_successo(0.4)
        return genera_resoconto(successo,
            "Alterazione climatica riuscita. Condizioni ambientali normalizzate, minaccia temporaneamente neutralizzata.",
            "Alterazione climatica fuori controllo. Creata una tempesta perpetua, situazione drasticamente peggiorata.")
    else:
        return "Opzione non valida. La richiesta di intervento rimane in sospeso."

def gestisci_collasso():
    stampa_lentamente("Allarme di collasso nel Livello 100 - Spiaggia Infinita!")
    stampa_lentamente("Opzioni disponibili:")
    stampa_lentamente("1. Attivare ancore dimensionali per stabilizzare il livello (Probabilità di successo: 70%)")
    stampa_lentamente("2. Evacuare il livello e sigillare gli accessi (Probabilità di successo: 80%)")
    stampa_lentamente("3. Tentare una fusione controllata con un livello adiacente (Probabilità di successo: 30%)")

    scelta = input("Seleziona un'opzione (1-3): ")

    if scelta == "1":
        successo = calcola_successo(0.7)
        return genera_resoconto(successo,
            "Ancore dimensionali attivate. Livello 100 stabilizzato. Fluttuazioni spazio-temporali ridotte del 85%.",
            "Attivazione fallita. Ancore hanno causato ulteriori fratture dimensionali. Parti della spiaggia stanno scomparendo.")
    elif scelta == "2":
        successo = calcola_successo(0.8)
        return genera_resoconto(successo,
            "Evacuazione completata. 90% del personale e dei sopravvissuti estratti. Accessi sigillati con successo.",
            "Evacuazione parziale. Solo il 60% evacuato. Sigillatura incompleta, rischio di contaminazione in altri livelli.")
    elif scelta == "3":
        successo = calcola_successo(0.3)
        return genera_resoconto(successo,
            "Fusione controllata riuscita. Creato nuovo livello stabile 'Arcipelago Onirico'. Nuove opportunità di esplorazione.",
            "Fusione catastrofica. Creato vortice dimensionale instabile. Multipli livelli compromessi.")
    else:
        return "Opzione non valida. Il collasso continua senza intervento."

if __name__ == "__main__":
    # Test
    print(gestisci_richiesta("Soccorso"))

