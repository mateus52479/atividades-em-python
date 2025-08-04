#12.	Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, utilizando as seguintes formulas (onde h corresponde à altura): 

sexo = input("digite seu genero, H ou F: ").upper()
altura = float(input("digite sua altura: "))

if sexo == "H":
    print("seu peso ideial é" ,(72.7*altura)-58)
    
elif sexo == "F":
    print("seu peso ideial é" ,(62.1*altura)-44,7)
else:
    print("por favor digite as informações corretamente")