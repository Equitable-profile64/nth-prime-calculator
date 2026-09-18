#!/usr/bin/env python3
import sys
import time

def is_prime(num):
    """Vérifie si un nombre est premier."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def nth_prime(n):
    """Retourne le n-ième nombre premier avec un rafraîchissement strict par bloc graphique."""
    count = 0
    num = 2
    bar_length = 20
    last_filled = -1
    
    # Affichage initial de la barre vide
    sys.stdout.write(f"\r\033[KCalcul en cours : [{' ' * bar_length}] 0% (0/{n})")
    sys.stdout.flush()
    
    while count < n:
        if is_prime(num):
            count += 1
            
            # On calcule le nombre exact de carrés à afficher (0 à 20)
            filled_length = int((bar_length * count) // n)
            
            # Le rafraîchissement se déclenche UNIQUEMENT si un carré s'ajoute ou à la fin
            if filled_length != last_filled or count == n:
                last_filled = filled_length
                percent = int((count * 100) // n)
                bar = '█' * filled_length + '-' * (bar_length - filled_length)
                
                sys.stdout.write(f"\r\033[KCalcul en cours : [{bar}] {percent}% ({count}/{n})")
                sys.stdout.flush()
                
        num += 1
        
    print()  # Saut de ligne final propre
    return num - 1

def main():
    """Fonction principale avec gestion du Ctrl+C et mesure du temps."""
    print("--- Calculateur de Nombre Premier (Entrez '0' pour quitter) ---")
    try:
        while True:
            try:
                n = int(input("\nVeuillez entrer le rang du nombre premier que vous souhaitez trouver : "))
                if n == 0:
                    print("Merci d'avoir utilisé le programme. Au revoir !")
                    break
                elif n < 0:
                    print("Le rang doit être un entier positif. Veuillez réessayer.")
                else:
                    start_time = time.perf_counter()
                    prime = nth_prime(n)
                    execution_time = time.perf_counter() - start_time
                    
                    print(f"Le {n}-ième nombre premier est {prime}")
                    print(f"Calcul exécuté en {execution_time:.2f} secondes.")
            except ValueError:
                print("Veuillez entrer un nombre entier valide. Veuillez réessayer.")
    except KeyboardInterrupt:
        print("\n\nProgramme interrompu par l'utilisateur. Au revoir !")
        sys.exit(0)

if __name__ == "__main__":
    main()
