from labelary import zpl2_to_pdf # pip install labelary-mwisslead
from os import listdir, remove, mkdir, path
from webbrowser import open_new_tab
from zipfile import ZipFile

class Prefs:
  removeZip     = None
  openPdf       = None
  zipFolderPath = None
  outputPath    = None

def toPdf():
  for zipFile in listdir(Prefs.zipFolderPath):
    if zipFile.endswith(".zip") and zipFile.startswith("Etiqueta MercadoEnvios"):
      with ZipFile(path.realpath(Prefs.zipFolderPath) + '\\' + zipFile, 'r') as zip_ref:
        with zip_ref.open("Etiqueta de envio.txt") as zpl:
          strZpl = ""
          for line in zpl:
            strZpl += str(line)

      pdfLabels = zpl2_to_pdf(strZpl)

      if (not path.exists(Prefs.outputPath)):
        mkdir(Prefs.outputPath)
                
      indexOffset = len(listdir(Prefs.outputPath))
      for i, label in enumerate(pdfLabels):
        labelPath = path.realpath(Prefs.outputPath) + '\\label{}.pdf'.format(i + indexOffset)
        with open(labelPath, 'wb') as fid:
          fid.write(label)
          if Prefs.openPdf:
            open_new_tab('file://' + labelPath)

      if Prefs.removeZip:
        remove(path.realpath(Prefs.zipFolderPath) + '\\' + zipFile)

def getPrefs():
  prefsPath = './prefs.txt'
  if (not path.exists(prefsPath)):
    with open(prefsPath, 'w') as prefs:
      prefs.write("DeleteZip:True\n")
      prefs.write("OpenPdf:True\n")
      prefs.write("ZipPath:./downloads\n")
      prefs.write("OutputPath:./pdfs\n")

  with open(prefsPath, 'r') as prefs:
    Prefs.removeZip = prefs.readline()[10:] == "True\n"
    Prefs.openPdf = prefs.readline()[8:] == "True\n"
    Prefs.zipFolderPath = prefs.readline()[8:][:-1]
    Prefs.outputPath = prefs.readline()[11:][:-1]

def changeConfigs(parameter, choice):
  with open('./prefs/prefs.txt', 'r') as prefs:
    newLine = parameter + ":" + str(choice) + "\n"
    replacementString = ""
    for line in prefs:
      if (parameter in line):
        replacementString += newLine
      else:
        replacementString += line

  with open('./prefs/prefs.txt', 'w') as prefs:
    prefs.write(replacementString)

  #Atualizo as variaveis    
  getPrefs()

getPrefs()

if(__name__ == '__main__'):
  import lmGUI