menu_principal = '''
            [Z]- Para Sacar
            [X]- Para ver Extrato
            [C]- Para fazer Deposito
            [S]- Para sair
            
=>'''
saldo = 0
limite = 500
limite_diario = 0
LIMITE_DIARIO = 3
extrato = []
while True:

    menu_opçoes = input(menu_principal)

    if menu_opçoes == 'Z':
        valor_saque = float(input('Qual o valor que deseja sacar?\n=>'))
        if valor_saque > 0:
            if LIMITE_DIARIO > limite_diario:
                if limite >= valor_saque:
                    if saldo > 0:
                        saldo -= valor_saque
                        limite_diario += 1
                        print(f'Saque de R${valor_saque} realizado com sucesso!\nSeu saldo agora é de R${saldo}')
                    else:
                        print(f'Seu saldo é insuficiente para o saque, você tem R${saldo}')
                else:
                    print(f'Você passou da quantidade limite para saque (R${limite}), por favor coloque uma quantidade menor.')
            else:
                print(f'Você passou do limite de saques diario ({LIMITE_DIARIO}), faça o saque no próximo dia.')
            extrato.append(-valor_saque)
        else:
            print('Operação não foi executada, insira um número positivo.')

    elif menu_opçoes == 'X':
        print('============ EXTRATO ============')
        saldo = 0 
        if not extrato:
            print('Não foi realizada nenhuma movimentação.')
        else:
            for transacao in extrato:
                if transacao > 0:
                    print(f'Depósito: R${transacao:.2f}')
                else:
                    print(f'Saque: R${abs(transacao):.2f}')
                saldo += transacao 
        print(f'Saldo atual: R${saldo:.2f}')
        print('=================================')

    elif menu_opçoes == 'C':
        valor_deposito = float(input('Qual o valor que deseja depositar em sua conta?\n=> '))
        if valor_deposito > 0:
            saldo += valor_deposito
            print(f'Depósito de R${valor_deposito} realizado com sucesso!')
            print(f'Seu saldo agora é de R${saldo}')
            extrato.append(valor_deposito)
        else:
            print("Por favor, insira um valor positivo.")

    elif menu_opçoes == 'S':
        print('Saindo do menu...')
        break

    else:
        ('Solitação incorreta. Por favor digite uma opção válida do nosso menu!')