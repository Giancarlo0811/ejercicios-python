import os

currentDir = os.path.dirname(__file__)

def writeToFile(filename, text):
    filePath = os.path.join(currentDir, filename)
    # abrir archivo en modo write 'w'
    with open(filePath, 'w') as fileObj:
        # escribir texto en el archivo
        fileObj.write(text)

def appendToFile(filename, text):
    filePath = os.path.join(currentDir, filename)
    # abrir archivo en modo append 'a'
    with open(filePath, 'a') as fileObj:
        # escribir texto al final del archivo
        fileObj.write(text)

def readFromFile(filename):
    filePath = os.path.join(currentDir, filename)
    # abrir archivo en modo read 'r'
    with open(filePath, 'r') as fileObj:
        # leer texto del archivo y devolverlo como un string
        return fileObj.read()
    
# tests
writeToFile('greet.txt', 'Hello!\n')
appendToFile('greet.txt', 'Goodbye!\n')
assert readFromFile('greet.txt') == 'Hello!\nGoodbye!\n'