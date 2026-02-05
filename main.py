usuarios = []
saldo = int(0)

def cadastro():
    nome = input('Digite seu nome: ')
    email = input('Digite seu email: ').lower()
    senha = input('Digite sua senha: ')
    idade = int(input('Digite sua idade: '))

    return {
        'nome': nome,
        'email': email,
        'senha': senha,
        'idade': idade,
        'saldo': 0
    }

def login(usuarios):
    email = input('Digite seu email: ').lower()
    senha = input('Digite sua senha: ')

    for usuario in usuarios:
        if usuario['email'] == email and usuario['senha'] == senha:
            print('Logado com sucesso')
            return posmenu(usuario)

    print('Usuário não encontrado')

def posmenu(usuario):
    while True:
        print(f"\nSeja Bem-Vindo {usuario['nome']}, o que deseja fazer?")
        print('1 - Realizar pagamento')
        print('2 - Ver saldo')
        print('3 - Sair')

        opcao = input('Selecione uma opção: ')
        if opcao == '1':
            pagamento(usuario)
        elif opcao == '2':
            print(f"Saldo disponível: {usuario['saldo']}")
        elif opcao == '3':
            print('Deslogando da sua conta...')
            return None
        else:
            print('Opção ainda não implementada.')

def listarusuarios(usuarios):
    if not usuarios:
        print('Nenhum usuário cadastrado.')
        return

    for usuario in usuarios:
        print('Nome:', usuario['nome'])
        print('Email:', usuario['email'])
        print('Idade:', usuario['idade'])
        print('-' * 20)

def pagamento(usuario):
    print('Quanto deseja pagar?\nCédulas disponíveis: 2, 5, 10, 20, 50 e 100.')
    pagar = int(input('Selecione o valor: R$'))
    if pagar > 0:
        usuario['saldo'] += pagar
        print(f"Saldo disponível: {usuario['saldo']}")
    else:
        print('Valor inválido.')

while True:
    print('\n====MENU====')
    print('1 - Cadastro')
    print('2 - Login')
    print('3 - Verificar informações')
    print('4 - Sair')

    opcao = input('Escolha sua opção: ')

    if opcao == '1':
        novousuario = cadastro()

        # valida idade
        if novousuario['idade'] < 18:
            print('Idade inferior a 18 anos, impossível realizar o cadastro.')
            continue

        # valida email único
        email_existe = False
        for usuario in usuarios:
            if usuario['email'] == novousuario['email']:
                email_existe = True
                break

        if email_existe:
            print('Email já cadastrado.')
            continue

        usuarios.append(novousuario)
        print('Cadastro realizado com sucesso!')
    elif opcao == '2':
        login(usuarios)
    elif opcao == '3':
        listarusuarios(usuarios)

    elif opcao == '4':
        print('Fechando o programa...')
        break

    else:
        print('Opção inválida')
