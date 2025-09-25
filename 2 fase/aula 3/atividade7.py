import calendar

ano = int(input("digite um ano: "))

def bissexto():
   if calendar.isleap(ano):
      return True
   return False

print(f"confirmação de ano bissexto é: {bissexto()}")