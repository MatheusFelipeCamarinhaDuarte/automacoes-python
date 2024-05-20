import tkinter as tk

def alerta_invalido():
    tela_alerta = tk.Toplevel()
    tela_alerta.title("!!!")
    largura = 200
    altura = 100
    x = (tela_alerta.winfo_screenwidth() // 2) - (largura // 2)
    y = (tela_alerta.winfo_screenheight() // 2) - (altura // 2)
    tela_alerta.geometry(f"{largura}x{altura}+{x}+{y}")
    label_titulo = tk.Label(tela_alerta, text=f"Você precisa escolhar uma opção!")
    label_titulo.pack(anchor=tk.CENTER, expand=True, fill=tk.BOTH)
    botao_ok = tk.Button(tela_alerta, text="OK", command=lambda: [tela_alerta.destroy()], width=14)
    botao_ok.pack(anchor=tk.CENTER, pady=10)