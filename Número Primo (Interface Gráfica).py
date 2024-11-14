import tkinter as tk
from tkinter import messagebox

def verificar_primo():
    try:
        num = int(entry.get())
        if num < 2:
            messagebox.showinfo("Resultado", "Não é um número primo")
            return

        for i in range(2, num):
            if num % i == 0:
                messagebox.showinfo("Resultado", "Não é um número primo")
                return
        messagebox.showinfo("Resultado", "É um número primo")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número inteiro válido.")

# Criar a janela principal
root = tk.Tk()
root.title("Verificador de Número Primo")
root.geometry("400x200")
root.configure(bg="#f0f8ff")  # Cor de fundo

# Título
title_label = tk.Label(root, text="Verificador de Número Primo", font=("Helvetica", 16), bg="#f0f8ff", fg="#4b0082")
title_label.pack(pady=10)

# Entrada de número
entry_label = tk.Label(root, text="Digite um número inteiro:", font=("Helvetica", 12), bg="#f0f8ff")
entry_label.pack(pady=5)

entry = tk.Entry(root, font=("Helvetica", 14), justify="center")
entry.pack(pady=10)

# Botão de verificação
check_button = tk.Button(root, text="Verificar", command=verificar_primo, font=("Helvetica", 12), bg="#7fffd4", fg="#000")
check_button.pack(pady=20)

# Iniciar o loop da interface gráfica
root.mainloop()
