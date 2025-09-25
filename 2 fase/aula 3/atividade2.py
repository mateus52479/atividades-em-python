def soma(n1, n2, n3):
    s = (n1 + n2 + n3)/3
    return s 

n1 = float(input("digite sua 1° nota: "))
n2 = float(input("digite sua 2° nota: "))
n3 = float(input("digite sua 3° nota: "))

media = soma(n1, n2, n3)
print(f"sua media: {media}")    

def resultado():
    if media >= 6:
        print("aluno aprovado")
    
    elif media >= 4 and media <6:
        print("verificação suplementar")
    else:
        print("aluno reprovado")

resultado()