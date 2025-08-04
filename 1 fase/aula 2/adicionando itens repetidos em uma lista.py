itens = []; 
repeat = []; 

for i in range(5):
    item = input("digite cinco termos: ")
    itens.append(item)
print(itens)

for a in itens:
    if itens.count(a)>1 and a not in repeat:
        repeat.append(a)
print(repeat)