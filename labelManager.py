import labelary # pip install labelary-mwisslead
import os
#from os import listdir, remove
import webbrowser
import zipfile
import GUI

def toPdf(zipFolderPath, outputPath, openOutput = True, removeZip = True):
    for zipFile in os.listdir(zipFolderPath):
        if zipFile.endswith(".zip"):
            with zipfile.ZipFile(os.path.realpath(zipFolderPath) + '\\' + zipFile, 'r') as zip_ref:
                with zip_ref.open("Etiqueta de envio.txt") as zpl:
                    strZpl = ""
                    for line in zpl:
                        strZpl += str(line)

            pdfLabels = labelary.zpl2_to_pdf(strZpl)

            indexOffset = len(os.listdir(outputPath))
            for i, label in enumerate(pdfLabels):
                labelPath = os.path.realpath(outputPath) + '\\label{}.pdf'.format(i + indexOffset)
                with open(labelPath, 'wb') as fid:
                    fid.write(label)
                    if openOutput:
                        webbrowser.open_new_tab('file://' + labelPath)

            if removeZip:
                os.remove(os.path.realpath(zipFolderPath) + '\\' + zipFile)


toPdf('downloads', 'pdfs')