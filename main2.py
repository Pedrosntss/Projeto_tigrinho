import tkinter as tk
root = tk.Tk()
root.title("Simulador de Investimentos - Sicredi")
root.geometry("400x420")
root.configure(bg="#005c36")
root.resizable(False, False)


#Título
tk.Label(root,
    text="   Simulador de Investimentos    ",
    font=("Arial", 14, "bold"),
    bg ="#005c36", fg ="#FFFFFF").pack(pady = (50, 4))

tKLabel = tk.Label(root,
    text="Sicredi",
    font=("Arial", "10", "italic"),
    bg="#005c36", fg="#a8d5bc").pack(pady= (0, 20))


#valor inicial
tk.Label(root,
         text= "Valor inicial (R$):",
         font= ("Arial", "10", "bold"),
         bg="#005c36", fg="#FFFFFF").pack(anchor= "w", padx=20)

entrada_principal = tk.Entry(root,
        font=("Arial", 11),
        bg="#FFFFFF", fg="#FF0000",
        relief=tk.FLAT, width=20)
entrada_principal.pack(pady= (4, 13), ipadx=13, ipady=10, fill = tk.X)


root.mainloop()