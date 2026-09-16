# nth-prime-calculator

Programme Python simple et pédagogique permettant de calculer le n-ième nombre premier.

Le projet est volontairement compact afin de faciliter la compréhension de l’algorithme, de la structure Python, de l’utilisation en ligne de commande, de l’intégration avec Termux et du workflow Git/GitHub.

## Fonctionnalités

- Vérification de la primalité d’un entier.
- Calcul du n-ième nombre premier.
- Validation des entrées utilisateur.
- Refus des rangs nuls ou négatifs.
- Gestion des entrées invalides ou non numériques.
- Interface interactive en ligne de commande.
- Exécution avec Python.
- Utilisation possible comme commande `prim` dans Termux.
- Aucune dépendance Python externe.

## Exemple

Les premiers nombres premiers sont :

```text
2, 3, 5, 7, 11, 13, 17, 19, 23, 29
```

Le 8e nombre premier est donc :

```text
19
```

Exemple d’exécution :

```text
Veuillez entrer le rang du nombre premier que vous souhaitez trouver: 8
Le 8-ième nombre premier est 19
```

## Prérequis

Le projet nécessite :

- Python 3.8 ou une version plus récente.
- Un terminal.
- Git pour versionner le projet.
- GitHub CLI pour créer et publier le dépôt depuis le terminal.

Aucun paquet Python externe n’est requis.

## Installation

### Cloner le dépôt

Clone le projet depuis GitHub :

```bash
git clone [https://github.com/USERNAME/nth-prime-calculator.git](https://github.com/USERNAME/nth-prime-calculator.git)
```

Remplace `USERNAME` par ton nom d’utilisateur GitHub.

Entre ensuite dans le répertoire :

```bash
cd nth-prime-calculator
```

### Télécharger les fichiers manuellement

Tu peux également télécharger l’archive du projet depuis GitHub, l’extraire, puis entrer dans le répertoire extrait :

```bash
cd nth-prime-calculator
```

## Exécuter le programme

### Avec Python

La méthode la plus portable consiste à exécuter :

```bash
python prime_calculator.py
```

Sur les systèmes où la commande `python` n’est pas disponible, utilise :

```bash
python3 prime_calculator.py
```

Le programme demande le rang du nombre premier recherché :

```text
Veuillez entrer le rang du nombre premier que vous souhaitez trouver:
```

Saisis un entier positif, par exemple :

```text
8
```

Le programme affiche :

```text
Le 8-ième nombre premier est 19
```

### Exécution directe

Le script peut aussi être exécuté directement s’il possède :

1. Un shebang Python.
2. Le droit d’exécution.

La première ligne de `prime_calculator.py` doit être :

```python
#!/usr/bin/env python3
```

Rends ensuite le fichier exécutable :

```bash
chmod +x prime_calculator.py
```

Lance-le avec :

```bash
./prime_calculator.py
```

Le préfixe `./` indique que le fichier exécutable se trouve dans le répertoire courant.

## Utilisation avec Termux

Le projet fonctionne dans Termux sur Android.

### Installer Python

Mets à jour les informations des paquets Termux :

```bash
pkg update
```

Installe Python :

```bash
pkg install python
```

Vérifie la version installée :

```bash
python --version
```

Exécute le programme :

```bash
python prime_calculator.py
```

### Créer la commande `prim`

Pour exécuter le programme en tapant simplement :

```bash
prim
```

vérifie d’abord que le fichier commence par :

```python
#!/usr/bin/env python3
```

Depuis le répertoire du projet, ajoute le droit d’exécution :

```bash
chmod +x prime_calculator.py
```

Crée un lien symbolique dans le répertoire des commandes Termux :

```bash
ln -sf "$PWD/prime_calculator.py" "$PREFIX/bin/prim"
```

Dans Termux, la variable `$PREFIX` désigne généralement le répertoire privé d’installation de Termux :

```text
/data/data/com.termux/files/usr
```

Le répertoire `$PREFIX/bin` est inclus dans le `PATH` de Termux. Les commandes installées à cet emplacement peuvent donc être exécutées depuis n’importe quel répertoire.

Teste la commande :

```bash
prim
```

