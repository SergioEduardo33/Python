soma=0
lista=[]

def somatorio(lista):
    soma=0
    for num in lista:
        soma+=num
    return soma


qtd=int(input("Digite a quantidade de números:"))

for c in range(qtd):
    num=int(input(f"Digite o {c+1}º valor:"))
    lista.append(num)

print(somatorio(lista))

