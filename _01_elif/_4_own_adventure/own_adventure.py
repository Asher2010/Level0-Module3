from tkinter import simpledialog, messagebox, Tk

# TODO Tell the user a story, but give them options so they can decide the
#  path of the plot.
#  Use pop-ups, if statements, and your imagination to make an interesting
#  story
window = Tk()
window.withdraw()
messagebox.showinfo(title=None, message="You stand at the edge of an ancient, enchanted forest. The path splits into two. Which way will you choose?")
question1 = simpledialog.askstring(title=None, prompt="Follow the left path or take the right path?")
if question1 == "Follow the left path":
    messagebox.showinfo(title=None, message="You decide to follow the left path. As you walk deeper into the forest, you notice a strange, glowing mushroom. It emits a soft, inviting light. What will you do?")
    option1 = simpledialog.askstring(title=None, prompt="Approach the glowing mushroom or continue down the path, ignoring the mushroom")
    if option1 == "Approach the glowing mushroom":
        messagebox.showinfo(title=None, message="You approach the glowing mushroom, and as you get closer, it suddenly sprouts tiny wings and starts to fly away. It leads you to a hidden grove with a hidden treasure chest. You have found a chest full of valuable gems! Congratulations, you've had a successful adventure.")
    elif option1 == "Continue down the path, ignoring the mushroom":
        messagebox.showinfo(title=None, message="You continue down the path, ignoring the mushroom. The path leads you deeper into the forest, and you encounter a mischievous gnome who guides you safely through the woods. You make it to the other side of the forest unscathed.")
elif question1 == "Take the right path":
    messagebox.showinfo(title=None, message="You choose the right path, and it leads you to a beautiful, tranquil lake. A small boat is waiting on the shore. What will you do?")
    option2 = simpledialog.askstring(title=None, prompt="Get in the boat and row across the lake or explore the area around the lake on foot?")
    if option2 == "Get in the boat and row across the lake":
        messagebox.showinfo(title=None, message="You choose the right path, and it leads you to a beautiful, tranquil lake. A small boat is waiting on the shore. What will you do?")
    elif option2 == "Explore the area around the lake on foot":
        messagebox.showinfo(title=None, message="You choose the right path, and it leads you to a beautiful, tranquil lake. A small boat is waiting on the shore. What will you do?")
