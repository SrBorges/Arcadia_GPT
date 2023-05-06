import openai
import webbrowser
import qrcode
from gptSec import SecretCode

def aiImage():

    openai.api_key = SecretCode.scKey()

    while True:
        print(50*"-")
        prompt = input("Descreva a imagem: ")
        print(".")
        print("..")
        print("...")
        print("processando... ")
        print(50*"-")
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="512x512"
        )

        image_url = response['data'][0]['url']
        webbrowser.open(image_url)

        img = qrcode.make(image_url)

        img.save("gpt_image.png")

        saida = input("Você deseja sair do chat: ")
        if saida == "sim":
            break