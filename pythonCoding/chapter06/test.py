# # 练习 6.1：人
# person = {"first_name": "Jack", "last_name": "Swagger", "age": 25, "city": "Edmond"}
# print(person)

# # 练习 6.2：喜欢的数 1
# favorite_nums = {"jack": 3, "zara": 7, "coco": 6, "eva": 1, "logistic": 3}
# print(favorite_nums)

# # 练习 6.3：词汇表
# words_table = {
#     "int": "整数型",
#     "double": "浮点型",
#     "char": "字符型",
#     "boolean": "布尔型",
#     "array": "数组型",
# }

# print(f"int\t\tdouble\t\tchar\t\tboolean\t\tarray")
# print(
#     f"{words_table['int']}\t\t{words_table['double']}\t\t{words_table['char']}\t\t{words_table['boolean']}\t\t{words_table['array']}"
# )

# # 练习 6.4：词汇表2
# words_table = {
#     "int": "整数型",
#     "double": "浮点型",
#     "char": "字符型",
#     "string": "字符串型",
#     "boolean": "布尔型",
#     "array": "数组型",
#     "set": "集合型",
# }
# for key, value in words_table.items():
#     print(f"类型：{key}\t说明：{value}")

# # 练习 6.5 河流
# rivers = {
#     "nile": "egypt",
#     "amazon": "brazil",
#     "rhine": "germany",
# }

# for river, county in rivers.items():
#     print(f"The {river.title()} runs through {county.title()}.")

# for river in rivers.keys():
#     print(f"{river.title()}")

# for county in rivers.values():
#     print(f"{county.title()}")

# 6.6 调查
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}
names = ["jen", "ellan", "phil", "jojo"]

for name, language in favorite_languages.items():
    if name in names:
        print(f"Thank you, {name.title()}!")
    else:
        print(f"Hello {name.title() },we invite you take the survey.")
