from os import listdir, mkdir, path, remove
from webbrowser import open_new_tab
from zipfile import ZipFile

from labelary import zpl2_to_pdf

PREFSPATH = './prefs.txt'


class Prefs:
  removeZip = None
  openPdf = None
  zipFolderPath = None
  outputPath = None


def toPdf():
  for zipFile in listdir(Prefs.zipFolderPath):
    if zipFile.endswith('.zip') and zipFile.startswith('Etiqueta MercadoEnvios'):
      with ZipFile(path.realpath(Prefs.zipFolderPath) + '\\' + zipFile, 'r') as zip_ref:
        with zip_ref.open('Etiqueta de envio.txt') as zpl:
          strZpl = ''
          for line in zpl:
            strZpl += str(line)

      pdfLabels = zpl2_to_pdf(strZpl)

      if not path.exists(Prefs.outputPath):
        mkdir(Prefs.outputPath)

      indexOffset = len(listdir(Prefs.outputPath))
      for i, label in enumerate(pdfLabels):
        labelPath = path.realpath(Prefs.outputPath) + '\\label{}.pdf'.format(
          i + indexOffset,
        )
        with open(labelPath, 'wb') as fid:
          fid.write(label)
          if Prefs.openPdf:
            open_new_tab('file://' + labelPath)

      if Prefs.removeZip:
        remove(path.realpath(Prefs.zipFolderPath) + '\\' + zipFile)


def getPrefs():
  if not path.exists(PREFSPATH):
    with open(PREFSPATH, 'w') as prefs:
      prefs.write('DeleteZip:True\n')
      prefs.write('OpenPdf:True\n')
      prefs.write('ZipPath:./downloads\n')
      prefs.write('OutputPath:./pdfs\n')

  with open(PREFSPATH, 'r') as prefs:
    Prefs.removeZip = prefs.readline()[10:] == 'True\n'
    Prefs.openPdf = prefs.readline()[8:] == 'True\n'
    Prefs.zipFolderPath = prefs.readline()[8:][:-1]
    Prefs.outputPath = prefs.readline()[11:][:-1]


def changeConfigs(parameter, choice):
  with open(PREFSPATH, 'r') as prefs:
    newLine = parameter + ':' + str(choice) + '\n'
    replacementString = ''
    for line in prefs:
      if parameter in line:
        replacementString += newLine
      else:
        replacementString += line

  with open(PREFSPATH, 'w') as prefs:
    prefs.write(replacementString)

  getPrefs()


getPrefs()

if __name__ == '__main__':
  import lmGUI  # noqa: F401
