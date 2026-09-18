#!/usr/bin/env python3
import sys

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
    """Retourne le n-ième nombre premier avec une barre de progression stable sous Termux."""
    count = 0
    num = 2
    bar_length = 20
    last_filled = -1
    
    # Premier affichage de la barre vide
    sys.stdout.write(f"\r\033[KCalcul en cours : [{' ' * bar_length}] 0% (0/{n})")
    sys.stdout.flush()
    
    while count < n:
        if is_prime(num):
            count += 1
            
            # Calcule directement la taille visuelle de la barre (de 0 à 20)
            filled_length = int(bar_length * count // n)
            
            # Ne rafraîchit l'écran que si la barre graphique évolue ou si on atteint la fin
            if filled_length != last_filled or count == n:
                last_filled = filled_length
                percent = int((count / n) * 100)
                bar = '█' * filled_length + '-' * (bar_length - filled_length)
                
                # Le code \033[K nettoie la ligne Termux pour éviter les duplications
                sys.stdout.write(f"\r\033[KCalcul en cours : [{bar}] {percent}% ({count}/{n})")
                sys.stdout.flush()
                
        num += 1
        
    print() # Saut de ligne final propre
    return num - 1

def main():
    """Fonction principale pour demander à l'utilisateur de saisir un rang."""
    print("--- Calculateur de Nombre Premier (Entrez '0' pour quitter) ---")
    while True:
        try:
            # Nettoyage de l'antislash fautif
            n = int(input("\nVeuillez entrer le rang du nombre premier que vous souhaitez trouver : "))
            if n == 0:
                print("Merci d'avoir utilisé le programme. Au revoir !")
                break
            elif n < 0:
                print("Le rang doit être un entier positif. Veuillez réessayer.")
            else:
                prime = nth_prime(n)
                print(f"Le {n}-ième nombre premier est {prime}")
        except ValueError:
            print("Veuillez entrer un nombre entier valide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
