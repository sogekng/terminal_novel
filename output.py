import time
import sys
import os


WORKING_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
TEXT_SOURCE = os.path.join(WORKING_DIRECTORY, "txt")


def clean():
    os.system('cls' if os.name == 'nt' else 'clear')


def openEncoded(path):
    return open(path, encoding='utf-8')


def openEncodedTxtFile(filename):
    return openEncoded(os.path.join(TEXT_SOURCE, filename))


def writeFlush(message):
    sys.stdout.write(message)
    sys.stdout.flush()


def typewriterPrint(message, wordsPerSecond=7.0, 
        endingSleepTime=1.0, considerPauses=True):
    for character in message:
        writeFlush(character)
        if considerPauses:
            if character == ",":
                time.sleep(0.5)
            elif character == ".":
                time.sleep(0.75)
            else:
                time.sleep(1.0 / (wordsPerSecond * 5))
        else:
            time.sleep(1.0 / (wordsPerSecond * 5))

    writeFlush("\n")
    time.sleep(endingSleepTime)


def typewriterPrintTxtFile(filename, wordsPerSecond=7.0,
                           endingSleepTime=1.0, considerPauses=True):
    with openEncodedTxtFile(filename) as txtFile:
        typewriterPrint(
            txtFile.read(), wordsPerSecond,
            endingSleepTime, considerPauses)

def start():
    while True:
        typewriterPrint("\n- Começar", 4.0)
        typewriterPrint("- Ler sinopse", 4.0)
        typewriterPrint("- Sair", 4.0)
        choice = input("> ").lower()

        if choice in ['c', 'começar', 'comecar']:
            break
        elif choice in ['l', 'ler sinopse']:
            while True:
                print('\n')
                typewriterPrintTxtFile('introduction')
                typewriterPrint('\n- Voltar')
                choice = input('> ').lower()
                if choice in ['v', 'voltar']:
                    break
                else:
                    continue
        elif choice in ['s', 'sair']:
            exit()
        else:
            typewriterPrint("\nNão entendi, repete")
            continue