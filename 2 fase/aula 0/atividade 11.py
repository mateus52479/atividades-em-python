codigo_lista = []
Qveiculos_lista = []
Aveiculos_lista = []
fodase_essa_merda = 0

for i in range(5):
    
    codigo = input(f"digite o codigo da {i+1}° cidade: ")
    Qveiculos = int(input(f"digite a quantidade de veiculos da {i+1}° cidade: "))
    Aveiculos = int(input(f"digite a quantidade de acidentes de transito com vitimas da {i+1}° cidade: "))
    codigo_lista.append(codigo)
    Qveiculos_lista.append(Qveiculos)
    Aveiculos_lista.append(Aveiculos)

indice_maximo = max(Aveiculos_lista)
indice_minimo = min(Qveiculos_lista)

for i in range(5):
    if Aveiculos_lista[i] == indice_maximo:
        print(f"o indice maximo é de {indice_maximo} e a cidade é a {codigo_lista[i]}")

for i in range(5):   
    if Aveiculos_lista[i] == indice_minimo:
        print(f"o indice minimo é de {indice_minimo} e a cidade é a {codigo_lista[i]}")

print(f"a media de veiculos é {sum(Qveiculos_lista)/5}")

for i in Aveiculos_lista:
    if i >= 2000:
        fodase_essa_merda +=1

if fodase_essa_merda != 0:
    print(f"a media de acidentes de cidades com menos de 2000 veiculos é {sum(Aveiculos_lista)/(5 - fodase_essa_merda)}")
else:
    print("a media de acidentes de cidades com menos de 2000 veiculos é 0")
