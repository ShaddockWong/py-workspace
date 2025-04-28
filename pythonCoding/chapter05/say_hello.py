# usernames = ["devops", "pc", "admin", "player", "rapper"]
# usernames = []

# if usernames:
#     for username in usernames:
#         if username == "admin":
#             print(f"Hello {username}, would you like to see a status report?")
#         else:
#             print(f"Hello {username.title()}, thank you for logging in again.")
# else:
#     print("We need to find some users!")

# 检查用户名
current_users = ["devops", "pc", "admin", "Player", "Rapper"]
new_users = ["player", "geeker", "rapper", "worker", "master"]

current_users_bak = []
for user in current_users:
    current_users_bak.append(user.lower())

for user in new_users:
    if user.lower() in current_users_bak:
        print(f"Username {user} is used, You should enter other username.")
    else:
        print(f"{user} is not used.")
