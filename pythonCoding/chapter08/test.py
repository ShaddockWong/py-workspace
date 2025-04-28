# # 练习8.1 消息
# def display_message():
#     print("The topic of this chapter is functions.")


# display_message()


# # 练习8.2 喜欢的书
# def favorite_book(title):
#     print(f"One of my favorite books is {title}.")


# favorite_book("Alice in Wonderland")


# # 练习8.3 T恤
# def make_shirt(size, words):
#     print(f"This T-shirt is {size} size, and {words} printed on it.")


# make_shirt("XL", "NIKE")


# # 练习8.4 大号T恤
# def make_shirt(size="L", words="I love Python"):
#     print(f"This T-shirt is {size} size, and {words} printed on it.")


# make_shirt()
# make_shirt("M")
# make_shirt("S", "I hate Python")


# # 练习8.5 城市
# def describe_city(city="Xi'an", country="china"):
#     print(f"{city} is in {country}.")


# describe_city("Reykjavik", "Iceland")
# describe_city()
# describe_city(city="Beijing")


# # 练习8.6 城市名
# def city_country(city, country):
#     print(f"{city.title()}, {country.title()}")


# city_country("xi'an", "china")
# city_country("toyko", "japan")
# city_country("london", "UK")
# city_country("new york", "USA")


# # 练习 8.7：专辑
# def make_album(singer, album, song_num=None):
#     album_info = {"singer": singer, "album": album}
#     if song_num:
#         album_info["song_num"] = song_num
#     return album_info


# print(make_album("JayZhou", "11月的萧邦", "12"))

# # 练习8.8 用户的专辑
# while True:
#     print("(enter 'q' at any time to quit)")
#     name = input("Please enter a singer name: ")
#     if name == "q":
#         break

#     album = input(f"Enter {name}'s album name: ")
#     if album == "q":
#         break

#     num = input(f"Enter a number as {album}'s song num: ")
#     if num == "q":
#         break

#     album_info = make_album(singer=name, album=album, song_num=num)
#     print(album_info)


# # 练习8.9 消息
# def show_messages(messages):
#     for message in messages:
#         print(message)


# messages = ["it's breaked", "China No.1", "MAGA"]
# show_messages(messages)


# # 练习8.10 发送消息
# def send_message(messages, sent_messages):
#     while messages:
#         message = messages.pop(0)
#         print(message)
#         sent_messages.append(message)


# messages = ["it's breaked", "China No.1", "MAGA"]
# sent_messages = []
# send_message(messages, sent_messages)

# print(messages)
# print(sent_messages)


# # 练习8.11 消息归档
# def send_message(messages, sent_messages):
#     for message in messages:
#         sent_messages.append(message)


# messages = ["it's breaked", "China No.1", "MAGA"]
# sent_messages = []
# send_message(messages, sent_messages)

# print(messages)
# print(sent_messages)


# # 练习8.12 三明治
# def make_sandwich(*ingredients):
#     print("\nMake a sandwich.")
#     for ingredient in ingredients:
#         print(f"- {ingredient}")


# make_sandwich("toast", "meat floss", "egg", "ham")
# make_sandwich("toast", "breasts", "lettuce")
# make_sandwich("breasts", "lettuce", "tomato")


# # 练习8.13 用户简介
# def build_profile(fitst, last, **user_info):
#     """创建一个字典，其中包含我们知道的有关用户的一切"""
#     user_info["first_name"] = fitst
#     user_info["last_name"] = last
#     return user_info


# user_profile = build_profile(
#     "jack", "swagger", location="Orlando", gender="male", height="185"
# )
# print(user_profile)


# # 练习8.14 汽车
# def make_car(manufacturer, model, **car_info):
#     car_info["manufacturer"] = manufacturer
#     car_info["model"] = model
#     return car_info


# car_info = make_car("subaru", "outback", color="blue", tow_package=True)
# print(car_info)

# 8.15 打印模型
