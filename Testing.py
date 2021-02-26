lista = ['a', 'b', 'c']
print(lista)
print("first Item:",lista[0])
print("Last item:",lista[-1])
def listta(lista):
    for x in lista:
        print(x)
listta(lista)
lista.append("d")
print(lista)
print(lista[3])
copylista = lista
print(copylista)