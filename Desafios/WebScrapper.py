from bs4 import BeautifulSoup
import requests

url = "https://www.tempo.pt/lisboa.htm"

result = requests.get(url)
doc = BeautifulSoup(result.content, "html.parser")
x = doc.find("span", class_="dato-temperatura").text
temp = x.replace("°", "")

print(f"A temperatura atual em Lisboa é de {temp}")

temp_int = int(temp)

if temp_int >= 0 and temp_int<=10:
    print("Utilização de um casaco quente")
elif temp_int>=11 and temp_int<=20:
    print("Utilização de um casaco leve")
elif temp_int >=21 and temp_int<=30:
    print("Não é preciso casaco")

input('Digite qualquer coisa para sair')
