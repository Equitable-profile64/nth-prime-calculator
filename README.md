# nth-prime-calculator

> 🇫🇷 Documentation française : [README.FR.md](README.FR.md)

A simple and educational Python command-line program for calculating the n-th prime number.

The project is intentionally small so that the underlying algorithm, Python structure, command-line usage, Git workflow, and Termux integration remain easy to understand.

## Features

- Determines whether an integer is prime.
- Calculates the n-th prime number.
- Validates user input.
- Rejects non-positive ranks.
- Handles invalid and non-numeric input.
- Provides an interactive command-line interface.
- Can be executed directly with Python.
- Can be installed as a custom `prim` command in Termux.
- Requires no external Python dependencies.

## Example

The first prime numbers are:

```text
2, 3, 5, 7, 11, 13, 17, 19, 23, 29
```

Therefore, the 8th prime number is:

```text
19
```

Example program output:

```text
Veuillez entrer le rang du nombre premier que vous souhaitez trouver: 8
Le 8-ième nombre premier est 19
```

## Requirements

The project requires:

- Python 3.8 or newer.
- A terminal.
- Git, if you want to version and publish the project.
- GitHub CLI, if you want to create the GitHub repository directly from the terminal.

No external Python package is required.

## Installation

### Clone the repository

Clone the project from GitHub:

```bash
git clone git@github.com:valorisa/nth-prime-calculator.git
```

Enter the project directory:

```bash
cd nth-prime-calculator
```

### Download the source manually

Alternatively, download the project archive from GitHub, extract it, and enter the extracted directory:

```bash
cd nth-prime-calculator
```

## Running the program

### With Python

The most portable way to execute the program is:

```bash
python prime_calculator.py
```

On systems where `python` refers to Python 2 or is unavailable, use:

```bash
python3 prime_calculator.py
```

The program asks for the rank of the prime number:

```text
Veuillez entrer le rang du nombre premier que vous souhaitez trouver:
```

Enter a positive integer, for example:

```text
8
```

The program displays:

```text
Le 8-ième nombre premier est 19
```

### Direct execution

The script can also be executed directly if it has:

1. A Python shebang.
2. Execute permission.

The first line of `prime_calculator.py` should be:

```python
#!/usr/bin/env python3
```

Then make the file executable:

```bash
chmod +x prime_calculator.py
```

Run it with:

```bash
./prime_calculator.py
```

The `./` prefix means that the executable file is located in the current directory.

## Using the program in Termux

This project works in Termux on Android.

### Install Python

Update the Termux package information:

```bash
pkg update
```

Install Python:

```bash
pkg install python
```

Check the installed version:

```bash
python --version
```

Run the program:

```bash
python prime_calculator.py
```

### Create the `prim` command

To run the program by typing only:

```bash
prim
```

first make sure that the script begins with:

```python
#!/usr/bin/env python3
```

From the project directory, make the script executable:

```bash
chmod +x prime_calculator.py
```

Create a symbolic link in the Termux command directory:

```bash
ln -sf "$PWD/prime_calculator.py" "$PREFIX/bin/prim"
```

The variable `$PREFIX` normally refers to the private Termux installation prefix:

```text
/data/data/com.termux/files/usr
```

The directory `$PREFIX/bin` is included in Termux's `PATH`, which allows commands installed there to be executed from any directory.

Test the command:

```bash
prim
```

You can check its location with:

```bash
command -v prim
```

Expected output:

```text
/data/data/com.termux/files/usr/bin/prim
```

### Important note about symbolic links

The symbolic link points to the exact location of the source file.

If the project directory is moved or renamed, the link may become invalid. Recreate it with:

```bash
cd ~/Projets/nth-prime-calculator
ln -sf "$PWD/prime_calculator.py" "$PREFIX/bin/prim"
```

Check the link with:

```bash
ls -l "$PREFIX/bin/prim"
```

### Alternative: install a copy

Instead of creating a symbolic link, you can copy the script into the Termux command directory:

```bash
cp prime_calculator.py "$PREFIX/bin/prim"
chmod +x "$PREFIX/bin/prim"
```

This makes `prim` independent from the project directory:

```bash
prim
```

However, changes made to the source file will not automatically be copied to the installed command. Repeat the copy command after modifying the source:

```bash
cp prime_calculator.py "$PREFIX/bin/prim"
chmod +x "$PREFIX/bin/prim"
```

A symbolic link is more convenient during development because it always uses the current source file.

## How the program works

The program is divided into three main functions:

