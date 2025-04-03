class TextFormatter:
    def __init__(self, document):
        self.document = document

    def apply_bold(self):
        self.document.content = f"**{self.document.content}**"

    def apply_italic(self):
        self.document.content = f"*{self.document.content}*"

    def apply_underline(self):
        self.document.content = f"__{self.document.content}__"