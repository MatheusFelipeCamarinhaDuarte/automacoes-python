def tela_inicial():
    import tkinter as tk
    from app.telas.tela_2_escolha_tipo import escolha_tipo
    from app.componentes.genericas.icone import caminho_icone
    #Criação da janela principal
    janela_principal = tk.Tk()
    janela_principal.withdraw()
    janela_principal.title("Matheus Solutions")
    icone = caminho_icone()
    janela_principal.iconbitmap(icone)
    janela_principal.resizable(False, False)
    
    # Dimensões de tela
    janela_principal.geometry(f"{550}x{400}+{(janela_principal.winfo_screenwidth() // 2) - (550 // 2)}+{(janela_principal.winfo_screenheight() // 2) - (400 // 2)}")
    janela_principal.deiconify()
    
    apresentacao = tk.Label(janela_principal, text="Projeto de importação de dados para dentro do banco")
    apresentacao.pack(anchor=tk.CENTER, expand=True)
    
    button = tk.Button(janela_principal, text="INICIAR", width=10,height=1, command=lambda: escolha_tipo(janela_principal))
    button.pack(anchor=tk.CENTER, expand=True)
    
    # Retornando a primeira tela criada
    return janela_principal

