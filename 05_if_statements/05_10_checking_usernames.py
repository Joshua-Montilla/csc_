current_users = ["Dewayne01", "Josh07", "Andrew#2", "Josef@04", "Jordan91"]
new_users = ["Dewayne01", "Eclipse02", "Jonson93", "Josef@04", "Jadrian21"]
CULowercase = ["dewayne01", "josh07", "andrew#2", "josef@04", "jordan91"]

for user in new_users:
    if user in current_users:
        print("\n This username "+user+", is already in use, please make another name. ")
    elif user in CULowercase:
         print("\n This username "+user+", is already in use, please make another name. ")
    else:
        print("\n This username, "+user+", is useable.")