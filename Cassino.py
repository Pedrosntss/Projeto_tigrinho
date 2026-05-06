import random

#14. MÁQUINA DE SLOTS
simbolos = ["🍌","💰","🤑","🐒", "💔"]
saldo = 20.0
print(f"="*40)
print("          HOOOOOLÁ MACAKITO🍌!")
print("   Seja bem viado ao Kassinão do Senai!               ")
print(f"="*40)
while saldo >= 0:
    if saldo <2:  
        input("MACAKITO Saldo insuficiente, pressione ENTER para depositar...")
        while saldo <2:
            deposito = float(input("Digite o valor que Deseja depositar (Minimo R$2): "))
            saldo+=deposito
            print(f"\nDepositado com sucesso! Saldo atual: R${saldo:.2f} ")
            print(f"\nDeposito insuficiente para girar, deposite mais🤑")
            print(f"="*50)
        print(f"Saldo atual: R${saldo:.2f}")
        print(f"="*50)
    input("MACAKITO, pressione ENTER para girar (custa R$2)...")
    saldo -= 2 

    resultado = [random.choice(simbolos) for _ in range(3)]
    print("|". join(resultado))

    if resultado[0] == resultado[1] == resultado[2]:
        premio = 20 
        saldo+=premio
        print("BOA MACAKITO JACKPOT!")
        print(f"agora você pode ter sua banana🍌!! Você ganhou {premio}!🐒")
        print(f"Saldo atual: R${saldo:.2f}")
        print(f"="*40)
    else:
        print("Não foi dessa vez Macakito 🐒💔 ")
        print(f"Saldo atual: R${saldo:.2f}")
        print(f"="*40)

