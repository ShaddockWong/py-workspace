names = ["duan shaojia", "yin dongdong", "quan xiaoning"]
# for name in names:
#     print(f"Welcome {name.title()}, Come and have dinner with me.")

not_come_name = "quan xiaoning"
print(f"Miss {not_come_name.title()} Unable to keep an appointment.")

names.remove(not_come_name)
names.append("chang xiaolong")

for name in names:
    print(f"Welcome {name.title()}, Come and have dinner with me.")

print("I find a bigest table.")

names.insert(0, "li jing")
names.insert(2, "wang yibo")
names.append("wang xiao")

for name in names:
    print(f"Welcome {name.title()}, Come and have dinner with me.")

print(f"We've had {len(names)} guests in total")

print("The new table couldn't be delivered on time, so I had to invite two people.")
cant_name = names.pop()
print(f"I'm sorry {cant_name.title()}, I can't invite you to dinner.")
cant_name = names.pop()
print(f"I'm sorry {cant_name.title()}, I can't invite you to dinner.")
cant_name = names.pop()
print(f"I'm sorry {cant_name.title()}, I can't invite you to dinner.")
cant_name = names.pop()
print(f"I'm sorry {cant_name.title()}, I can't invite you to dinner.")

for name in names:
    print(f"Welcome {name.title()}, Come and have dinner with me.")

del names[0]
del names[0]
print(names)
