Usernames = ["Josh", "Andrew", "Jesus", "Josef", "Dewayne", "Admin"]

for user in Usernames:
    if user == "Admin":
        print("\nHello "+user+", would you like to see a status report?")
    else:
        print("\nHello "+user+", thank you for logging in.")