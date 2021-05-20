import pyautogui

import tkinter as tk

from tkinter.filedialog import *


root = tk.Tk()

window = tk.Canvas(root, width=200, height=100)
window.pack()
root.title("Screenshot Tool")


def new_shot():
    screen_shot = pyautogui.screenshot()
    save_path = asksaveasfilename()
    screen_shot.save(save_path+"screencap.png")

ss_button= tk.Button(text="Take Screenshot", command = new_shot, font=15)
window.create_window(100,50,window=ss_button)

root.mainloop()





