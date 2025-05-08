import json

def save_users(users, filename="users.json"):
    data = []
    for user in users:
        user_data = {
            "username": user.username,
            "documents": user.documents 
        }
        data.append(user_data)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print(f"Пользователи успешно сохранены в файл '{filename}'.")


def load_users(filename="users.json"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        from user import User  
        users = []
        for item in data:
            u = User(item["username"], documents=item.get("documents", []))
            users.append(u)
        print(f"Пользователи успешно загружены из файла '{filename}'.")
        return users, data
    except (FileNotFoundError, json.JSONDecodeError):
        print(f"Файл '{filename}' с пользователями не найден или пуст.")
        return [], []
