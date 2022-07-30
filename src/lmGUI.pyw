from tkinter import *
from tkinter import messagebox
from labelManager import changeConfigs, toPdf, zipFolderPath, outputPath

subwindowSize = "300x130"

def todo():
    messagebox.showwarning("TO DO", "AINDA NÃO FIZ ESSA PARTE")

def newZipWindow():
    def setPath():
        changeConfigs("ZipPath", entry.get())
        newWindow.destroy()

    newWindow = Toplevel(root)
    newWindow.title("")
    
    label = Label(newWindow, text="Caminho atual:\n\n" + zipFolderPath + "\n\nDigite o novo caminho da pasta de downloads")
    label.pack(padx=30, pady=20)

    entry = Entry(newWindow)
    entry.pack()

    submitButton = Button(newWindow, text="OK", command=setPath, padx=20, pady=5)
    submitButton.pack(pady=20)

    entry.focus()

def newPdfWindow():
    def setPath():
        changeConfigs("OutputPath", entry.get())
        newWindow.destroy()

    newWindow = Toplevel(root)
    newWindow.title("")
    
    label = Label(newWindow, text="Caminho atual:\n\n" + outputPath + "\n\nDigite o novo caminho da pasta de pdfs")
    label.pack(padx=30, pady=20)

    entry = Entry(newWindow)
    entry.pack()

    submitButton = Button(newWindow, text="OK", command=setPath, padx=20, pady=5)
    submitButton.pack(pady=20)

    entry.focus()

def setRmZip():
    changeConfigs("DeleteZip", messagebox.askquestion("Escolha uma opção", "Deseja Excluir os arquivos zips depois de converter para pdf?") == 'yes')

def setOpPdf():
    changeConfigs("OpenPdf", messagebox.askquestion("Escolha uma opção", "Deseja abrir automaticamente os pdfs convertidos?") == 'yes')

root = Tk()
root.title("Label Manager")
root.iconbitmap(default='D:/ESTUDO/repositorios/LabelManager/favicon/favicon.ico')

#Configurando o menu no topo da GUI
mainMenu = Menu(root)
configMenu = Menu(mainMenu, tearoff=0)
configMenu.add_command(label="Definir Pasta dos Zips", command=newZipWindow)
configMenu.add_command(label="Definir Pasta dos Pdfs", command=newPdfWindow)
mainMenu.add_cascade(label="Configurações", menu=configMenu)
prefMenu = Menu(mainMenu, tearoff=0)
prefMenu.add_command(label="Excluir zips?", command=setRmZip)
prefMenu.add_command(label="Abris pdfs?", command=setOpPdf)
mainMenu.add_cascade(label="Preferências", menu=prefMenu)

mainFrame = Frame(root)
mainFrame.pack(padx=60, pady=30)

toPdfB = Button(mainFrame, text="Converter Etiquetas para PDF", command=toPdf, padx=10, pady=10)
toPdfB.pack()

Label(mainFrame, text="", pady=0).pack()

printButton = Button(mainFrame, text="Imprimir Etiquetas", command=todo, padx=10, pady=10)
printButton.pack()

root.config(menu=mainMenu)
root.mainloop()