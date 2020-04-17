import os
import sys

# DIRECTORY_PHOTOS = '/Users/guilherme/Desktop/Gopro-Google-Photos'
DIRECTORY_PHOTOS = '/Users/guilherme/Desktop/python-organize-gopro/pasta'
# print(os.getcwd())

# mypath = os.getcwd()
mypath = DIRECTORY_PHOTOS
# print(os.path.dirname(DIRECTORY_PHOTOS))


def listFilesInDir():
    # print(os.listdir(mypath))
    # for f in os.listdir(mypath):
    #     print(f)
    #     if os.path.isfile(os.path.join(mypath, f)):
    #         print('isfile')
    #     elif os.path.isdir(os.path.join(mypath, f)):
    #         print('isdir')

    # Usando a compressao de lista do Python, recebe somente os arquivos
    onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
    print(onlyfiles)
    
    return onlyfiles
    

def listGroups():
    photos = listFilesInDir()

    grupo = set()
    for ph in photos:    
        
        # print(ph)
        # print(ph[:4])
        grupo.add(ph[:4])
        if "GO" not in ph:
            pass
        if "G026" in ph:
            # print('ok')
            # grupo.append(ph)
            pass

        # print(grupo)

    return grupo


def createFolders(grupo):
    for g in grupo:
        # print(g)
        try:
            os.mkdir(os.path.join(mypath, g))
        except OSError:
            print("O diretorio %s nao foi criado" % g)


def groupPhotosInFolder():
    grupos = listGroups()
    createFolders(grupos)

    photos = listFilesInDir()

    for ph in photos:
        os.rename(os.path.join(mypath, ph), os.path.join(mypath, ph[:4], ph))


def main(argv):
    # DIRECTORY_PHOTOS = '/Users/guilherme/Desktop/python-organize-gopro/pasta'
    # # print(os.getcwd())

    # mypath = DIRECTORY_PHOTOS
    
    # print(argv)
    groupPhotosInFolder()


# Chama a rotina de excucao do programa
main(sys.argv[1:])