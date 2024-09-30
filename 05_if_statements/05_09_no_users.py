Usernames = ["Josh", "Andrew", "Jesus", "Josef", "Dewayne", "Admin"]
del Usernames[0]
del Usernames[0]
del Usernames[0]
del Usernames[0]
del Usernames[0]
del Usernames[0]
for user in Usernames:
    if user == "Admin":
        print("\nHello "+user+", would you like to see a status report?")
    else:
        print("\nHello "+user+", thank you for logging in.")
else:
    print("We need to find some users!")