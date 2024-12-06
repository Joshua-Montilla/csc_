from pathlib import Path

person = input("Enter your name: ")

path = Path("10_files_and_exceptions/guest.txt")
path.write_text(person)