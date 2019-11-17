# import mypackage.user
# import mypackage.user as mymodule
from mypackage.user import adminUser
# bob = user.adminUser('bob',23)
bob =adminUser('bob',23)
print(bob.name)
bob.say_hi()
bob.say_hello()
