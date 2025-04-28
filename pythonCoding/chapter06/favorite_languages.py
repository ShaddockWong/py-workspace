# favorite_languages = {
#     "jen": "python",
#     "sarah": "c",
#     "edward": "rust",
#     "phil": "python",
# }

# language = favorite_languages["sarah"].title()
# print(f"Sarah's favorite language is {language}.")

# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}")

# # 遍历字典中的所有键
# friends = ["phil", "sarah"]
# for name in favorite_languages.keys():
#     print(f"Hi,{name.title()}.")

#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}!")

# if "erin" not in favorite_languages.keys():
#     print("Erin, please take our poll!")

# # 按特定顺序遍历字典中的所有键
# favorite_languages = {
#     "jen": "python",
#     "sarah": "c",
#     "edward": "rust",
#     "phil": "python",
# }

# for name in sorted(favorite_languages.keys()):
#     print(f"{name.title()}, thank you for taking the poll.")

# # 遍历字典中的所有值
# favorite_languages = {
#     "jen": "python",
#     "sarah": "c",
#     "edward": "rust",
#     "phil": "python",
# }

# print("The following languages have been mentioned:")
# # 使用set()可以对数据进行去重
# for language in set(favorite_languages.values()):
#     print(language.title())

# 在字典中存储列表
favorite_languages = {
    "jen": ["python", "rust"],
    "sarsh": ["c"],
    "edward": ["rust", "go"],
    "phil": ["python", "haskell"],
}

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"\n{name.title()}'s favorite languages is {languages[0]}")
    else:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")
