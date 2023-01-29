class Dialogue():
    def __init__(self, dialogue_file):
        self.dialogue = self.load_dialogue(dialogue_file)
        self.current_line = 0

    def load_dialogue(self, dialogue_file):
        with open(dialogue_file, "r") as f:
            lines = f.readlines()
        return lines
    

    def display_line(self):
        print(self.dialogue[self.current_line])

    def next_line(self):
        self.current_line += 1

    def run(self):
        while self.current_line < len(self.dialogue):
            self.display_line()
            input("Press Enter to continue...")
            self.next_line() 

dialogue = Dialogue("dialogue.txt")
dialogue.run()  