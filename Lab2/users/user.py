class User:
    def __init__(self, username, password, role="Viewer"):
        self.username = username
        self.password = password
        self.role = role

    def has_permission(self, action):
        permissions = {
            "Viewer": ["open"],
            "Editor": ["open", "edit"],
            "Admin": ["open", "edit", "delete", "manage"],
        }
        return action in permissions.get(self.role, [])