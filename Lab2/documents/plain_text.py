from .document import Document

class PlainText(Document):
    def __init__(self, name):
        super().__init__(name)