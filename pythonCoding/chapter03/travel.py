places = ["sanya", "guiyang", "dunhuang", "xinjiang", "tokyo"]
print(f"原始列表：{places}")

sorted_places = sorted(places)
print(f"字母顺序排序后列表：{sorted_places}")

sorted_places = sorted(places, reverse=True)
print(f"字母逆序排序后列表：{sorted_places}")

print(f"原始列表：{places}")

places.reverse()
print(f"反转后列表：{places}")

places.reverse()
print(f"反转后再反转列表：{places}")

places.sort()
print(f"字母顺序排序后列表：{places}")

places.sort(reverse=True)
print(f"字母逆序排序后列表：{places}")
