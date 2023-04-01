# Classes use Pascal case(first letter of each word is capitalized)
# Constructor specifies what happens when object is being initialized.
# Attributes are variables associated with the object.
#
class User:
    def __init__(self, user_id, username):  # a function to initialize all the starting values
    # the function is called every time object is created
        self.id = user_id
        self.name = username
        self.followers = 0  # default value, do not have to provide
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User("001", "Uliana")
user_2 = User("001", "Tom")
print(user1.name)
