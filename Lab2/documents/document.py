class Document:
    def __init__(self, name):
        self.name = name
        self.content = ""

    def add_content(self, text):
        self.content += text

    def clear_content(self):
        self.content = ""

    def get_content(self):
        return self.content

    def save(self, storage):
        storage.save(self.name, self.content)

    def load(self, storage):
        self.content = storage.load(self.name)