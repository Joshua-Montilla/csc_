from pathlib import Path
import json

def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        profile = json.loads(contents)
        return profile
    else:
        return None

def get_new_username(path):
    """Prompt for a new username."""
    name = input("What is your name? ")
    age = input("Age? ")
    place = input("Location? ")
    profile = {
        'name' : name,
        'age' : age,
        'location' : place
        }
    contents = json.dumps(profile)
    path.write_text(contents)
    return profile

def greet_user():
    """Greet the user by name."""
    path = Path('10_files_and_exceptions/profile.json')
    profile = get_stored_username(path)
    if profile:
        print(f"Welcome back, {profile['name']}!")
        print(f"Has it been your {1+int(profile['age'])}th birthday yet?")
        print(f"How is it at {profile['location']}?")
    else:
        profile = get_new_username(path)
        print(f"We'll remember you when you come back, {profile['name']}!")

greet_user()