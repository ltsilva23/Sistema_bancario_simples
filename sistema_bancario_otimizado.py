import textwrap


menu = """

============Olá, Bem-Vindo!============

        1 - Depositar
        2 - Sacar
        3 - Consultar Saldo
        4 - Extrato
        5 - Novo cliente
        6 - Listar clientes
        7 - Criar conta
        8 - Listar conta
        0 - Sair
========================================
"""

saldo_inicial = 0
limite_maximo = 500
extrato = []
limite_saques = 3
AGENCIA = "0001"
numero_saques = limite_saques
usuarios = []
contas = []
numero_conta = 1

def validar_valor(mensagem):
    while True:
        valor = input(mensagem)
        try:
            valor = float(valor.replace(",", "."))
            if valor < 0:
                print("\nNão é possível depositar ou sacar um valor negativo.")
                continue
            return valor
        except ValueError:
            print("\nValor inválido. Por favor, insira um número válido.")

def depositar(saldo, limite_maximo, extrato):
    while True:
        if saldo >= limite_maximo:
            print(
                "\nSeu saldo atingiu o limite máximo de R$500. Não é possível fazer mais depósitos."
            )
            break
        valor = validar_valor(
            f"Informe o valor do depósito (ou digite 0 para voltar ao menu de opções, Limite disponível: R$ {limite_maximo - saldo:.2f}): R$ "
        )
        if valor == 0:
            break
        if saldo + valor > limite_maximo:
            print("\nDepósito excede o limite máximo permitido de R$500.")
            continue
        saldo += valor
        extrato.append(("depósito", valor))
        print(
            f"\nOperação realizada com sucesso! Você depositou R$ {valor:.2f}. \nSeu saldo atual é de R$ {saldo:.2f}\n"
        )
    return saldo

def sacar(saldo, limite_maximo, extrato, numero_saques):
    while True:
        if numero_saques <= 0:
            print(
                "\nVocê atingiu o limite de saques diários. Não é possível realizar mais saques."
            )
            break
        valor_saque = validar_valor(
            "Informe o valor que deseja sacar (ou digite 0 para voltar ao menu de opções): R$ "
        )
        if valor_saque == 0:
            break
        if valor_saque < 2 or valor_saque % 2 != 0:
            print("\nO valor mínimo de saque é R$ 2.00 e deve ser múltiplo de 2.")
            continue
        if valor_saque > saldo:
            print(
                "\nVocê não possui este valor em conta. Por favor, consulte seu saldo."
            )
            break
        if valor_saque > limite_maximo:
            print("\nO valor solicitado excede o limite máximo permitido por saque.")
            continue
        saldo -= valor_saque
        extrato.append(("saque", valor_saque))
        numero_saques -= 1
        print(
            f"\nOperação realizada com sucesso! Você sacou R$ {valor_saque:.2f}. Seu saldo atual é de R$ {saldo:.2f}\n"
        )
        print(f"Você possui {numero_saques} saques disponíveis.")
    return saldo, numero_saques

def consultar_saldo(saldo):
    print(f"\nSeu saldo atual é de R$ {saldo:.2f}\n")

def imprimir_extrato(extrato, saldo):
    if not extrato:
        print("\nNão há movimentações no extrato.\n")
        print(f"\nSeu saldo atual é de R$ {saldo:.2f}\n")
    else:
        print("\nExtrato:\n")
        print("Depósitos:\t\t\t\tSaques:")
        depositos = [
            f"+ R$ {valor:.2f}" for tipo, valor in extrato if tipo == "depósito"
        ]
        saques = [f"- R$ {valor:.2f}" for tipo, valor in extrato if tipo == "saque"]
        max_transacoes = max(len(depositos), len(saques))
        for i in range(max_transacoes):
            deposito = depositos[i] if i < len(depositos) else ""
            saque = saques[i] if i < len(saques) else ""
            print(f"{deposito.ljust(25)}\t\t{saque}")
        print(f"\nSeu saldo atual é de R$ {saldo:.2f}\n")

