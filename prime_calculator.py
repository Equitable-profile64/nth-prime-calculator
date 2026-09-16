#!/usr/bin/env python3

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
    """Retourne le n-ième nombre premier."""
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            count += 1
        num += 1
    return num - 1

def main():
    """Fonction principale pour demander à l'utilisateur de saisir un rang et afficher le nombre premier correspondant."""
    while True:
        try:
            n = int(input("Veuillez entrer le rang du nombre premier que vous souhaitez trouver: "))
            if n <= 0:
                print("Le rang doit être un entier positif. Veuillez réessayer.")
            else:
                prime = nth_prime(n)
                print(f"Le {n}-ième nombre premier est {prime}")
                break
        except ValueError:
            print("Veuillez entrer un nombre entier valide. Veuillez réessayer.")

if __name__ == "__main__":
    main()

