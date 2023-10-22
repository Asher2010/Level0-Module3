from tkinter import Tk, simpledialog, messagebox
window = Tk()
window.withdraw()

if __name__ == '__main__':
    x = 99
    for i in range(100):
        print(x + "bottles of beer on the wall," + x + "bottles of beer.")
