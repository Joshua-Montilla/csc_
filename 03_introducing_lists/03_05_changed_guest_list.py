guest = ["Eminem", "Elisa", "Obama"]



invitation2 = f" I once again formally invite you to have a fun dinner with me."

#print("I formally invite you, " + guest[0].title() + invitation + "\n")
#print("I formally invite you, " + guest[1].title() + invitation + "\n")
#print("I formally invite you, " + guest[2].title() + invitation + "\n")

#print( guest[0] + " called and had said he unfortunately couldn't make it.")

del guest[0]
guest.insert(0,"Jesus")

print("With a change in plan, " + guest[0].title() + invitation2 + "\n")
print("With a change in plan, " + guest[1].title() + invitation2 + "\n")
print("With a change in plan, " + guest[2].title() + invitation2 + "\n")