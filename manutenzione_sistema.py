import time
import os
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_centered(text):
    terminal_width = os.get_terminal_size().columns
    print(text.center(terminal_width))

def loading_animation():
    for _ in range(20):
        for char in "|/-\\":
            print_centered(f"Caricamento {char}")
            time.sleep(0.1)
            clear_screen()

def progress_bar():
    width = 40
    for i in range(width + 1):
        percent = i * 100 // width
        bar = '█' * i + '-' * (width - i)
        print_centered(f"Progresso: [{bar}] {percent}%")
        time.sleep(0.05)
        clear_screen()

def matrix_effect():
    chars = "01"
    width = os.get_terminal_size().columns
    height = os.get_terminal_size().lines

    for _ in range(100):
        screen = [[' ' for _ in range(width)] for _ in range(height)]
        for col in range(width):
            for row in range(height):
                if random.random() < 0.02:
                    screen[row][col] = random.choice(chars)
        
        print("\n".join("".join(row) for row in screen))
        time.sleep(0.05)
        clear_screen()

def scanning_animation():
    width = os.get_terminal_size().columns - 4
    for _ in range(3):
        for i in range(width):
            bar = ' ' * i + '|||' + ' ' * (width - i)
            print_centered(f"[{bar}]")
            time.sleep(0.02)
            clear_screen()
        for i in range(width, 0, -1):
            bar = ' ' * i + '|||' + ' ' * (width - i)
            print_centered(f"[{bar}]")
            time.sleep(0.02)
            clear_screen()

def run_maintenance():
    print_centered("Inizializzazione manutenzione del sistema MEG OMEGA")
    time.sleep(2)
    clear_screen()

    print_centered("Avvio scansione di sicurezza")
    scanning_animation()

    print_centered("Caricamento moduli di sistema")
    loading_animation()

    print_centered("Ottimizzazione database")
    progress_bar()

    print_centered("Aggiornamento firewall")
    matrix_effect()

    print_centered("Manutenzione completata con successo")
    time.sleep(2)
    clear_screen()

if __name__ == "__main__":
    run_maintenance()
