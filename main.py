import time
import sys
import os
import platform
from math import trunc


def shutdown():
    sistema = platform.system().lower()
    try:
        if "windows" in sistema:
            os.system("shutdown /s /t 0")
        elif "linux" in sistema or "darwin" in sistema:
            os.system("shutdown now")
        else:
            print("\nSistema operacional não reconhecido")
    except Exception as e:
        print(f"\nErro ao tentar o shutdown {e}")
def temporizador_com_shutdown():
    print("=== Temporizador trolator tabajara ===")
    try:
        entrada = input("\nQuantos segundos até o desligamento?")
        segundos = int(entrada)

        while segundos > 0:
            mins, secs = divmod(segundos, 60)
            timer = f"{mins:02d}: {secs02d}"

            # Bip nos 10 segundos finais
            bip = "\a" if 0 < segundos < 10 else ""
            print(f"\r Tempo restante: {timer}{bip}", end="", flush=True)
            time.sleep(1)
            segundos -=1

            print("\n\nIniciando desligamento... Tchau! 👋")

            shutdown()
    except valueError:
        print("\Erro: Por favor, digite apenas números inteiros")
    except KeyboardInterrupt:
        print("\n\nOperação cancelada pelo usuário")
if __name__ == "__main__":
