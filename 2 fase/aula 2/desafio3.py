frase = "eu gosto de python e eu estudo python"

palavras = frase.split()
frequencia = {}  

for i in palavras:
    if i in frequencia:
        frequencia[i] += 1
    else:
        frequencia[i] = 1

print(frequencia)