with open('input.txt', "r", encoding="utf-8") as f:
    list_users = f.readlines()

user_info_dict = {}

for user_info in list_users:
    user_info = user_info.strip().split(" ")
    user = user_info[0]
    print(user)
    password = user_info[1]
    print(password)
    if not user or not password:
        print(f'No info for {user}{password}')
    else:
        print("Ok")
        user_info_dict[user] = password

print(user_info_dict)
