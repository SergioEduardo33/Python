
def media(x,y,z):
    resultado = (x+y+z)/3
    return resultado

num = []

for c in range(0,3):
    n=int(input("Digite um número:"))
    num.append(n)

resposta=media(num[0],num[1],num[2])
print(resposta)
