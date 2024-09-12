guest = ["Eminem", "Elisa", "Obama"]



invitation = f" to have a nice dinner with me."

print("I formally invite you, " + guest[0].title() + invitation + "\n")
print("I formally invite you, " + guest[1].title() + invitation + "\n")
print("I formally invite you, " + guest[2].title() + invitation + "\n")

print( guest[0] + " called and had said he unfortunately couldn't make it.")

del guest[0]
guest.insert(0,"Jesus")
print (guest)


