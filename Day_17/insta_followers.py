# Just some practice with classes from Angela.
# Use PascalCase for class names
# Use snake_case for pretty much everything else

class User:
    def __init__(self, user_id, user_name): # This is the constructor or initializer, whenever a new object is created it requires these paramaeters
        self.id = user_id
        self.user_name = user_name
        self.followers = 0
        self.following = 0


    def follow_someone(self, who_to_follow):
        self.following += 1
        who_to_follow.followers += 1




user_1 = User('001', 'Chris')
user_2 = User("002", "Fruitcake")


# follow_someone(user_1, user_2)
# This is super wrong, methods need an object

user_1.follow_someone(user_2)


print(user_1.following)
print(user_1.followers)
print(user_2.following)
print(user_2.followers)
