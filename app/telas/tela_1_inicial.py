def tela_inicial():
    """Janela Principal da aplicação, com o intuito de inciar aplicação e não retornar a está tela novamente.

    Returns:
        tk.Tk: Retorna uma tela Tk.
    """
    
    # Importações
    import tkinter as tk
    from app.telas.tela_2_escolha_tipo import escolha_tipo
    from app.componentes.genericas.icone import caminho_icone
    from app.componentes.tela.componetes_tela import Janela
    
    # Criação da janela principal
    # janela_principal = tk.Tk()
    janela_principal = Janela()
    janela_principal.withdraw()
    # Colocado o título e caminho de icone para a janela
    janela_principal.title("Matheus Solutions")
    icone = caminho_icone()
    janela_principal.iconbitmap(icone)
    janela_principal.deiconify()
    
    # Travando as dimensões da janela
    janela_principal.resizable(False, False)
    
    # Colocando as dimensões iniciais (e fixas) da tela
    altura = 400
    largura = 550
    x = (janela_principal.winfo_screenwidth() // 2) - (largura // 2)
    y = (janela_principal.winfo_screenheight() // 2) - (altura // 2)
    janela_principal.geometry(f"{largura}x{altura}+{x}+{y}")
    
    # Colocando a linha de apresentação do projeto
    apresentacao = tk.Label(janela_principal, text="Projeto de importação de dados para dentro do banco")
    apresentacao.pack(anchor=tk.CENTER, expand=True)
    
    # Colocando a linha de inícia do código em si. Uma vez colocado, ele não volta para cá
    button = tk.Button(janela_principal, text="INICIAR", width=10,height=1, command=lambda: escolha_tipo(janela_principal))
    button.pack(anchor=tk.CENTER, expand=True)
    
    # Retornando a primeira tela criada
    return janela_principal




# Teste individual da tela.
if __name__ == "__main__":
    app = tela_inicial()
    app.mainloop()