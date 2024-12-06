def make_shirt(size= "large", text="i love python"):
    print("\nMy shirt should be a "+ size.upper())
    print('And should have"'+ text.title()+ '"on it.')

make_shirt()
make_shirt(size= "medium")
make_shirt("small", "i need it for my little sister.")