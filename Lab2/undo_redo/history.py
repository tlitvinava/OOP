class History:
    def __init__(self):
        self.commands = []
        self.index = -1

    def execute_command(self, command):
        command.execute()
        self.commands = self.commands[:self.index + 1]  # Удаляем действия впереди
        self.commands.append(command)
        self.index += 1

    def undo(self):
        if self.index >= 0:
            self.commands[self.index].undo()
            self.index -= 1

    def redo(self):
        if self.index + 1 < len(self.commands):
            self.index += 1
            self.commands[self.index].execute()