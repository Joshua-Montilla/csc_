from pathlib import Path
import json

path = Path("10_files_and_exceptions/favnumber.json")
fav = path.read_text()
num = json.loads(fav)

print(f"we remember {num} is your favorite number.")