```python
is_prime(num)
nth_prime(n)
main()
```

### The `is_prime` function

The `is_prime` function determines whether a number is prime.

A prime number is a positive integer greater than 1 that has exactly two positive divisors:

- 1.
- The number itself.

Examples of prime numbers:

```text
2, 3, 5, 7, 11, 13
```

Examples of non-prime numbers:

```text
1, 4, 6, 8, 9, 10
```

The function immediately rejects numbers less than or equal to 1:

```python
if num <= 1:
    return False
```

Numbers 2 and 3 are prime:

```python
if num <= 3:
    return True
```

The function then rejects numbers divisible by 2 or 3:

```python
if num % 2 == 0 or num % 3 == 0:
    return False
```

The `%` operator returns the remainder of an integer division.

For example:

```python
10 % 2 == 0
```

means that 10 is divisible by 2.

The function then tests possible divisors using increments of 6:

```python
i = 5

while i * i <= num:
    if num % i == 0 or num % (i + 2) == 0:
        return False
    i += 6
```

Numbers greater than 3 that are prime are always of the form:

```text
6k - 1
```

or:

```text
6k + 1
```

For example:

```text
5  = 6 × 1 - 1
7  = 6 × 1 + 1
11 = 6 × 2 - 1
13 = 6 × 2 + 1
17 = 6 × 3 - 1
19 = 6 × 3 + 1
```

This optimization avoids testing many unnecessary divisors.

### The `nth_prime` function

The `nth_prime` function calculates the n-th prime number.

For example:

```text
nth_prime(1)  = 2
nth_prime(2)  = 3
nth_prime(3)  = 5
nth_prime(8)  = 19
```

The function starts at 2 and counts prime numbers:

```python
count = 0
num = 2

while count < n:
    if is_prime(num):
        count += 1
    num += 1
```

When the requested number of primes has been found, the function returns the last prime detected:

```python
return num - 1
```

The subtraction is necessary because `num` is incremented once after the last prime is found.

### The `main` function

The `main` function manages interaction with the user.

It repeatedly asks for a value:

```python
n = int(input(...))
```

The input is converted from text to an integer.

If the user enters an invalid value, Python raises a `ValueError`. The program catches this exception and displays an explanatory message:

```python
except ValueError:
    print("Veuillez entrer un nombre entier valide. Veuillez réessayer.")
```

The program also rejects zero and negative values:

```python
if n <= 0:
    print("Le rang doit être un entier positif. Veuillez réessayer.")
```

The loop stops after a valid positive rank has been processed.

## Algorithm

The program uses trial division.

To determine whether a number is prime, it tries to find a divisor. If a divisor is found, the number is not prime.

The program only tests possible divisors up to the square root of the number. This is sufficient because if a number has a factor larger than its square root, it must also have a corresponding factor smaller than its square root.

For example, for 36:

```text
6 × 6 = 36
```

At least one factor of any composite number must be less than or equal to its square root.

The implementation uses the condition:

```python
while i * i <= num:
```

This avoids calculating a floating-point square root.

## Complexity

Let \(p\) be a candidate number.

The primality test requires approximately:

```text
O(√p)
```

divisor checks in the worst case.

Calculating the n-th prime requires testing successive integers until the n-th prime is found. The execution time increases as `n` becomes larger.

This implementation is appropriate for educational use and moderate values of `n`. It is not intended to compete with advanced prime-generation algorithms or precomputed prime databases.

## Input examples

### Valid input

```text
1
```

Output:

```text
Le 1-ième nombre premier est 2
```

```text
8
```

Output:

```text
Le 8-ième nombre premier est 19
```

```text
10
```

Output:

```text
Le 10-ième nombre premier est 29
```

### Invalid input

Input:

```text
0
```

Output:

```text
Le rang doit être un entier positif. Veuillez réessayer.
```

Input:

```text
-4
```

Output:

```text
Le rang doit être un entier positif. Veuillez réessayer.
```

Input:

```text
abc
```

Output:

```text
Veuillez entrer un nombre entier valide. Veuillez réessayer.
```

## Project structure

```text
nth-prime-calculator/
├── .gitignore
├── README.md
└── prime_calculator.py
```

### File descriptions

| File | Description |
|---|---|
| `prime_calculator.py` | Main Python program. |
| `README.md` | Project documentation. |
| `.gitignore` | Files and directories ignored by Git. |

## Development workflow

Enter the project directory:

```bash
cd ~/Projets/nth-prime-calculator
```

