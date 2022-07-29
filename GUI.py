from cgitb import text
from tkinter import *
from tkinter import messagebox
#from labelManager import toPdf

def oi(arg1):
    label = Label(root, text="Hello, " + arg1)
    label.pack()

def popup():
    Frame(None).pack()
    messagebox.showinfo("POPEI", 'Aqui tbm')

root = Tk()
root.title("Label Manager")
root.geometry("300x300")
#root.iconbitmap()

mainMenu = Menu(root)
configMenu = Menu(mainMenu, tearoff=0)
configMenu.add_command(label="Definir Pasta dos .zip", command=popup)
configMenu.add_command(label="Definir Pasta para salvar os Pdf's", command=popup)
mainMenu.add_cascade(label="Config", menu=configMenu)

clicked = StringVar()
clicked.set("Config")

zipPathLabel = Label(root, text="Zip Path")
zipPathLabel.pack()

zipEntry = Entry(root)
zipEntry.pack()

toPdfB = Button(root, text="Converter para PDF", command=oi, padx=10, pady=10)
toPdfB.pack()

root.config(menu=mainMenu)
root.mainloop()