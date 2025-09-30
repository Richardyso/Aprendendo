import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        dias = int(entry_dias.get())
        if dias <= 0:
            raise ValueError("Número de dias deve ser maior que zero.")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido de dias.")
        return

    valores = text_diarias.get("1.0", tk.END).strip().splitlines()

    if dias == 1:
        if len(valores) != 1:
            messagebox.showerror("Erro", "Insira apenas o valor de 1 diária.")
            return
        try:
            diaria = float(valores[0].replace(",", "."))
            resultado = diaria * 1.05
            label_resultado.config(text=f"Valor total com ISS: R$ {resultado:.2f}")
        except ValueError:
            messagebox.showerror("Erro", "Valor de diária inválido.")
    else:
        if len(valores) != dias:
            messagebox.showerror("Erro", f"Insira {dias} valores de diárias (um por linha).")
            return
        total = 0
        try:
            for valor in valores:
                diaria = float(valor.replace(",", "."))
                total += diaria * 1.05
            label_resultado.config(text=f"Valor total com ISS: R$ {total:.2f}")
        except ValueError:
            messagebox.showerror("Erro", "Um ou mais valores de diária são inválidos.")

# Janela principal
root = tk.Tk()
root.title("Calculadora de Diárias com ISS")
root.geometry("400x400")
root.configure(bg="#f0f4f8")

# Estilo
font_titulo = ("Arial", 14, "bold")
font_normal = ("Arial", 11)

# Título
titulo = tk.Label(root, text="Calculadora de Diárias", font=font_titulo, bg="#f0f4f8", fg="#333")
titulo.pack(pady=10)

# Entrada de dias
frame_dias = tk.Frame(root, bg="#f0f4f8")
frame_dias.pack(pady=5)
tk.Label(frame_dias, text="Quantidade de dias:", font=font_normal, bg="#f0f4f8").pack(side="left")
entry_dias = tk.Entry(frame_dias, width=5)
entry_dias.pack(side="left", padx=5)

# Entrada de valores
label_diarias = tk.Label(root, text="Digite os valores das diárias (1 por linha):", font=font_normal, bg="#f0f4f8")
label_diarias.pack(pady=5)
text_diarias = tk.Text(root, height=10, width=40)
text_diarias.pack()

# Botão calcular
btn_calcular = tk.Button(root, text="Calcular", command=calcular, font=font_normal, bg="#4CAF50", fg="white")
btn_calcular.pack(pady=10)

# Resultado
label_resultado = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#f0f4f8", fg="#000")
label_resultado.pack(pady=10)

root.mainloop()
