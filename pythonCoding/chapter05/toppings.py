# requested_topping = "mushrooms"
# if requested_topping != "anchovies":
#     print("Hold the anchovies!")

# requested_toppings = ["mushrooms", "extra cheese"]

# if "mushrooms" in requested_toppings:
#     print("Adding mushrooms.")
# if "pepperoni" in requested_toppings:
#     print("Adding pepperoni.")
# if "extra cheese" in requested_toppings:
#     print("Adding extra cheese.")

# print("\nFinished making your pizza!")

# requested_toppings = ["mushrooms", "green peppers", "extra cheese"]

# for requested_topping in requested_toppings:
#     print(f"Add {requested_topping}.")

# print("\nFinished making your pizza!")

# # 检查特殊元素
# requested_toppings = ["mushrooms", "green peppers", "extra cheese"]

# for requested_topping in requested_toppings:
#     if requested_topping == "green peppers":
#         print("Sorry, we are out of green peppers right now.")
#     else:
#         print(f"Add {requested_topping}.")

# print("\nFinished making your pizza!")

# # 确定列表非空
# requested_toppings = []

# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print(f"Adding {requested_topping}.")
#     print("\nFinished marking your pizza!")
# else:
#     print("Are you sure you want a plain pizza?")

# 使用多个列表
available_toppings = [
    "mushrooms",
    "olives",
    "green peppers",
    "pepperoni",
    "pineapple",
    "extra cheese",
]

requested_toppings = ["mushrooms", "french fries", "extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")
