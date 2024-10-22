favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}
friends = ["Jadrian", "Josef", "Elisa", "Kevin", "phil","jen"]
for f in friends:
    print("\n Hello " + f.title())

    if f not in favorite_languages.keys():
        print(f.title() + ", Please take the poll to determine your favorite language.")
    else:
        print("Thank you for participating in the poll.")