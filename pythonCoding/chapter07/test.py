# # 7.4 披萨配料
# flag = True
# while flag:
#     p = input("Please enter a topping: ")
#     if p == "quit":
#         flag = False
#     else:
#         print(f"We add {p} on the pizza.")

# 7.5 电影票
while True:
    age = int(input("Please tell me your age: "))
    if age < 3:
        print(f"Your are free!")
    elif 12 > age >= 3:
        print(f"10$ Please.")
    elif 12 <= age:
        print(f"15$ Please.")
