from os import listdir, mkdir, path, remove
from webbrowser import open_new_tab
from zipfile import ZipFile

from labelary import zpl2_to_pdf

from app.prefs import PREFS


def to_pdf():
  for zip_file in listdir(PREFS.zipPath):
    if zip_file.endswith('.zip') and zip_file.startswith('Etiqueta MercadoEnvios'):
      with ZipFile(path.realpath(PREFS.zipPath) + '\\' + zip_file, 'r') as zip_ref:
        with zip_ref.open('Etiqueta de envio.txt') as zpl:
          strZpl = ''
          for line in zpl:
            strZpl += str(line)

      pdf_labels = zpl2_to_pdf(strZpl)

      if not path.exists(PREFS.outputPath):
        mkdir(PREFS.outputPath)

      index_offset = len(listdir(PREFS.outputPath))
      for i, label in enumerate(pdf_labels):
        label_Path = path.realpath(PREFS.outputPath) + '\\label{}.pdf'.format(
          i + index_offset,
        )
        with open(label_Path, 'wb') as fid:
          fid.write(label)
          if PREFS.openFile:
            open_new_tab('file://' + label_Path)

      if PREFS.deleteZip:
        remove(path.realpath(PREFS.zipPath) + '\\' + zip_file)
