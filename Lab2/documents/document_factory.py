from .plain_text import PlainText
from .markdown import Markdown
from .rich_text import RichText

class DocumentFactory:
    @staticmethod
    def create_document(doc_type, name):
        if doc_type == "plain":
            return PlainText(name)
        elif doc_type == "markdown":
            return Markdown(name)
        elif doc_type == "rich":
            return RichText(name)
        else:
            raise ValueError(f"Неизвестный тип документа: {doc_type}")