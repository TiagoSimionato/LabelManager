from tkinter import Button, Frame, Label, Menu, Tk, Toplevel, messagebox
from tkinter.filedialog import askdirectory

from app.prefs import PREFS, change_prefs
from app.toPdf import to_pdf

subwindowSize = '300x130'


def todo():
  messagebox.showwarning('TO DO', 'AINDA NÃO FIZ ESSA PARTE')


def new_path_window(mainText: str, configName: str):
  def set_path():
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
    command=set_path,
    padx=20,
    pady=5,
  )
  submitButton.pack(pady=10)


def new_zip_window():
  new_path_window(
    'Caminho atual:\n\n' + PREFS.zipPath,
    'zipPath',
  )


def new_pdf_window():
  new_path_window(
    'Caminho atual:\n\n' + PREFS.outputPath,
    'outputPath',
  )


def set_delete_zip():
  change_prefs(
    'deleteZip',
    messagebox.askquestion(
      'Escolha uma opção',
      'Deseja Excluir os arquivos das etiquetas depois de converter para pdf?',
    )
    == 'yes',
  )


def set_open_pdf():
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

main_menu = Menu(root)
config_menu = Menu(main_menu, tearoff=0)
config_menu.add_command(
  label='Definir pasta com as etiquetas',
  command=new_zip_window,
)
config_menu.add_command(
  label='Definir pasta para salvar os etiquetas convertidas',
  command=new_pdf_window,
)
main_menu.add_cascade(label='Configurações', menu=config_menu)
pref_menu = Menu(main_menu, tearoff=0)
pref_menu.add_command(label='Excluir zips', command=set_delete_zip)
pref_menu.add_command(
  label='Abrir automaticamente arquivos convertidos',
  command=set_open_pdf,
)
main_menu.add_cascade(label='Preferências', menu=pref_menu)

main_frame = Frame(root)
main_frame.pack(padx=60, pady=30)

to_pdf_button = Button(
  main_frame,
  text='Converter Etiquetas para PDF',
  command=to_pdf,
  padx=10,
  pady=10,
)
to_pdf_button.pack()

Label(main_frame, text='', pady=0).pack()

# print_button = Button(
#   main_frame,
#   text='Imprimir Etiquetas',
#   command=todo,
#   padx=10,
#   pady=10,
# )
# print_button.pack()

root.config(menu=main_menu)
