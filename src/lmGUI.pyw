from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askdirectory
from labelManager import changeConfigs, toPdf, Prefs

subwindowSize = "300x130"

def todo():
  messagebox.showwarning("TO DO", "AINDA NÃO FIZ ESSA PARTE")

def newPathWindow(mainText, configName):
  def setPath():
    newPath = askdirectory(initialdir="")
    if (newPath):
      changeConfigs(configName, newPath)
      newWindow.destroy()

  newWindow = Toplevel(root)
  newWindow.title("")
  newWindow.minsize(300, 100)
   
  label = Label(newWindow, text=mainText)
  label.pack(padx=30, pady=10)

  submitButton = Button(newWindow, text="Definir nova pasta", command=setPath, padx=20, pady=5)
  submitButton.pack(pady=10)

def newZipWindow():
  newPathWindow("Caminho atual da pasta de downloads:\n\n" + Prefs.zipFolderPath, "ZipPath")

def newPdfWindow():
  newPathWindow("Caminho atual onde são gerados os PDFs:\n\n" + Prefs.outputPath, "OutputPath")

def setRmZip():
  changeConfigs("DeleteZip", messagebox.askquestion("Escolha uma opção", "Deseja Excluir os arquivos zips depois de converter para pdf?") == 'yes')

def setOpPdf():
  changeConfigs("OpenPdf", messagebox.askquestion("Escolha uma opção", "Deseja abrir automaticamente os pdfs convertidos?") == 'yes')

root = Tk()
root.title("Label Manager")
root.iconbitmap(default='./favicon/favicon.ico')
root.minsize(302, 167)

#Configurando o menu no topo da GUI
mainMenu = Menu(root)
configMenu = Menu(mainMenu, tearoff=0)
configMenu.add_command(label="Pasta dos Zips", command=newZipWindow)
configMenu.add_command(label="Pasta dos PDFs", command=newPdfWindow)
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