Check the current Git status:

```bash
git status
```

Run the program:

```bash
python prime_calculator.py
```

Or, in Termux:

```bash
prim
```

After making changes, inspect the differences:

```bash
git diff
```

Stage the changes:

```bash
git add .
```

Create a commit:

```bash
git commit -m "Improve prime calculator documentation"
```

Push the commit to GitHub:

```bash
git push
```

Check the repository status again:

```bash
git status
```

Expected output:

```text
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

## Git initialization

If the project has not yet been initialized as a Git repository:

```bash
git init
git branch -M main
git add .
git commit -m "Initial commit"
```

Add a GitHub remote:

```bash
git remote add origin [https://github.com/USERNAME/nth-prime-calculator.git](https://github.com/USERNAME/nth-prime-calculator.git)
```

Replace `USERNAME` with your GitHub username.

Push the `main` branch:

```bash
git push -u origin main
```

The `-u` option associates the local `main` branch with the remote `origin/main` branch. Future pushes can then be performed with:

```bash
git push
```

## Creating the GitHub repository with GitHub CLI

If GitHub CLI is installed and authenticated, create and push the repository with:

```bash
gh repo create nth-prime-calculator --public --source=. --remote=origin --push
```

For a private repository, use:

```bash
gh repo create nth-prime-calculator --private --source=. --remote=origin --push
```

Check the authentication status:

```bash
gh auth status
```

Open the repository in a browser:

```bash
gh repo view --web
```

## Testing checklist

Before committing changes, verify:

```bash
python --version
python prime_calculator.py
```

Test at least the following inputs:

```text
1
2
8
10
0
-1
abc
```

For Termux, also verify:

```bash
command -v prim
prim
```

Check the executable permission:

```bash
ls -l prime_calculator.py
```

The permission string should contain `x`, for example:

```text
-rwxr-xr-x
```

## Troubleshooting

### `python: command not found`

Install Python in Termux:

```bash
pkg update
pkg install python
```

### `prime_calculator.py: command not found`

Use the relative path:

```bash
./prime_calculator.py
```

Or execute it through Python:

```bash
python prime_calculator.py
```

### `Permission denied`

Add execute permission:

```bash
chmod +x prime_calculator.py
```

### Bash reports a syntax error near `(`

The script is probably missing its Python shebang.

Add this line at the very beginning:

```python
#!/usr/bin/env python3
```

Then run:

```bash
chmod +x prime_calculator.py
./prime_calculator.py
```

### `prim: command not found`

Recreate the symbolic link:

```bash
cd ~/Projets/nth-prime-calculator
ln -sf "$PWD/prime_calculator.py" "$PREFIX/bin/prim"
```

Check that `$PREFIX/bin` is in the `PATH`:

```bash
echo "$PATH"
```

Check the command:

```bash
command -v prim
```

### The `prim` command uses an old version

If `prim` is a symbolic link, verify its target:

```bash
ls -l "$PREFIX/bin/prim"
```

Recreate the link if necessary:

```bash
cd ~/Projets/nth-prime-calculator
ln -sf "$PWD/prime_calculator.py" "$PREFIX/bin/prim"
```

### Git reports `not a git repository`

Make sure you are inside the project directory:

```bash
cd ~/Projets/nth-prime-calculator
```

Then initialize Git if necessary:

```bash
git init
```

### Git reports that no remote exists

Display the configured remotes:

```bash
git remote -v
```

Add the GitHub remote:

```bash
git remote add origin [https://github.com/USERNAME/nth-prime-calculator.git](https://github.com/USERNAME/nth-prime-calculator.git)
```

## Possible improvements

This project can be extended in several directions:

- Add command-line arguments such as `python prime_calculator.py 100`.
- Add an optional `--verbose` mode.
- Add automated tests with `unittest` or `pytest`.
- Improve grammatical agreement in French output.
- Add a benchmark mode.
- Cache previously calculated prime numbers.
- Generate a list of primes up to a specified limit.
- Add a graphical user interface.
- Package the program as an installable Python application.
- Add continuous integration with GitHub Actions.
- Add static analysis with Ruff, Black, or mypy.
- Add type annotations.
- Add support for multiple languages.
- Add a dedicated command-line entry point.
- Publish the program as a Python package.

## License

This project does not currently specify a license.

If you want other people to freely use, modify, and redistribute the project, add an open-source license such as the MIT License.

## Author

Created as a practical Python, command-line, Git, GitHub, and Termux learning project.

