
def primo_ou_nao():
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                print(num, "não é primo!")
                break
            else:
                print(num, "é primo")
                break
num=int(input("Digite um número:"))
print(primo_ou_nao())
