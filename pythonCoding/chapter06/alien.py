# alien_0 = {"color": "green", "point": 5}

# # 访问字典中的值
# print(alien_0["color"])
# print(alien_0["point"])

# new_point = alien_0["point"]
# print(f"You just earned {new_point} points!")

# # 添加键值对
# print(alien_0)

# alien_0["x_position"] = 0
# alien_0["y_position"] = 25
# print(alien_0)

# # 从创建一个空字典开始
# alien_0 = {}
# alien_0["color"] = "green"
# alien_0["point"] = 25

# print(alien_0)

# # 修改字典中的值
# alien_0 = {"color": "green"}
# print(f"The alien is {alien_0['color']}.")

# alien_0["color"] = "yellow"
# print(f"The alien is now {alien_0['color']}.")

# alien_0 = {"x_position": 0, "y_position": 25, "speed": "fast"}
# print(f"Original position: {alien_0['x_position']}")

# # 向右移动外星人
# # 根据当前速度确定将外星人向右移动多远
# if alien_0["speed"] == "slow":
#     x_increment = 1
# elif alien_0["speed"] == "medium":
#     x_increment = 2
# else:
#     # 这个外星人的移动速度肯定很快
#     x_increment = 3

# # 新位值为旧位置加上移动距离
# alien_0["x_position"] = alien_0["x_position"] + x_increment

# print(f"New position: {alien_0['x_position']}")

# # 删除键值对
# alien_0 = {"color": "green", "point": 5}
# print(alien_0)

# del alien_0["point"]
# print(alien_0)

# 嵌套
# alien_0 = {"color": "green", "points": 5}
# alien_1 = {"color": "yellow", "points": 10}
# alien_2 = {"color": "red", "point": 15}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)

# 创建一个用于存储外星人的空列表
aliens = []

# 创建 30 个绿色的外星人
for alien_number in range(30):
    new_alien = {"color": "green", "point": 5, "speed": "slow"}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["point"] = 10

# 显式前 5 个外星人
for alien in aliens[:5]:
    print(alien)
print("...")

# 显式创建了多少外星人
print(f"Total number of aliens: {len(aliens)}")
