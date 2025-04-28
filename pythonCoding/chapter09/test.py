# # 练习9.1 餐馆
# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type

#     def describe_restaurant(self):
#         print(f"The {self.restaurant_name} is {self.cuisine_type} restaurant.")

#     def open_restaurant(self):
#         print(f"{self.restaurant_name} is open.")


# my_restaurant = Restaurant("La Tour d’Argent", "French cuisine")
# your_restaurant = Restaurant("Fuxing Lou", "Chinese cuisine")

# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()

# your_restaurant.describe_restaurant()
# your_restaurant.open_restaurant()


# # 练习9.3 用户
# class User:

#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name

#     def greet_uesr(self):
#         print(f"Hello {self.first_name}, welcome to python world.")


# my_user = User("si", "zhao")
# your_user = User("neng", "liu")

# my_user.greet_uesr()
# your_user.greet_uesr()


# # 练习 9.4 就餐人数
# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0

#     def describe_restaurant(self):
#         print(
#             f"The {self.restaurant_name} is {self.cuisine_type} restaurant.\n{self.number_served} people in there."
#         )

#     def open_restaurant(self):
#         print(f"{self.restaurant_name} is open.")

#     def set_number_served(self, served_num):
#         self.number_served = served_num

#     def increment_number_served(self, add_num):
#         self.number_served += add_num


# my_restaurant = Restaurant("La Tour d’Argent", "French cuisine")
# my_restaurant.describe_restaurant()

# my_restaurant.set_number_served(20)
# my_restaurant.increment_number_served(5)
# my_restaurant.describe_restaurant()


# # 练习9.5 尝试登录次数
class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def greet_uesr(self):
        print(f"Hello {self.first_name}, welcome to python world.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


# my_user = User("si", "zhao")

# my_user.greet_uesr()
# my_user.increment_login_attempts()
# my_user.increment_login_attempts()
# my_user.increment_login_attempts()
# print(my_user.login_attempts)

# my_user.reset_login_attempts()
# print(my_user.login_attempts)


# # 练习9.6 冰激凌小店
# class IceCreamStand(Restaurant):

#     def __init__(self, restaurant_name, cuisine_type, flavors):
#         super().__init__(restaurant_name, cuisine_type)
#         self.flavors = flavors

#     def show_flavors(self):
#         print(f"The {self.restaurant_name} has {self.flavors} flavors.")


# my_stand = IceCreamStand("IceHourse", "ice cream", ["banana", "apple", ""])


# # 练习 9.7 管理员
# class Admin(User):

#     def __init__(self, first_name, last_name, privileges):
#         super().__init__(first_name, last_name)
#         self.privileges = privileges

#     def show_privileges(self):
#         print(
#             f"The user {self.first_name} {self.last_name} have {self.privileges} privileges."
#         )


# my_user = Admin("yiqi", "wang", ["can add post", "can delete post", "can ban user"])
# my_user.show_privileges()


# # 练习9.8 权限
# class Privileges:
#     """权限类"""

#     def __init__(self, privileges=["can add post", "can delete post", "can ban user"]):
#         self.privileges = privileges

#     def show_privileges(self):
#         print(f"User have {self.privileges} privileges.")


# class Admin(User):

#     def __init__(self, first_name, last_name):
#         super().__init__(first_name, last_name)
#         self.privileges = Privileges()


# 练习 9.13 骰子
# from random import randint


# class Die:
#     def __init__(self, sides=6):
#         self.sides = sides

#     def roll_die(self):
#         print(randint(1, self.sides))


# # my_sides_6 = Die()
# # for i in range(10):
# #     my_sides_6.roll_die()

# # my_sides_10 = Die(10)
# # for i in range(10):
# #     my_sides_10.roll_die()

# my_sides_20 = Die(20)
# for i in range(10):
#     my_sides_20.roll_die()

# 练习 9.14彩票
from random import choice

tickets = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e"]
luck_nums = []
my_tickets = []
for i in range(4):
    luck_nums.append(choice(tickets))
    my_tickets.append(choice(tickets))

print(f"幸运彩票号是:{luck_nums}")

count = 1
while my_tickets != luck_nums:
    my_tickets = []
    for i in range(4):
        my_tickets.append(choice(tickets))
        count += 1

print(count)
