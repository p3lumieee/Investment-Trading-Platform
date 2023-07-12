from tkinter import *

# setup
root = Tk()
root.title("Menu system")

# create frames
menuFrame = Frame(root)
menuFrame.grid(row=0, column=0)
itemFrame = Frame(root)
itemFrame.grid(row=0, column=1)


# clear screen function
def clear(object):
    slaves = object.grid_slaves()
    for x in slaves:
        x.destroy()


# different items on different menus
def menu1():
    clear(itemFrame)
    Label(itemFrame, text="Hello").grid(row=0, column=0)
    Entry(itemFrame).grid(row=1, column=0)


def menu2():
    clear(itemFrame)
    Checkbutton(itemFrame, text="greetings").grid(row=0, column=0)
    Label(itemFrame, text="Menu2").grid(row=1, column=0)


# persistent menu buttons
menuButton1 = Button(menuFrame, text="menu1", command=menu1).grid(row=0, column=0)
menuButton2 = Button(menuFrame, text="menu2", command=menu2).grid(row=1, column=0)

mainloop()
