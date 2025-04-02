import json
import os

class LocalStorage:
    def save(self, name, content):
        with open(f"{name}.txt", "w") as file:
            file.write(content)

    def load(self, name):
        if os.path.exists(f"{name}.txt"):
            with open(f"{name}.txt", "r") as file:
                return file.read()
        return ""