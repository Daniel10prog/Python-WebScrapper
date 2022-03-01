import glob
import os
import re

files = glob.glob(r"C:\Users\Daniel\Desktop\TRABALHOS\ALGORITMOS E ESTRUTURAS DE DADOS\Desafios\images_scrambled")
if os.path.isdir(r"C:\Users\Daniel\Desktop\TRABALHOS\ALGORITMOS E ESTRUTURAS DE DADOS\Desafios\images_scrambled"):
    for myFile in files:
        new_name = re.sub('[0-9]','', myFile)
        os.rename(myFile, new_name)
        print(new_name)
    print("Feito jovem!")
else:
    print("Jovem o caminho não existe!")
os.system("pause")
