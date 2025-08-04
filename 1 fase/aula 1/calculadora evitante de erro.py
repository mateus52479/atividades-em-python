#14.	Escreva o menu de opções abaixo. Leia a opção do usuario e execute a operação escolhida. Escreva uma mensagem de erro se a opção for inválida. Escolha a opção: 

n1 = float(input("digite o primeiro numero: "))
n2 = float(input("digite o segundo numero: "))

print("escolha uma das opções: \n" \
"1	Soma de 2 numeros. \n" \
"2	Diferença entre 2 números (maior pelo menor). \n" \
"3	Produto entre 2 números. \n" \
"4	Divisão entre 2 números (o denominador não pode ser zero).")

resposta = float(input("digite entre 1 a 4: "))

if resposta == 1:
    print("soma: ", n1+n2)
elif resposta == 2:
    if (n1>n2):
        print("diferença: ", n1-n2)
    elif (n1<n2):
        print("diferença: ", n2-n1)
    else:
        print("diferença: 0")
elif resposta == 3:
    print("o produto: ",n1*n2)
elif resposta == 4:
    if n1!=0:
        print("divisao do segundo pelo primeiro: ",n2/n1)
    elif n2!=0:
        print("divisao do primeiro pelo segundo: ",n1/n2)
    else:
        print("por favor coloque um numero diferente de zero")
else:
    print("coloque uma opção possivel")
    
    