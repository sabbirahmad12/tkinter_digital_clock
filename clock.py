from tkinter import *
import time

root = Tk()

root.title('Digital Clock')
root.iconbitmap('C:/Users/Pacific BD/Desktop/clock.ico')

def Times():
    timeVar = time.strftime('%I: %M: %S %p')
    label.config(text = timeVar)
    label.after(100, Times)

label = Label(root, text = 'Clock', font = ('Arial', 100), bg = 'black', fg = ('red'))
label.pack()

Times()
root.mainloop()