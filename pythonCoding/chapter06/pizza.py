# 在字典中存储列表
# 存储顾客所点披萨的信息
pizza = {
    "crust": "thick",
    "topppings": ["mushrooms", "extra cheese"],
}

# 概述顾客点的披萨
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
for topping in pizza["topppings"]:
    print(f"\t{topping}")
