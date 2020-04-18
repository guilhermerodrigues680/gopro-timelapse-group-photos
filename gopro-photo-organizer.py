# GoPro time-lapse photo organizer in folders
# Organizador de fotos time-lapse da GoPro em pastas
# Por: Guilherme Rodrigues -> github.com/guilhermerodrigues680


import os
import sys


# Retorna somente os arquivos do directorio
def listFilesInDir(mypath):
    # Usando a compressao de lista do Python, recebe somente os arquivos
    onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
    
    return onlyfiles
    

# Retorna uma lista com grupos de fotos time-lapse
def listGroups(listPhotoFiles):
    grupo = set()

    # Preenche o set() com valores unicos - EX de foto time-lapse: G0261752.JPG
    for ph in listPhotoFiles:
        if ph[1].isdigit():
            grupo.add(ph[:4])

    return grupo


# Cria as pastas para cada grupo
def createFolders(grupo, mypath):
    for g in grupo:
        try:
            os.mkdir(os.path.join(mypath, g))
        except OSError:
            print("O diretorio %s nao foi criado" % g)


# Move as fotos time-lapse de um grupo para a pasta
def groupPhotosInFolder(listPhotoFiles, mypath):
    listTLPhotoFiles = [ph for ph in listPhotoFiles if ph[1].isdigit()]
    
    for ph in listTLPhotoFiles:
        os.rename(os.path.join(mypath, ph), os.path.join(mypath, ph[:4], ph))


# Rotina principal de execucao do programa
def main(argv):
    if not argv:
        raise Exception('É preciso especificar o diretorios que contém as fotos')

    mypath = argv[0]
    
    listPhotoFiles = listFilesInDir(mypath)
    print("Arquivos:\n%s" % listPhotoFiles)
    groups = listGroups(listPhotoFiles)
    print("Grupos:\n%s" % groups)
    createFolders(groups, mypath)
    groupPhotosInFolder(listPhotoFiles, mypath)


main(sys.argv[1:])