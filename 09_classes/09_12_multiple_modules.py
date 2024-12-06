# 4
from one_user import User
from Admins2 import Privileges, Admin

admin = Admin("Jadrian", "The destroyer", 950, "Space")
print(admin.fname, admin.lname)
admin.privilege.show_privileges()