import tkinter as tk


def criar_janela_e_carrinho():
    janela = tk.Tk()
    janela.title("Carrinho de compra")
    janela.geometry("400x500")
    janela.resizable(True, True)
    carrinho = []
    entrada_item = ""
    # Título
    pergunta = tk.Label(janela, text="Item (ou 'total' para o total):", font=("Arial", 12))
    pergunta.pack(pady=15)

    # Campo de entrada (Entry) - Criamos apenas UM aqui
    while True:
        entrada_item = tk.Entry(janela, font=("Arial", 12))
        entrada_item.pack(pady=10)

        if entrada_item == 'total':

    carrinho.append(entrada_item)


    # Botão de sair
    botao_sair = tk.Button(janela, text="Sair", command=janela.destroy)
    botao_sair.pack(pady=10)

    # O mainloop deve ser a última coisa!
    # Ele é quem mantém a janela aberta e "escutando" cliques.
    janela.mainloop()

if __name__ == "__main__":
    criar_janela_e_carrinho()