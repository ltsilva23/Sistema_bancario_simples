menu = """
============Olá, Bem-Vindo!============

        1 - Depositar
        2 - Sacar
        3 - Consultar Saldo
        4 - Extrato
        0 - Sair
========================================
"""

saldo_inicial = 0
limite_maximo = 500
extrato = []
limite_saques = 3
sacar_outro = limite_saques

while True:
    opcao = int(input(menu + "Informe a opção desejada: "))
    if opcao == 0:
            print("\nObrigado por usar o sistema bancário! Até logo.\n")
        break

    if opcao == 1:
        if saldo_inicial >= limite_maximo:
            print("\nSeu saldo atingiu o limite máximo de R$500. Não é possível fazer mais depósitos.")
        else:
            while True:
                valor = input("Informe o valor do depósito: R$ ")
                valor = valor.replace(',', '.')
                try:
                    valor = float(valor)
                except ValueError:
                    print("\nValor inválido. Por favor, insira um número válido.")
                    continue
                if valor <= 0:
                    print("\nNão é possível depositar este valor.")
                    continue
                while saldo_inicial + valor > limite_maximo:
                    print("\nDepósito excede o limite máximo permitido de R$500.")
                    valor = input(f"Informe um valor menor ou igual ao limite disponível R${limite_maximo - saldo_inicial:.2f} (ou digite 0 para voltar ao menu de opções): ")
                    valor = valor.replace(',', '.')
                    try:
                        valor = float(valor)
                    except ValueError:
                        print("\nValor inválido. Por favor, insira um número válido.")
                        continue
                    if valor == 0:
                        break
                if valor == 0:
                    break
                saldo_inicial += valor
                extrato.append(('depósito', valor))
                print(f"\nOperação realizada com sucesso! Você depositou R$ {valor:.2f}. \nSeu saldo atual é de R$ {saldo_inicial:.2f}\n")

                if saldo_inicial >= limite_maximo:
                    print("\nSeu saldo atingiu o limite máximo de R$500. Não é possível fazer mais depósitos.")
                    break
                
                depositar_outro = input("Deseja depositar outro valor? (S/N): ").upper()
                if depositar_outro != 'S':
                    break

    elif opcao == 2:
        if sacar_outro <= 0:
            print("\nVocê atingiu o limite de saques diários. Não é possível realizar mais saques.")
        else:
            while True:
                valor_atual = saldo_inicial
                valor_saque = input("Informe o valor que deseja sacar: R$ ")
                valor_saque = valor_saque.replace(',', '.')
                try:
                    valor_saque = float(valor_saque)
                except ValueError:
                    print("\nValor inválido. Por favor, insira um número válido.")
                    continue
                if valor_atual < 2:
                    print("\nVocê não possui saldo suficiente para efetuar saques.")
                    break
                if valor_saque < 2 or valor_saque % 2 != 0:
                    print("\nO valor mínimo de saque é R$ 2.00 e deve ser múltiplo de 2.")
                    continue
                if valor_saque > saldo_inicial:
                    print("\nVocê não possui este valor em conta. Por favor, consulte seu saldo.")
                    break
                if valor_saque > limite_maximo:
                    print("\nO valor solicitado excede o limite máximo permitido por saque.")
                    continue
                saldo_inicial -= valor_saque
                extrato.append(('saque', valor_saque))
                saldo_atual = saldo_inicial
                sacar_outro -= 1
                print(f"\nOperação realizada com sucesso! Você sacou R$ {valor_saque:.2f}. Seu saldo atual é de R$ {saldo_inicial:.2f}\n")
                if saldo_inicial == 0:
                    break
                else:
                    print(f"Você possui {sacar_outro} saques disponíveis.")
                if saldo_atual == 0:
                    print("\nSeu saldo é zero. Não é possível realizar mais saques.")
                    break
                if sacar_outro <= 0:
                    print("\nVocê atingiu o limite de saques diários. Não é possível realizar mais saques.")
                    break

                sacar_outro_mais = input("Deseja sacar outro valor? (S/N): ").upper()
                if sacar_outro_mais != 'S':
                    break

    elif opcao == 3:
        if saldo_inicial == 0:
            print(f"Você não possui saldo R$ {saldo_inicial} ")
        else:
            print(f"\nSeu saldo atual é de R$ {saldo_inicial:.2f}\n")
        
    elif opcao == 4:
        if not extrato:
            print("\nNão há movimentações no extrato.\n")
        else:
            print("\nExtrato:\n")
            print("Depósitos:\t\t\t\tSaques:")
    
        depositos = [f"+ R$ {valor:.2f}" for tipo, valor in extrato if tipo == 'depósito']
        saques = [f"- R$ {valor:.2f}" for tipo, valor in extrato if tipo == 'saque']
    
        max_transacoes = max(len(depositos), len(saques))
    
        for i in range(max_transacoes):
            deposito = depositos[i] if i < len(depositos) else ""
            saque = saques[i] if i < len(saques) else ""
            print(f"{deposito.ljust(25)}\t\t{saque}")
    
        print(f"\nSeu saldo atual é de R$ {saldo_inicial:.2f}\n")
    else:
        print("\nOpção inválida. Tente novamente.\n")
