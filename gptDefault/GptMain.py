import openai
import qrcode
from gptSec import SecretCode

def usegpt():
    openai.api_key = SecretCode.scKey()
    model_engine = "text-davinci-003"

    while True:
        print(50*'-')
        prompt = input("Pergunte: ")
        print(".")
        print("...")
        print("...")
        print("Processando... ")
        print(50*"-")

        completion = openai.Completion.create(

            engine = model_engine,
            prompt = prompt,
            max_tokens = 1024,
            temperature = 0.7,

        )

        response = completion.choices[0].text
        print(response)

        arquivo = open("arquivo.txt", 'w')
        arquivo.write(response)
        img = qrcode.make(response)
        img.save("gptText.png")

        arquivo.close()

        saida = input("Deseja sair do chat:  ")
        if saida == "sim":
            break


