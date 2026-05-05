import tkinter as tk 
from tkinter import ttk

def main():
    #Criação da janela "Pai"
    root = tk.Tk()
    root.title = ("Minha primeira janela")
    root.geometry("400x200")
    root.resizable(True, True)

    #label simple (Etiqueta, um texto na minha janela)
    label = ttk.Label(root, text="JOGO DO DINO", font=("TkDefaultFont",20))
    label.pack(expand=True)
   
    #Botão para fechar a janela (Btn é abreviação de botão\button)

    btn = ttk.Button(root,text="fechar", command=root.destroy)
    btn.pack(anchor="center", pady=10)

    #inicia o loop de eventos
    root.mainloop()

#comando para encerrar e limpar a memoria
if __name__ == "__main__":
    main()
