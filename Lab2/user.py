class User:
    def __init__(self, username, documents=None):
        self.username = username
        self.documents = documents if documents is not None else []
        self.notifications = []

    def __str__(self):
        return f"User: {self.username}"


def get_user_role_for_document(user, doc_title):
    for entry in user.documents:
        if entry.get("title") == doc_title:
            return entry.get("role")
    return None
