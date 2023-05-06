# -*- coding:UTF-8 -*-

from gptDefault import GptMain
from gptImage import GptImage
from gptHelp import Help

print("1 - GPT TALK. \n")
print("2 - GPT IMAGE. \n")
print("3 - Help. \n")
print("9 - Sair")

def menu():
    opcao = int(input("Informe sua escolha: "))

    match opcao:
        case 1:
            GptMain.usegpt()
        case 2:
            GptImage.aiImage()
        case 3:
            Help.help()
        case 9:
            print("Processo encerrado. ")
            return
        case _:
            print("Opção inválida. ")

            menu()

menu()