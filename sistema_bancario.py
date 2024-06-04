menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        saque = float(input("Informe o valor do saque: "))
        if saque > 0:
            if saque <= limite and saque <= saldo  and numero_saques <= LIMITE_SAQUES:
                saldo -= saque
                numero_saques += 1
                print("Saque efetuado")
            else:
                print("Não foi possivel realizar o saque")
                print(f"Limite de saques: {LIMITE_SAQUES}, saque realizados: {numero_saques}")
                print(f"Limite por saque: {limite:.2f}, valor digitado: {saque:.2f}")
                print(f"Saldo: {saldo:.2f}")
        else:
            print("Valor inválido")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")