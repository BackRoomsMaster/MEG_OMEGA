import random
import json
import os

def genera_nome():
    nomi = ["Alex", "Sam", "Jordan", "Casey", "Taylor", "Morgan", "Riley", "Avery", "Quinn", "Skyler"]
    cognomi = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
    return f"{random.choice(nomi)} {random.choice(cognomi)}"

def genera_livello():
    return random.randint(0, 999)

def genera_status():
    stati = ["disperso", "morto", "in pericolo", "ferito", "impazzito", "scomparso", "intrappolato"]
    return random.choice(stati)

def genera_file_agente():
    agente = {
        "nome": genera_nome(),
        "livello": genera_livello(),
        "status": genera_status()
    }
    return agente

def genera_backrooms_files(num_files=20):
    if not os.path.exists("backrooms_data"):
        os.makedirs("backrooms_data")

    file_generati = []
    for i in range(num_files):
        agente = genera_file_agente()
        nome_file = f"agente_{i+1:03d}.json"
        percorso_file = os.path.join("backrooms_data", nome_file)
        with open(percorso_file, "w") as f:
            json.dump(agente, f, indent=2)
        file_generati.append(nome_file)
        print(nome_file)  # Stampa il nome del file generato

    return file_generati

if __name__ == "__main__":
    genera_backrooms_files()
