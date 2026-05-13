import time
import sys
import os
import platform

def shutdown():
    sistema = platform.system().lower()
    try:
        if "windows" in sistema:
            os.system("shutdown /s /t 0")
        elif "linux" in sistema or "darwin" in sistema:
            os.system("shutdown now")
        else:
            print("\nSistem operacional não reconhecido")
    except Exception as e:
        print(f"\nErro ao tentar o shutdown: {e}")
def temporizador_com_shutdown():
    print("=== Temporizador Trolator Tabajara ===\n")
    try:
        entrada = input("\nQuantos segundos até o desligamento?")
        segundos = int(entrada)

        while segundos > 0:
            """Se o usuário digitar 125 segundos, o divmod(125,60)" Faz o seguinte: Divide 125 por 60.
             0 60 cabe 2 vezes dentro de 125(esses são os minutos), após calcular quanto sobrou a divisão.
             125 - (60x2) = 5(esse são os segundos)"""
            mins, secs = divmod(segundos, 60)
            timer = f"{mins:02d}:{secs:02d}"

            #Bip nos 10 segundos finais
            bip = "\a" if 0 < segundos < 10 else ""
            print(f"\r Tempo restante: {timer}{bip}", end="",flush=True)
            time.sleep(1)
            segundos -= 1

            print("\n\nIniciando o desligamento... Tchola! ‍🏳️‍🌈?")

            shutdown()
    except ValueError:
        print("\nErro: Por favor, digite apenas números inteiros.")
    except KeyboardInterrupt:
        print("\n\nOperação cancelada pelo usuário.")
if __name__=="__main__":
            temporizador_com_shutdown()