palavra=str(input("Digite uma palavra: ")).strip().upper()
def contador(palavra):
    contador_letra=0
    letra=str(input("Qual letra você quer saber a repetição ?")).strip().upper()

    for p in palavra:
        if p== letra:
            contador_letra+=1

    return contador_letra


print(contador(palavra))
