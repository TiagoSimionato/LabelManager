from tkinter import Button, Frame, Label, Menu, Tk, Toplevel, messagebox
from tkinter.filedialog import askdirectory

from app.prefs import PREFS, change_prefs
from app.toPdf import toPdf

subwindowSize = '300x130'


def todo():
  messagebox.showwarning('TO DO', 'AINDA NÃO FIZ ESSA PARTE')


def newPathWindow(mainText: str, configName: str):
  def setPath():
    newPath = askdirectory(initialdir='')
    if newPath:
      change_prefs(configName, newPath)
      newWindow.destroy()

  newWindow = Toplevel(root)
  newWindow.title('')
  newWindow.minsize(300, 100)

  label = Label(newWindow, text=mainText)
  label.pack(padx=30, pady=10)

  submitButton = Button(
    newWindow,
    text='Definir nova pasta',
    command=setPath,
    padx=20,
    pady=5,
  )
  submitButton.pack(pady=10)


def newZipWindow():
  newPathWindow(
    'Caminho atual:\n\n' + PREFS.zipPath,
    'zipPath',
  )


def newPdfWindow():
  newPathWindow(
    'Caminho atual:\n\n' + PREFS.outputPath,
    'outputPath',
  )


def setRmZip():
  change_prefs(
    'deleteZip',
    messagebox.askquestion(
      'Escolha uma opção',
      'Deseja Excluir os arquivos das etiquetas depois de converter para pdf?',
    )
    == 'yes',
  )


def setOpPdf():
  change_prefs(
    'openPdf',
    messagebox.askquestion(
      'Escolha uma opção',
      'Deseja abrir automaticamente os arquivos convertidos?',
    )
    == 'yes',
  )


root = Tk()
root.title('Label Manager')
root.iconbitmap(default='./favicon/favicon.ico')
root.minsize(302, 167)

mainMenu = Menu(root)
configMenu = Menu(mainMenu, tearoff=0)
configMenu.add_command(
  label='Definir pasta com as etiquetas',
  command=newZipWindow,
)
configMenu.add_command(
  label='Definir pasta para salvar os etiquetas convertidas',
  command=newPdfWindow,
)
mainMenu.add_cascade(label='Configurações', menu=configMenu)
prefMenu = Menu(mainMenu, tearoff=0)
prefMenu.add_command(label='Excluir zips', command=setRmZip)
prefMenu.add_command(
  label='Abrir automaticamente arquivos convertidos',
  command=setOpPdf,
)
mainMenu.add_cascade(label='Preferências', menu=prefMenu)

mainFrame = Frame(root)
mainFrame.pack(padx=60, pady=30)

toPdfB = Button(
  mainFrame,
  text='Converter Etiquetas para PDF',
  command=toPdf,
  padx=10,
  pady=10,
)
toPdfB.pack()

Label(mainFrame, text='', pady=0).pack()

printButton = Button(
  mainFrame,
  text='Imprimir Etiquetas',
  command=todo,
  padx=10,
  pady=10,
)
printButton.pack()

root.config(menu=mainMenu)