Vérifie son emplacement :

```bash
command -v prim
```

Résultat attendu :

```text
/data/data/com.termux/files/usr/bin/prim
```

### À propos des liens symboliques

Le lien symbolique pointe vers l’emplacement exact du fichier source.

Si le projet est déplacé ou renommé, le lien peut devenir invalide. Recrée-le avec :

```bash
cd ~/Projets/nth-prime-calculator
ln -sf "$PWD/prime_calculator.py" "$PREFIX/bin/prim"
```

Vérifie le lien avec :

```bash
ls -l "$PREFIX/bin/prim"
```

### Installer une copie du script

Au lieu de créer un lien symbolique, tu peux copier le script dans le répertoire des commandes Termux :

```bash
cp prime_calculator.py "$PREFIX/bin/prim"
chmod +x "$PREFIX/bin/prim"
```

La commande sera alors indépendante du répertoire du projet :

```bash
prim
```

Cependant, les modifications apportées au fichier source ne seront pas automatiquement copiées dans la commande installée. Après chaque modification, exécute :

```bash
cp prime_calculator.py "$PREFIX/bin/prim"
chmod +x "$PREFIX/bin/prim"
```

Le lien symbolique est plus pratique pendant le développement, car il utilise toujours la version actuelle du fichier source.

## Fonctionnement du programme

Le programme est organisé autour de trois fonctions principales :

```python
is_prime(num)
nth_prime(n)
main()
```

### Fonction `is_prime`

La fonction `is_prime` détermine si un nombre est premier.

Un nombre premier est un entier supérieur à 1 qui possède exactement deux diviseurs positifs :

- 1.
- Lui-même.

Exemples de nombres premiers :

```text
2, 3, 5, 7, 11, 13
```

Exemples de nombres qui ne sont pas premiers :

```text
1, 4, 6, 8, 9, 10
```

La fonction rejette immédiatement les nombres inférieurs ou égaux à 1 :

```python
if num <= 1:
    return False
```

Les nombres 2 et 3 sont premiers :

```python
if num <= 3:
    return True
```

La fonction rejette ensuite les nombres divisibles par 2 ou par 3 :

```python
if num % 2 == 0 or num % 3 == 0:
    return False
```

L’opérateur `%` renvoie le reste d’une division entière.

Par exemple :

```python
10 % 2 == 0
```

signifie que 10 est divisible par 2.

La fonction teste ensuite les diviseurs possibles avec des incréments de 6 :

```python
i = 5

while i * i <= num:
    if num % i == 0 or num % (i + 2) == 0:
        return False
    i += 6
```

Les nombres supérieurs à 3 qui sont premiers sont toujours de la forme :

```text
6k - 1
```

ou :

```text
6k + 1
```

Exemples :

```text
5  = 6 × 1 - 1
7  = 6 × 1 + 1
11 = 6 × 2 - 1
13 = 6 × 2 + 1
17 = 6 × 3 - 1
19 = 6 × 3 + 1
```

Cette optimisation évite de tester de nombreux diviseurs inutiles.

### Fonction `nth_prime`

La fonction `nth_prime` calcule le n-ième nombre premier.

Par exemple :

```text
nth_prime(1) = 2
nth_prime(2) = 3
nth_prime(3) = 5
nth_prime(8) = 19
```

La fonction commence à 2 et compte les nombres premiers :

```python
count = 0
num = 2

while count < n:
    if is_prime(num):
        count += 1
    num += 1
```

Lorsque le nombre de nombres premiers recherché est atteint, la fonction retourne le dernier nombre premier trouvé :

```python
return num - 1
```

La soustraction est nécessaire parce que `num` est incrémenté après la détection du dernier nombre premier.

### Fonction `main`

La fonction `main` gère l’interaction avec l’utilisateur.

Elle demande une valeur :

```python
n = int(input(...))
```

L’entrée utilisateur est d’abord une chaîne de caractères, puis elle est convertie en entier.

Si l’utilisateur saisit une valeur invalide, Python déclenche une exception `ValueError`. Le programme intercepte cette exception et affiche un message explicatif :

```python
except ValueError:
    print("Veuillez entrer un nombre entier valide. Veuillez réessayer.")
```

