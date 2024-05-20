import tkinter as tk
from app.telas.escolha_sistema import escolha_sistema
from app.root import caminho_icone

def tela_inicial():
    #Criação da janela principal
    janela = tk.Tk()
    janela.title("Migração")
    icone = caminho_icone()
    janela.iconbitmap(icone)
    janela.resizable(False, False)

    # Dimensões de tela
    largura_primeira_janela = 250
    altura_primeira_janela = 180
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    x = (largura_tela // 2) - (largura_primeira_janela // 2)
    y = (altura_tela // 2) - (altura_primeira_janela // 2)
    janela.geometry(f"{largura_primeira_janela}x{altura_primeira_janela}+{x}+{y}")

    # Menu de ação das telas de migração
    produtos = tk.Button(janela, text="Migração de produtos", width=30 ,command=lambda: escolha_sistema(janela,'produtos'))
    produtos.pack(anchor=tk.W,pady=5,padx=20)
    inventario = tk.Button(janela, text="Migração de inventario", width=30, command=lambda: escolha_sistema(janela,'inventario'))
    inventario.pack(anchor=tk.W,pady=5,padx=20)
    cliente = tk.Button(janela, text="Migração de clientes", width=30, command=lambda: escolha_sistema(janela,'clientes'))
    cliente.pack(anchor=tk.W,pady=5,padx=20)
    
    # Botao de sair
    sair = tk.Button(janela, text="Sair", command=lambda: janela.quit())
    sair.pack(anchor=tk.SE, pady=20, padx=20)
    
    # Retornando a primeira tela criada
    return janela

if __name__ == "__main__":
    # Criando uma instância da aplicação
    app = tela_inicial()
    # Permanecendo ela em loop
    app.mainloop()
