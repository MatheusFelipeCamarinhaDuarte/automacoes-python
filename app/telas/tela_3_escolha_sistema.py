from app.componentes.tela.componetes_tela import Janela


def tela_de_escolha_sistema(janela_principal:Janela,migracao:str):
    import tkinter as tk
    from app.componentes.tela.componetes_tela import radio_botoes
    from app.componentes.tela.alertas import alerta_invalido
    from app.componentes.genericas.verificacoes import verifica_outros
    from app.telas.escolha_tabela import tela_de_insercao
    from app.telas.tela_2_escolha_tipo import escolha_tipo
    #Limpa a tela anterior
    janela_principal.limpar()
    
    # Refaz as dimensões da nova tela
    x = (janela_principal.winfo_screenwidth() // 2) - (420 // 2)
    y = (janela_principal.winfo_screenheight() // 2) - (280 // 2)
    janela_principal.geometry(f"{420}x{280}+{x}+{y}")
    janela_principal.title("Escolha o sistema")  
    
    
    
    # Frame superior
    frame_superior = tk.Frame(janela_principal)
    frame_superior.pack(side=tk.TOP, padx=10, expand=True, fill=tk.BOTH)
    label_titulo = tk.Label(frame_superior, text=f"Importação de {migracao.lower()}:")
    label_titulo.pack()
    
    # Criando frame do sistema de origem
    frame_sistema_origem = tk.Frame(frame_superior,padx=10, pady=10, width=20, height=100)
    frame_sistema_origem.pack(side=tk.LEFT,anchor=tk.N, padx=10)
    label_titulo = tk.Label(frame_sistema_origem, text="Escolha o sistema de origem:")
    label_titulo.pack(anchor=tk.W)
    
    # sistemas_origem = ["EMsys","Posto Fácil", "Seller", "Outros"]
    sistemas_origem = ["Seller"]
    var_origem = radio_botoes(sistemas_origem,frame_sistema_origem)

    # Criando frame do sistema de destino
    frame_sistema_destino = tk.Frame(frame_superior,padx=10, pady=10, width=20, height=100)
    frame_sistema_destino.pack(side=tk.LEFT,anchor=tk.N ,padx=10)
    label_titulo = tk.Label(frame_sistema_destino, text="Escolha o sistema de destino:")
    label_titulo.pack(anchor=tk.W)
    sistemas_destino = ["AutoSystem"]
    var_destino = radio_botoes(sistemas_destino,frame_sistema_destino)


    # Criando frame de baixo
    frame_inferior = tk.Frame(janela_principal)
    frame_inferior.pack(side=tk.BOTTOM, padx=10, expand=True, fill=tk.BOTH)
    button_submit = tk.Button(frame_inferior, text="Proximo", command=lambda: [tela_de_insercao(janela_principal,janela_principal,migracao,var_origem.get(),var_destino.get()) if (verifica_outros('Nenhuma opção selecionada',var_origem.get(),var_destino.get())) else alerta_invalido("Você precisa escolher o campo de origem e destino antes de prosseguir!")])
    button_submit.pack()
    
    # Rodapé dinâmico
    janela_principal.rodape(frame_inferior,escolha_tipo)


