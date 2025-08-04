#3.	Faça um programa que mostre na tela uma pergunta de múltipla escolha e que, a partir da resposta do usuário, mostre na tela se ele acertou ou não.

print("a partir do seu conhecimento responda a resposta correta: \n" \
"a) (a==1) A variavel (a) esta sendo afirmada que é igual a 1 \n" \
"b) print transforma numero inteiro para real \n" \
"c) ctrl + D possibilita mudar todas palavras iguas"  )

resposta = input("resporta: ")

if resposta == "c":
    print("resposta correta")
else:
    print("resposta incoreta")