Le programme refuse également les valeurs nulles ou négatives :

```python
if n <= 0:
    print("Le rang doit être un entier positif. Veuillez réessayer.")
```

La boucle s’arrête après le traitement d’un rang positif valide.

## Algorithme utilisé

Le programme utilise la division par essais successifs.

Pour déterminer si un nombre est premier, il cherche un éventuel diviseur. Si un diviseur est trouvé, le nombre n’est pas premier.

Le programme teste uniquement les diviseurs possibles jusqu’à la racine carrée du nombre. Cette limite est suffisante : si un nombre possède un facteur supérieur à sa racine carrée, il possède nécessairement un facteur correspondant inférieur ou égal à cette racine carrée.

Par exemple, pour 36 :

```text
6 × 6 = 36
```

Au moins un facteur d’un nombre composé est inférieur ou égal à sa racine carrée.

Le programme utilise la condition suivante :

```python
while i * i <= num:
```

Cette écriture évite de calculer une racine carrée en virgule flottante.

## Complexité

Soit \(p\) un nombre candidat.

Le test de primalité nécessite environ :

```text
O(√p)
```

tests de divisibilité dans le pire cas.

Pour calculer le n-ième nombre premier, le programme teste les entiers successifs jusqu’à trouver le n-ième nombre premier. Le temps d’exécution augmente donc avec la valeur de `n`.

Cette implémentation convient à l’apprentissage et au calcul de valeurs modérées. Elle n’est pas conçue pour remplacer des algorithmes avancés de génération de nombres premiers ou des bases de nombres premiers précalculées.

## Exemples d’entrée

### Entrées valides

Entrée :

```text
1
```

Sortie :

```text
Le 1-ième nombre premier est 2
```

Entrée :

```text
8
```

Sortie :

```text
Le 8-ième nombre premier est 19
```

Entrée :

```text
10
```

Sortie :

```text
Le 10-ième nombre premier est 29
```

### Entrées invalides

Entrée :

```text
0
```

Sortie :

```text
Le rang doit être un entier positif. Veuillez réessayer.
```

Entrée :

```text
-4
```

Sortie :

```text
Le rang doit être un entier positif. Veuillez réessayer.
```

Entrée :

```text
abc
```

Sortie :

```text
Veuillez entrer un nombre entier valide. Veuillez réessayer.
```

## Structure du projet

```text
nth-prime-calculator/
├── .gitignore
├── README.FR.md
├── README.md
└── prime_calculator.py
```

### Description des fichiers

| Fichier | Description |
|---|---|
| `prime_calculator.py` | Programme Python principal. |
| `README.md` | Documentation principale en anglais. |
| `README.FR.md` | Documentation française. |
| `.gitignore` | Fichiers et répertoires ignorés par Git. |

## Workflow de développement

Entre dans le répertoire du projet :

```bash
cd ~/Projets/nth-prime-calculator
```

Vérifie l’état actuel de Git :

```bash
git status
```

Exécute le programme :

```bash
python prime_calculator.py
```

Ou, dans Termux :

```bash
prim
```

Après une modification, examine les différences :

```bash
git diff
```

Ajoute les modifications à l’index Git :

```bash
git add .
```

Crée un commit :

```bash
git commit -m "Add French README"
```

Envoie le commit sur GitHub :

```bash
git push
```

Vérifie à nouveau l’état du dépôt :

```bash
git status
```

Résultat attendu :

