from tkinter import *


class Window:
    def __init__(self):
        root = Tk()
        menu = Menu(root)
        root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label='file', menu=filemenu)
        filemenu.add_command(label='new', command=self.callbacl)
        filemenu.add_separator()
        filemenu.add_command(label='oepn', command=self.callbacl)
        root.mainloop()

    def callbacl():
        print('sss')


Window()