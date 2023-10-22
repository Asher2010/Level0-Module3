from tkinter import Tk, simpledialog, messagebox
window = Tk()
window.withdraw()

if __name__ == '__main__':
    # TODO: Look at the AreYouHappy.png image
    #       Use pop-ups to recreate the chart using if and elif statements
    question = simpledialog.askstring(title=None, prompt="Are you happy?")
    if question == "Yes":
        messagebox.showinfo(title=None, message="Keep doing whatever you're doing")

    elif question == "No":
        question2 = simpledialog.askstring(title=None, prompt="Do you want to be happy?")
        if question2 == "Yes":
            messagebox.showinfo(title=None, message="Change something")
        elif question2 == "No":
            messagebox.showinfo(title=None, message="Keep doing whatever you're doing")
    pass
