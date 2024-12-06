from pathlib import Path
import json

def fav_number():
    path = Path("10_files_and_exceptions/favnumber.json")
    if path.exists():
        fav = path.read_text()
        num = json.loads(fav)

        print(f"we remember {num} is your favorite number.")
    
    else: 
        num = input("Whats your favorite number? ")
        fav = json.dumps(num)
        path.write_text(fav)
        print(f"{str(num)} is stored.")

fav_number()