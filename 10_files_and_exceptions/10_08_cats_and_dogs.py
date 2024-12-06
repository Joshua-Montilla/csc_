from pathlib import Path

Cats = Path("10_files_and_exceptions/cats.txt")
#Dogs = Path("10_files_and_exceptions/dogs.txt")
Dogs = Path("01_getting_started/dogs.txt")

try:
    catinfo = Cats.read_text()
    for line in catinfo.splitlines():
        print(line)
except FileNotFoundError:
    print(f"WHERE'S MY {Cats}!")

print("\n")

try:
    doginfo = Dogs.read_text()
    for line in doginfo.splitlines():
        print(line)
except FileNotFoundError:
    print(f"I think I miss my {Dogs}...")