def cadastro():
    print("-=-" * 20)
    print("Faça seu cadastro!")
    print("-=-"*20)
    novo_email = str(input("email: "))

    while True:
        nova_senha = str(input("senha: "))
        confirmar_senha = str(input("Confirme a senha: "))

        if nova_senha == confirmar_senha:
            print("Cadastro realizado com sucesso!")
            break
        else:
            print("As senhas não coincidem! Tente novamente!")

    return novo_email, nova_senha


def login(email, senha):
    usuario_cadastrado = False
    print("-=-"*20)
    print("Login")
    print("-=-" * 20)
    while not usuario_cadastrado:
        email_input = str(input("email: "))
        senha_input = str(input("senha: "))
        if email_input == email and senha_input == senha:
            print("Login Bem-Sucedido!")
            usuario_cadastrado = True
        else:
            print("Usuário ou senha incorretos! Tente novamente!")


email_cadastrado, senha_cadastrada = cadastro()

login(email_cadastrado, senha_cadastrada)

print("Obrigado pela preferência!")
print("Preencha abaixo com as suas informações!")
nome=str(input("Digite seu nome: "))
idade=int(input("Digite sua idade: "))
sexo=str(input("Digite seu sexo: "))
altura=float(input("Digite sua altura: "))
peso=float(input("Digite seu peso: "))
print()
print("Registro Concluído!")

print("-=-"*20)
restrição=str(input("Possui alguma restrição[S/N]:")).split()

print("-=-"*20)
print("""Nível de Condicionamento
1 - Sedentário
2 - Básico
3 - Intermediário
4 - Avançado""")

opcao_nivel=0

while opcao_nivel not in (1,2,3):
    opcao_nivel=int(input("Digite a opção: "))
    if opcao_nivel not in (1,2,3):
        print("Opção Inválida! Tente Novamente!")

print("-=-"*20)

print("""Escolha sua meta
1 - Emagrecimento
2 - Ganhar Massa Muscular
3 - Definição""")

opcao_meta=0

while opcao_meta not in (1,2,3):
    opcao_meta=int(input("Digite a opção: "))
    if opcao_meta not in (1,2,3):
        print("Opção Inválida! Tente Novamente!")

if opcao_meta ==1:
    print("Plano para emagrecimento")
    print("""Treino de Pernas e Glúteos
    .Agachamento livre: 4 séries de 12 repetições
    .Avanço com halteres: 3 séries de 10 repetições (cada perna)
    .Cadeira extensora: 3 séries de 12 repetições
    .Elevação de panturrilha em pé: 4 séries de 15 repetições
    .Agachamento sumô: 3 séries de 12 repetições
    """)
    print("""Treino de Membros Superiores - Parte Superior
    .Supino reto: 4 séries de 10 repetições
    .Remada curvada: 4 séries de 10 repetições
    .Desenvolvimento de ombros com halteres: 3 séries de 12 repetições
    .Rosca direta com barra: 3 séries de 12 repetições
    .Tríceps pulley: 3 séries de 12 repetições
    """)
    print("""Treino de Cardio (exercícios aeróbicos)
    .45-60 minutos de corrida, bicicleta, elíptico ou esteira em intensidade moderada a alta.
    """)
    print("""Treino de Pernas e Glúteos
    .Agachamento frontal: 4 séries de 10 repetições
    .Stiff: 3 séries de 12 repetições
    .Cadeira adutora: 3 séries de 12 repetições
    .Elevação de panturrilha sentado: 4 séries de 15 repetições
    .Glúteo na máquina: 3 séries de 12 repetições
    """)
    print("""Treino de Membros Superiores - Parte Superior
    .Supino inclinado com halteres: 4 séries de 10 repetições
    .Remada unilateral com halteres: 4 séries de 10 repetições (cada braço)
    .Elevação lateral com halteres: 3 séries de 12 repetições
    .Rosca martelo: 3 séries de 12 repetições
    .Tríceps francês: 3 séries de 12 repetições
    """)
    print("""Treino de Cardio (exercícios aeróbicos)
    .45-60 minutos de atividade aeróbica de sua escolha, como corrida, bicicleta, elíptico ou esteira, em intensidade moderada a alta.
        """)
