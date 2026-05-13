import tkinter as tk

root = tk.Tk()
root.title("Simulador de Investimentos - Sicredi")
root.geometry("400x420")
root.configure(bg="#005c36")
root.resizable(False, False)

#titulo
tk.label(root, text="=== Investimentos de investimentos ===", font=("Arial",14, "bold"), bg="#005c36",fg="#005c36").pack(pady=(50,4))


root.mainloop()
