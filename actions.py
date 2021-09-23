from output import *


def choices(txt, cont):
    global registro
    nome = ""
    txt += str(cont)
    with open('terminal_novel/txt/story', 'r', encoding='utf-8') as a:
        for linha in a:
            linha = linha.strip('\n')
            if nome == "":
                if txt in linha.split():
                    nome = linha
            else:
                registro = linha.split(', ')
                return typewriterPrint(f"\n({len(registro[0][0])})- {registro[0]}"), typewriterPrint(f"({len(registro[1][0])+len(registro[1][0])})- {registro[1]}")


def storyActions(txt, cont):
    nome = ""
    txt += str(cont)
    with open('terminal_novel/txt/story', 'r', encoding='utf-8') as a:
        for linha in a:
            linha = linha.strip('\n')
            if nome == "":
                if txt in linha.split():
                    nome = linha
            else:
                registro = linha.split('.')
                return typewriterPrint(f"\n{registro[0]}")


def story(txt):
    nome = ""
    with open('terminal_novel/txt/story', 'r', encoding='utf-8') as a:
        for linha in a:
            linha = linha.strip('\n')
            if nome == "":
                if txt in linha.split():
                    nome = linha
            else:
                registro = linha.split('.')
                return typewriterPrint(f"\n{registro[0]}")


def actions():
    story('story')
    cont = 1
    while True:
        choices('action', cont)
        typewriterPrint("\n- Qual a sua ação?", 6.0)
        choice = input("> ").lower()

        if choice in ['1', registro[0][0].lower(), registro[0].lower()]:
            storyActions(f'action{cont}-', 1)
            cont += 1
        elif choice in ['2', registro[1][0].lower(), registro[1].lower()]:
            storyActions(f'action{cont}-', 2)
            cont += 1
        elif choice != registro:
            typewriterPrint("\nNão entendi, repita")
            continue
        else:
            print("\nERROR3450")
            continue