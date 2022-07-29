import labelary # pip install labelary-mwisslead
import os
#from os import listdir, remove, path
from webbrowser import open_new_tab
import zipfile

def toPdf():
    for zipFile in os.listdir(zipFolderPath):
        if zipFile.endswith(".zip") and zipFile.startswith("Etiqueta MercadoEnvios"):
            with zipfile.ZipFile(os.path.realpath(zipFolderPath) + '\\' + zipFile, 'r') as zip_ref:
                with zip_ref.open("Etiqueta de envio.txt") as zpl:
                    strZpl = ""
                    for line in zpl:
                        strZpl += str(line)

            pdfLabels = labelary.zpl2_to_pdf(strZpl)

            if (not os.path.exists(outputPath)):
                os.mkdir(outputPath)
                
            indexOffset = len(os.listdir(outputPath))
            for i, label in enumerate(pdfLabels):
                labelPath = os.path.realpath(outputPath) + '\\label{}.pdf'.format(i + indexOffset)
                with open(labelPath, 'wb') as fid:
                    fid.write(label)
                    if openPdf:
                        open_new_tab('file://' + labelPath)

            if removeZip:
                os.remove(os.path.realpath(zipFolderPath) + '\\' + zipFile)

def getPrefs():
    if (not os.path.exists('./prefs')):
        os.mkdir('./prefs')

    prefsPath = './prefs/prefs.txt'
    if (not os.path.exists(prefsPath)):
            with open(prefsPath, 'w') as prefs:
                prefs.write("DeleteZip:True\n")
                prefs.write("OpenPdf:True\n")
                prefs.write("ZipPath:./downloads\n")
                prefs.write("OutputPath:./pdfs\n")

    with open(prefsPath, 'r') as prefs:
        global removeZip 
        removeZip = prefs.readline()[10:] == "True\n"
        global openPdf
        openPdf = prefs.readline()[8:] == "True\n"
        global zipFolderPath
        zipFolderPath = prefs.readline()[8:][:-1]
        global outputPath
        outputPath = prefs.readline()[11:][:-1]

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
print(removeZip)
print(openPdf)
print(zipFolderPath)
print(outputPath)
import lmGUI