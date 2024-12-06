from pathlib import Path

person ="\nEnter your name: "

path = Path("10_files_and_exceptions/guest_book.txt")

people_container = []
while True:
    people = input(person)
    if people == 'quit':
        break

    print(f"Adding you, {people}, to our list")
    people_container.append(people)

line = ''
for people in people_container:
    line += f"{people}\n"
path.write_text(line)