import tkinter as tk 
import random 
import pygame

#configuração
simbolos =  ["🍵", "🤑", "🐘", "👽","🍊"]
saldo = 20.0
custo_giro = 2 

# Função de Girar():
def girar():
    global saldo

    if saldo < custo_giro:
        # texto que vai aparecer quando o saldo for maior que o custo do giro
        # é como se fosse o print só que fazendo no tk\em janelas
        resultado_Label.config(text="Saldo insuficiente!", fg="red")
        return
    saldo -= custo_giro

    resultado = [random.choice(simbolos) for _ in range(3)]

    #atualiza os slots

    slot1.config(text=resultado[0])
    slot2.config(text=resultado[1])
    slot3.config(text=resultado[2])

    #Verifica vitória 
    if resultado[0] == resultado[1] == resultado [2]:
        premio = 60000
        saldo += premio 
        resultado_Label.config(text=f"🎉 JACKPOT! +R$ {premio}", fg="green")
    else:
        resultado_Label.config(text=f"😟 Tente novamente...", fg = "black")

    saldo_label.config(text=f"Saldo: R$ {saldo: .2f}")

#Janela principal
janela = tk.Tk()
janela.title = ("Kassinão do Sesi")
janela.geometry ("400x300")
janela.resizable (True,True)

#TITULO
titulo = tk.Label(janela, text="Kassinão do Sesi", font= ("Arial", 16, "bold"))
titulo.pack(pady=10)

# Frame dos slots 
frame_slots = tk.Frame(janela)
frame_slots.pack(pady=10)

slot1 = tk.Label(frame_slots, text="❓", font=("Arial", 30))
slot1.pack(side="left", padx=10)

slot2 = tk.Label(frame_slots, text="❓", font=("Arial", 30))
slot2.pack(side="left", padx=10)

slot3 = tk.Label(frame_slots, text="❓", font=("Arial", 30))
slot3.pack(side="left", padx=10)

# Resultado
resultado_Label = tk.Label(janela, text="Clique para GIRAR", font=("Arial",12))
resultado_Label.pack(pady=10)

#saldo
saldo_label =  tk.Label(janela, text=f"Saldo: R$ {saldo:.2f}", font=("Arial", 12))
saldo_label.pack(pady=15)

#Botão Girar
botao = tk.Button(janela, text=("Gire🤑", 12), command=girar)
botao.pack(pady=15)

#loop
janela.mainloop()