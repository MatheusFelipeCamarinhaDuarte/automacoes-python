import tkinter as tk
from app.componentes.genericas.icone import caminho_icone
def alerta_invalido(mensagem):
    tela_alerta = tk.Tk()
    tela_alerta.title("ALERTA!")
    icone = caminho_icone()
    tela_alerta.iconbitmap(icone)
    tela_alerta.resizable(False, False)
    largura = 300
    altura = 100
    x = (tela_alerta.winfo_screenwidth() // 2) - (largura // 2)
    y = (tela_alerta.winfo_screenheight() // 2) - (altura // 2)
    tela_alerta.geometry(f"{largura}x{altura}+{x}+{y}")
    label_titulo = tk.Label(tela_alerta,  wraplength=200, text=mensagem)
    label_titulo.pack(anchor=tk.CENTER, expand=True, fill=tk.BOTH)
    botao_ok = tk.Button(tela_alerta,text="OK", command=lambda: [tela_alerta.destroy()], width=14)
    botao_ok.pack(anchor=tk.CENTER, pady=10)
    tela_alerta.mainloop()