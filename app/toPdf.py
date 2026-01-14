from os import listdir, mkdir, path, remove
from webbrowser import open_new_tab
from zipfile import ZipFile

from labelary import zpl2_to_pdf

from app.prefs import PREFS


def toPdf():
  for zipFile in listdir(PREFS.zipPath):
    if zipFile.endswith('.zip') and zipFile.startswith('Etiqueta MercadoEnvios'):
      with ZipFile(path.realpath(PREFS.zipPath) + '\\' + zipFile, 'r') as zip_ref:
        with zip_ref.open('Etiqueta de envio.txt') as zpl:
          strZpl = ''
          for line in zpl:
            strZpl += str(line)

      pdfLabels = zpl2_to_pdf(strZpl)

      if not path.exists(PREFS.outputPath):
        mkdir(PREFS.outputPath)

      indexOffset = len(listdir(PREFS.outputPath))
      for i, label in enumerate(pdfLabels):
        labelPath = path.realpath(PREFS.outputPath) + '\\label{}.pdf'.format(
          i + indexOffset,
        )
        with open(labelPath, 'wb') as fid:
          fid.write(label)
          if PREFS.openPdf:
            open_new_tab('file://' + labelPath)

      if PREFS.deleteZip:
        remove(path.realpath(PREFS.zipPath) + '\\' + zipFile)
