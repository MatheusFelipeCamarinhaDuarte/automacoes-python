import tkinter as tk
from app.root import NovaTela 
def abrir_segunda_janela(janela):
    # Oculta a primeira janela
    janela.withdraw()
    
    # Cria a segunda janela
    segunda_janela = NovaTela()
    segunda_janela.title("Segunda Janela")
    # Obtém as dimensões e a posição da primeira janela
    # Define a geometria da segunda janela para herdar a altura e a posição da primeira
    largura1 = janela.winfo_width()
    altura1 = janela.winfo_height()
    x1 = janela.winfo_x()
    y1 = janela.winfo_y()
    segunda_janela.geometry(f"{largura1}x{altura1}+{x1}+{y1}")
    
    # Adiciona um botão na segunda janela
    botao2 = tk.Button(segunda_janela, text="Sair", command=lambda: janela.quit())
    botao3 = tk.Button(segunda_janela, text="Voltar para a tela inicial", command=lambda: fechar_segunda_janela(segunda_janela, janela))
    botao2.pack(anchor=tk.E, side=tk.BOTTOM, pady=20, padx=20)
    botao3.pack(anchor=tk.CENTER, side=tk.BOTTOM, padx=20)
    # botao2.place(x=550,y=400)
    # botao3.place(x=520,y=400)
    
    # Intercepta o evento de fechamento da segunda janela
    segunda_janela.protocol("WM_DELETE_WINDOW", lambda: janela.quit())

def fechar_segunda_janela(segunda_janela, janela):
    # Obtém a posição da segunda janela
    x2 = segunda_janela.winfo_x()
    y2 = segunda_janela.winfo_y()
    largura1 = segunda_janela.winfo_width()
    altura1 = segunda_janela.winfo_height()
    
    # Fecha a segunda janela
    segunda_janela.destroy()
    
    # Reposiciona a primeira janela na posição da segunda janela
    janela.geometry(f"{largura1}x{altura1}+{x2}+{y2}")
    
    # Mostra a primeira janela novamente
    janela.deiconify()