```text
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

## Initialisation de Git

Si le projet n’a pas encore été initialisé comme dépôt Git :

```bash
git init
git branch -M main
git add .
git commit -m "Initial commit"
```

Ajoute le dépôt distant GitHub :

```bash
git remote add origin [https://github.com/USERNAME/nth-prime-calculator.git](https://github.com/USERNAME/nth-prime-calculator.git)
```

Remplace `USERNAME` par ton nom d’utilisateur GitHub.

Pousse la branche `main` :

```bash
git push -u origin main
```

L’option `-u` associe la branche locale `main` à la branche distante `origin/main`. Les prochains envois pourront ensuite être effectués avec :

```bash
git push
```

## Créer le dépôt GitHub avec GitHub CLI

Si GitHub CLI est installé et authentifié, crée et publie le dépôt avec :

```bash
gh repo create nth-prime-calculator --public --source=. --remote=origin --push
```

Pour créer un dépôt privé :

```bash
gh repo create nth-prime-calculator --private --source=. --remote=origin --push
```

Vérifie l’authentification :

```bash
gh auth status
```

Ouvre le dépôt dans un navigateur :

```bash
gh repo view --web
```

## Liste de vérification

Avant de créer un commit, vérifie :

```bash
python --version
python prime_calculator.py
```

Teste au minimum les entrées suivantes :

```text
1
2
8
10
0
-1
abc
```

Dans Termux, vérifie également :

```bash
command -v prim
prim
```

Vérifie le droit d’exécution :

```bash
ls -l prime_calculator.py
```

La chaîne de permissions doit contenir `x`, par exemple :

```text
-rwxr-xr-x
```

## Dépannage

### `python: command not found`

Installe Python dans Termux :

```bash
pkg update
pkg install python
```

### `prime_calculator.py: command not found`

Utilise le chemin relatif :

```bash
./prime_calculator.py
```

Ou exécute le script avec Python :

```bash
python prime_calculator.py
```

### `Permission denied`

Ajoute le droit d’exécution :

```bash
chmod +x prime_calculator.py
```

### Bash signale une erreur de syntaxe près de `(`

Le script ne possède probablement pas le shebang Python.

Ajoute cette ligne tout au début :

```python
#!/usr/bin/env python3
```

Puis exécute :

```bash
chmod +x prime_calculator.py
./prime_calculator.py
```

### `prim: command not found`

Recrée le lien symbolique :

```bash
cd ~/Projets/nth-prime-calculator
ln -sf "$PWD/prime_calculator.py" "$PREFIX/bin/prim"
```

Vérifie que `$PREFIX/bin` est présent dans le `PATH` :

```bash
echo "$PATH"
```

Vérifie la commande :

```bash
command -v prim
```

### La commande `prim` utilise une ancienne version

Si `prim` est un lien symbolique, vérifie sa cible :

```bash
ls -l "$PREFIX/bin/prim"
```

Recrée le lien si nécessaire :

```bash
cd ~/Projets/nth-prime-calculator
ln -sf "$PWD/prime_calculator.py" "$PREFIX/bin/prim"
```

### Git indique que le répertoire n’est pas un dépôt

Assure-toi d’être dans le répertoire du projet :

```bash
cd ~/Projets/nth-prime-calculator
```

Initialise Git si nécessaire :

```bash
git init
```

### Aucun dépôt distant n’est configuré

Affiche les dépôts distants configurés :

```bash
git remote -v
```

Ajoute le dépôt GitHub :

```bash
git remote add origin [https://github.com/USERNAME/nth-prime-calculator.git](https://github.com/USERNAME/nth-prime-calculator.git)
```

## Améliorations possibles

Le projet peut évoluer de plusieurs manières :

- Accepter le rang en argument : `python prime_calculator.py 100`.
- Ajouter un mode détaillé avec `--verbose`.
- Ajouter des tests automatisés avec `unittest` ou `pytest`.
- Améliorer l’accord grammatical des messages français.
- Ajouter un mode de benchmark.
- Mettre en cache les nombres premiers déjà calculés.
- Générer tous les nombres premiers jusqu’à une limite donnée.
- Ajouter une interface graphique.
- Transformer le projet en application Python installable.
- Ajouter l’intégration continue avec GitHub Actions.
- Ajouter une analyse statique avec Ruff, Black ou mypy.
- Ajouter des annotations de type.
- Ajouter la prise en charge de plusieurs langues.
- Ajouter un point d’entrée en ligne de commande.
- Publier le programme comme paquet Python.

## Licence

Aucune licence n’est actuellement spécifiée pour ce projet.

Si tu souhaites autoriser explicitement la réutilisation, la modification et la redistribution du code, ajoute une licence open source telle que la licence MIT.

## Auteur

Projet créé comme exercice pratique autour de Python, de la ligne de commande, de Git, de GitHub et de Termux.

