guest = ["Eminem", "Elisa", "Obama"]
del guest[0]
guest.insert(0,"Jesus") #Replacement guest for eminem
#new guest bigger table
guest.append("Joshua R.")
guest.insert(0, "Michael Jordan")
guest.insert(2, "Kevin")

invitation3 = " apologies for the third for those already invited there has been a change of plans but for those new you've been invited to attend a grand feast with a select few others please attend!"

print("Good evening, " + guest[1] + invitation3 + "\n")
print("Good evening, " + guest[4] + invitation3 + "\n")
print("Good evening, " + guest[3] + invitation3 + "\n")
print("Good evening, " + guest[5] + invitation3 + "\n")
print("Good evening, " + guest[0] + invitation3 + "\n")
print("Good evening, " + guest[2] + invitation3 + "\n")

