pizzas = ["Mushroom", "Pepperoni", "Hawaiian"]
# for pizza in pizzas:
#     print(f"I like {pizza} pizza.")

# print("I really love pizza!")

friend_pizzas = pizzas[:]

pizzas.append("Supreme")
friend_pizzas.insert(0, "Mediterranean")

for pizza in pizzas:
    print(f"My favorite pizzas are:{pizza}")

print()

for pizza in friend_pizzas:
    print(f"My friend's favorite pizzas are:{pizza}")
