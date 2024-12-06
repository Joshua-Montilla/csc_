from pathlib import Path
import json

path = Path("10_files_and_exceptions/favnumber.json")

num = input("Whats your favorite number? ")
fav = json.dumps(num)
path.write_text(fav)
print(f"{str(num)} is stored.")