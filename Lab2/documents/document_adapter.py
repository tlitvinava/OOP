import json
import os

class DocumentAdapter:
    def save(self, document, format_type):
        if format_type == "txt":
            with open(f"{document.name}.txt", "w") as file:
                file.write(document.get_content())
        elif format_type == "json":
            with open(f"{document.name}.json", "w") as file:
                json.dump({"content": document.get_content()}, file)
        elif format_type == "xml":
            content = f"<document><content>{document.get_content()}</content></document>"
            with open(f"{document.name}.xml", "w") as file:
                file.write(content)
        else:
            raise ValueError(f"Неизвестный формат: {format_type}")