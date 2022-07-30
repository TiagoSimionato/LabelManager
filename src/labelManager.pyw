from labelary import zpl2_to_pdf # pip install labelary-mwisslead
from os import listdir, remove, mkdir, path
from webbrowser import open_new_tab
from zipfile import ZipFile

def toPdf():
    for zipFile in listdir(zipFolderPath):
        if zipFile.endswith(".zip") and zipFile.startswith("Etiqueta MercadoEnvios"):
            with ZipFile(path.realpath(zipFolderPath) + '\\' + zipFile, 'r') as zip_ref:
                with zip_ref.open("Etiqueta de envio.txt") as zpl:
                    strZpl = ""
                    for line in zpl:
                        strZpl += str(line)

            pdfLabels = zpl2_to_pdf(strZpl)

            if (not path.exists(outputPath)):
                mkdir(outputPath)
                
            indexOffset = len(listdir(outputPath))
            for i, label in enumerate(pdfLabels):
                labelPath = path.realpath(outputPath) + '\\label{}.pdf'.format(i + indexOffset)
                with open(labelPath, 'wb') as fid:
                    fid.write(label)
                    if openPdf:
                        open_new_tab('file://' + labelPath)

            if removeZip:
                remove(path.realpath(zipFolderPath) + '\\' + zipFile)

def getPrefs():
    if (not path.exists('./prefs')):
        mkdir('./prefs')

    prefsPath = './prefs/prefs.txt'
    if (not path.exists(prefsPath)):
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
import lmGUI