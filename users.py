
class User():
    def __init__(self, first, last, g, w):
        self.first_name = first
        self.last_name = last
        self.gender = g
        self.weight = w
        self.login_attempts = 0

    def describe_user(self):
        print("Here's a summary of " + self.first_name.title() + " " + self.last_name.title())
        print("Gender: " + self.gender)
        print("Weight: " + str(self.weight))
        print("\n")

    def greet_user(self):
        print("Hello, " + self.first_name.title() + ". It's been a while -- we miss you!")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print("Login attempt #: " + str(self.login_attempts))
        print("\n")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print("Resetting login attempts...login attempt is now: " + str(self.login_attempts))

class Admin(User):
    def __init__(self, first, last, g, w):
        super().__init__(first, last, g, w)
        # self.priviledges = ["can add post", "can delete post", "can ban user", "can use backdoor"]
        self.privilege1 = Privileges()

class Privileges():
    def __init__(self):
        self.priviledges = ["can add post", "can delete post", "can ban user", "can use backdoor"]

    def show_priviledges(self):
        for privilege in self.priviledges:
            print("List of priviledges: " + str(privilege) + ", ")

admin1 = Admin("Gary", "Li", "F", 145)
admin1.privilege1.show_priviledges()