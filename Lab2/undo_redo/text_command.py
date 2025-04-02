from .command import Command

class TextCommand(Command):
    def __init__(self, document, action, text=""):
        self.document = document
        self.action = action
        self.text = text

    def execute(self):
        if self.action == "add":
            self.document.add_content(self.text)
        elif self.action == "remove":
            self.document.content = self.document.content[:-len(self.text)]

    def undo(self):
        if self.action == "add":
            self.document.content = self.document.content[:-len(self.text)]
        elif self.action == "remove":
            self.document.add_content(self.text)