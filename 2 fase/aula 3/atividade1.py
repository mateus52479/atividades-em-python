def soma(n1, n2, n3):
    s = (n1 + n2 + n3)/3
    return s 

n1 = float(input("digite sua 1° nota: "))
n2 = float(input("digite sua 2° nota: "))
n3 = float(input("digite sua 3° nota: "))
    
print(f"sua media: {soma(n1, n2, n3):.2}")    