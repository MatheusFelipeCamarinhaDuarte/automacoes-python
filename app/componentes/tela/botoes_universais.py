import tkinter as tk

def voltar_uma_tela(janela_anterior,janela_atual):
    largura = janela_anterior.winfo_width()
    altura = janela_anterior.winfo_height()
    x = (janela_anterior.winfo_screenwidth() // 2) - (largura // 2)
    y = (janela_anterior.winfo_screenheight() // 2) - (altura // 2)
    # Fecha a janela atual
    janela_atual.destroy()
    # Reposiciona a primeira janela na posição da segunda janela
    janela_anterior.geometry(f"{largura}x{altura}+{x}+{y}")
    # Mostra a primeira janela novamente
    janela_anterior.deiconify()

def botao_voltar(ultimo_frame,tela_anterior,tela_atual):
    voltar = tk.Button(ultimo_frame, text="Voltar", command=lambda: [voltar_uma_tela(tela_anterior,tela_atual)])
    voltar.pack(side=tk.LEFT, pady=10, padx=10)
    return voltar

def botao_sair(ultimo_frame,janela_principal,padix=10,padiy=10):
    sair = tk.Button(ultimo_frame, text="Sair", command=lambda: janela_principal.quit())
    sair.pack(side=tk.RIGHT, pady=padiy, padx=padix)
    return sair

#Teste unitário para a verificação dos componentes
if __name__ == "__main__":
    # Exemplo de uso
    root = tk.Tk()

    frame = tk.Frame(root, width=300, height=300)
    frame.pack()


    root.mainloop()