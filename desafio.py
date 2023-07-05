menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor do depósito:"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Erro! Valor incorreto.")

    elif opcao == "s":
        valor = float(input("Digite o valor do saque:"))

        saldo_excedente = valor > saldo

        limite_excedido = valor > limite

        saques_excedidos = numero_saque >= LIMITE_SAQUE

        if saldo_excedente:
            print("Saldo insuficiente")

        elif limite_excedido:
            print("Valor do saque excede o limite")

        elif saques_excedidos:
            print("Você ultrapassou a qunantidade de saques por hoje")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque += 1

        else:
            print("Erro! Valor incorreto.")


    elif opcao == "e":
        print("\n=====EXTRATO=====")
        print("Sem movimentação." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.f}")
        print("===================")

    elif opcao == "q":
        break

    else:
        print("Operação invalida, por favor selecione novamente a opção desejada.")