#atividade A
from datetime import datetime


print(f"hora atual: {datetime.now()}")


#atividade B
from datetime import date

ano = int(input("digite o ano que voce nasceu: "))
ano_atual = date.today().year

print(f"a sua idade com base no ano é {ano_atual - ano}")


#atividade C

from datetime import datetime, timedelta

data_str = input("Digite uma data no formato dia/mes/ano: ")

data = datetime.strptime(data_str, "%d/%m/%Y")

nova_data = data + timedelta(days=15)

print(f"A nova data é: {nova_data.strftime('%d/%m/%Y')}")
