class TextOperations:
    def __init__(self, document):
        self.document = document
        self.clipboard = ""

    def insert_text(self, text):
        self.document.add_content(text)

    def cut_text(self, start, end):
        self.clipboard = self.document.content[start:end]
        self.document.content = self.document.content[:start] + self.document.content[end:]

    def copy_text(self, start, end):
        self.clipboard = self.document.content[start:end]

    def paste_text(self):
        self.document.add_content(self.clipboard)