def criar_usuario(usuarios):
    while True:
        cpf_usuario = input("Informe o CPF (somente números): ")
        
        cpf_existe = any(usuario["cpf"] == cpf_usuario for usuario in usuarios)
        if cpf_existe:
            print("CPF já cadastrado. Tente novamente.")
        else:
            nome_usuario = input("Informe o nome completo do cliente: ")
            data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
            endereco = input("Informe o endereço completo (logradouro, número - bairro - cidade/sigla estado): ")
        
            usuario = {
                "cpf": cpf_usuario,
                "nome": nome_usuario,
                "data_nascimento": data_nascimento,
                "endereco": endereco,
            }

            usuarios.append(usuario)
            print("Usuário criado com sucesso!")
        
        cadastrar_outro_usuario = input("Deseja cadastrar outro cliente? (S/N): ").upper()  
        if cadastrar_outro_usuario != 'S':
            break

def filtrar_usuarios(cpf_usuario, usuarios):
    cpf_usuario = input("\nInforme o CPF do usuário a ser buscado (somente números): ")

    usuario_encontrado = next((usuario for usuario in usuarios if usuario["cpf"] == cpf_usuario), None)

    if usuario_encontrado:
        print("\nUsuário encontrado:")
        print(f"\nNome: {usuario_encontrado['nome']}")
        print(f"\nData de Nascimento: {usuario_encontrado['data_nascimento']}")
        print(f"\nEndereço: {usuario_encontrado['endereco']}")
        return usuario_encontrado
    else:
        print("Usuário não encontrado.")
        return None

def criar_conta(AGENCIA,numero_conta, usuarios):
    while True:
        cpf_usuario = input("Informe o CPF (somente números): ")

        usuario = next((usuario for usuario in usuarios if usuario["cpf"] == cpf_usuario), None)
        if not usuario:
            print("Este cliente não possui cadastro no sistema.")
        else:   
            conta = {
                "agencia": AGENCIA,
                "numero_conta": f"{numero_conta}",
                "cpf_usuario": cpf_usuario,
                "nome_usuario": usuario["nome"]
            }
            contas.append(conta)
            print("Conta criada com sucesso!")
            numero_conta += 1  

        cadastrar_outra_conta = input("Deseja cadastrar outra conta? (S/N): ").upper()  
        if cadastrar_outra_conta != 'S':
            break

def listar_contas(contas):
    if not contas:
        print("Não há contas cadastradas.")
    else:
        for conta in contas:
            print("\n\tContas Cadastradas:\n ")
            cadastro = f"""\
                  Agência:\t{conta['agencia']} 
                  C/C:\t\t{conta['numero_conta']} 
                  Titular:\t{conta['nome_usuario']}
                  CPF:\t{conta['cpf_usuario']} 
              """
            print("=" * 100)
            print(textwrap.dedent(cadastro))

while True:
    opcao = int(input(menu + "Informe a opção desejada: "))
    if opcao == 0:
        print("\nObrigado por usar o sistema bancário! Até logo.\n")
        break
    elif opcao == 1:
        saldo_inicial = depositar(saldo_inicial, limite_maximo, extrato)
        if saldo_inicial >= limite_maximo:
            continuar = input(
                "Você atingiu o limite máximo de R$500. Deseja voltar ao menu de opções? (S/N): "
            ).upper()
            if continuar != "S":
                break
    elif opcao == 2:
        saldo_inicial, numero_saques = sacar(
            saldo_inicial, limite_maximo, extrato, numero_saques
        )
    elif opcao == 3:
        consultar_saldo(saldo_inicial)
    elif opcao == 4:
        imprimir_extrato(extrato, saldo_inicial)
    elif opcao == 5:
        criar_usuario(usuarios)
    elif opcao == 6:
        filtrar_usuarios(None, usuarios)
    elif opcao == 7:
        numero_conta = len(contas) + 1
        criar_conta(AGENCIA, numero_conta, usuarios)
    elif opcao == 8:
        listar_contas(contas)
    else:
        print("\nOpção inválida. Tente novamente.\n")
