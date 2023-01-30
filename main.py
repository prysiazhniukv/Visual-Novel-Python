import tkinter as Tk
from PIL import Image, ImageTk, ImageDraw


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


# Create main window
root = Tk.Tk()
root.title("Visual Novel")

# Initialize game state
current_scene = 1

# Create label to display text
label = Tk.Label(root, text="Scene 1")
label.pack()

# Create button to advance to next scene


def advance_scene():
    global current_scene
    current_scene += 1
    label["text"] = f"Scene {current_scene}"


button = Tk.Button(root, text="Next Scene", command=advance_scene)
button.pack()


def scene_1():
    background_image1 = Image.open("backgrounds/Train_Night.png")

    background_image1.thumbnail((500, 500), Image.ANTIALIAS)
    background_image1 = ImageTk.PhotoImage(background_image1)

    # Load anime character image with transparent background
    character_image1 = Image.open(
    "charachters/Miki Casual/Miki_A_Casual_Smile_Blush.png").convert("RGBA")
    character_image1 = character_image1.resize((200, 200), Image.ANTIALIAS)
    character_mask = Image.new("L", character_image1.size, 0)
    character_draw = ImageDraw.Draw(character_mask)
    character_draw.rectangle((0, 0) + character_image1.size, fill=255)
    character_image1.putalpha(character_mask)
    character_image1 = ImageTk.PhotoImage(character_image1)

    # Create label to display text and images
    label1 = Tk.Label(root, image=background_image1)
    label1.image = background_image1  # Keep reference to avoid garbage collection
    label1.pack()

    character_label1 = Tk.Label(root, image=character_image1, bg="white")
    character_label1.place(x=150, y=100)

    dialogue_label1 = Tk.Label(
        root, text="Hello!", font=("Helvetica", 16), bg="white")
    dialogue_label1.place(x=200, y=300)


scene_1()

# Start event loop
root.mainloop()


# dialogue = Dialogue("dialogue.txt")
# dialogue.run()