elif opcao_meta ==2:
    print("Plano para ganhar massa")
    print("""Treino de Peito e Tríceps
    .Supino reto: 4 séries de 8-10 repetições
    .Supino inclinado com halteres: 3 séries de 10-12 repetições
    .Crucifixo com halteres: 3 séries de 10-12 repetições
    .Extensão de tríceps com corda: 3 séries de 10-12 repetições
    .Paralelas: 3 séries de 10-12 repetições
    """)
    print("""Treino de Costas e Bíceps
    .Barra fixa: 4 séries de 8-10 repetições
    .Remada curvada: 3 séries de 10-12 repetições
    .Puxada alta com polia: 3 séries de 10-12 repetições
    .Rosca direta com barra: 3 séries de 10-12 repetições
    .Rosca alternada com halteres: 3 séries de 10-12 repetições
    """)
    print("""Treino de Pernas
    .Agachamento livre: 4 séries de 8-10 repetições
    .Leg press: 3 séries de 10-12 repetições
    .Cadeira extensora: 3 séries de 10-12 repetições
    .Cadeira flexora: 3 séries de 10-12 repetições
    . Panturrilha no leg press: 4 séries de 12-15 repetições
    """)
    print("""Treino de Ombros e Trapézio
    .Desenvolvimento de ombros com barra: 4 séries de 8-10 repetições
    .Elevação lateral com halteres: 3 séries de 10-12 repetições
    .Desenvolvimento Arnold: 3 séries de 10-12 repetições
    .Encolhimento de ombros com barra: 3 séries de 10-12 repetições
    """)
    print("""Treino de Pernas e Glúteos
    .Agachamento frontal: 4 séries de 8-10 repetições
    .Stiff: 3 séries de 10-12 repetições
    .Afundo com halteres: 3 séries de 10-12 repetições (cada perna)
    .Cadeira adutora: 3 séries de 10-12 repetições
    .Glúteo na máquina: 3 séries de 10-12 repetições
    """)
else:
    print("Plano para definição")
    print(""" Treino de Peito e Tríceps
    .Supino reto com halteres: 4 séries de 10-12 repetições
    .Supino inclinado com barra: 3 séries de 10-12 repetições
    .Crucifixo inclinado com halteres: 3 séries de 10-12 repetições
    .Extensão de tríceps na polia: 3 séries de 10-12 repetições
    .Tríceps testa com halteres: 3 séries de 10-12 repetições
    """)
    print(""" Treino de Costas e Bíceps
    .Barra fixa (ou puxada alta na polia): 4 séries de 10-12 repetições
    .Remada curvada: 3 séries de 10-12 repetições
    .Pull-down na polia: 3 séries de 10-12 repetições
    .Rosca direta com barra EZ: 3 séries de 10-12 repetições
    .Rosca martelo com halteres: 3 séries de 10-12 repetições
    """)
    print(""" Treino de Pernas
    .Agachamento livre: 4 séries de 10-12 repetições
    .Leg press: 3 séries de 10-12 repetições
    .Cadeira extensora: 3 séries de 10-12 repetições
    .Cadeira flexora: 3 séries de 10-12 repetições
    .Panturrilha no leg press: 4 séries de 12-15 repetições
    """)
    print(""" Treino de Ombros e Trapézio
    .Desenvolvimento de ombros com halteres: 4 séries de 10-12 repetições
    .Elevação lateral com halteres: 3 séries de 10-12 repetições
    .Desenvolvimento Arnold: 3 séries de 10-12 repetições
    .Encolhimento de ombros com halteres: 3 séries de 10-12 repetições
    """)
    print(""" Treino de Pernas e Glúteos
    .Agachamento sumô: 4 séries de 10-12 repetições
    .Passadas com halteres: 3 séries de 10-12 repetições (cada perna)
    .Cadeira adutora: 3 séries de 10-12 repetições
    .Cadeira abdutora: 3 séries de 10-12 repetições
    .Glúteo na máquina: 3 séries de 10-12 repetições
    """)
    print(""" Treino de Abdominais e Cardio
    .Prancha: 3 séries de 30-60 segundos
    .Crunch abdominal: 3 séries de 15-20 repetições
    .Exercício de prancha lateral: 3 séries de 30-60 segundos (cada lado)
    .Cardio: 30-45 minutos de atividade aeróbica moderada (corrida, bicicleta, elíptico, etc.)
    """)



