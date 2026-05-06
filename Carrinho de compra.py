import tkinter as tk

janela = tk.Tk()
janela.title("Carrinho de compra")
janela.geometry("400x500")
janela.resizable(True,True)
 #titulo
pergunta = tk.Label(janela, text="item (ou 'total' para o total):", font=("Arial", 12))
pergunta.pack(pady=15)

item = tk.Entry(janela)
item.pack(pady=10)
while item != 'total':
    item = tk.Entry(janela)
    item.pack(pady=10)

#botão de sair
botao = tk.Button(janela,text="sair",command=janela.destroy)
botao.pack(pady=10)


    


janela.mainloop()