import tkinter as tk
from app.telas.escolha_sistema import escolha_sistema
from app.root import caminho_icone

def tela_inicial():
    # Cria a primeira janela
    janela = tk.Tk()
    janela.title("Migração")
    icone = caminho_icone()
    janela.iconbitmap(icone)

    # Define o tamanho da primeira janela
    largura_primeira_janela = 250
    altura_primeira_janela = 180

    # Obtém a largura e altura da tela
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    # Calcula a posição x e y para centralizar a janela
    x = (largura_tela // 2) - (largura_primeira_janela // 2)
    y = (altura_tela // 2) - (altura_primeira_janela // 2)

    # Define a geometria da primeira janela
    janela.geometry(f"{largura_primeira_janela}x{altura_primeira_janela}+{x}+{y}")
    janela.resizable(False, False)
    
    # Adiciona um botão na primeira janela
    produtos = tk.Button(janela, text="Migração de produtos", width=30 ,command=lambda: escolha_sistema(janela,'produtos'))
    produtos.pack(anchor=tk.W,pady=5,padx=20)
    inventario = tk.Button(janela, text="Migração de inventario", width=30, command=lambda: escolha_sistema(janela,'inventario'))
    inventario.pack(anchor=tk.W,pady=5,padx=20)
    cliente = tk.Button(janela, text="Migração de clientes", width=30, command=lambda: escolha_sistema(janela,'clientes'))
    cliente.pack(anchor=tk.W,pady=5,padx=20)
    botao2 = tk.Button(janela, text="Sair", command=lambda: janela.quit())
    botao2.pack(anchor=tk.SE, pady=20, padx=20)
    
    # Inicia o loop principal da primeira janela
    return janela
    # janela.mainloop()

if __name__ == "__main__":
    # Criando uma instância da aplicação
    app = tela_inicial()
    app.mainloop()
