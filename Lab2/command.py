class Command:
    def __init__(self, editor):
        self.editor = editor

    def execute(self):
        raise NotImplementedError("You should implement this method.")

    def undo(self):
        raise NotImplementedError("You should implement this method.")
    
class UndoCommand(Command):
    def execute(self):
        self.editor.undo()

class RedoCommand(Command):
    def execute(self):
        self.editor.redo()    