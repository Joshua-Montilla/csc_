guest = ["Eminem", "Elisa", "Obama"]
del guest[0]
guest.insert(0,"Jesus") #Replacement guest for eminem
#new guest bigger table
guest.append("Joshua R.")
guest.insert(0, "Michael Jordan")
guest.insert(2, "Kevin")

message = " apologies for the inconvience I wasn't able to get the big table and had shrunk down I'll be sure to make this up for you guys at a later date."
print("Good evening, " + guest[2] + message + "\n")
print("Good evening, " + guest[5] + message + "\n")
print("Good evening, " + guest[0] + message + "\n")
print("Good evening, " + guest[4] + message + "\n")


guest.pop(2)
guest.pop(4)
guest.pop(0)
guest.pop(2)

print(guest)
invitation4 = " after all the inconvience I formally invite you to have a great and fun dinner with me. Please show up I'd highly appreciate it."

print("Hello once again " + guest[1] + invitation4 + "\n")
print("Hello once again " + guest[0] + invitation4 + "\n")

del guest[1]
del guest[0]

