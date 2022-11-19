'''Esse programa pede dois números e um operador para realizar algumas operações, 
ao fim de cada este pergunta se deseja sair ou não!'''
while True:
    n1=input('Digite um número:')
    n2=input('Digite outro número:')
    operador=input('Coloque um operador:')
    sair=input('Deseja sair[s/n]:')
    if sair=='s':
        break
    try:
        n1=float(n1)
        n2=float(n2)
        if operador=='+':
            print(n1+n2)
        elif operador=='-':
            print(n1-n2)
        elif operador=='/':
            print(n1/n2)
        elif operador=='*':
            print(n1*n2)
    except:
        print('Isso não é um número!')
