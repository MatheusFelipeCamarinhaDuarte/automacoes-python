import tkinter as tk
from app.root import NovaTela
from app.assets.alertas import alerta_invalido
from app.telas.inserir_dados import tela_de_insercao
from app.assets.botoes_universais import voltar_uma_tela
from app.assets.verificacoes import verifica_nulos

def mostrar_selecao(opcao,var_opcao,sistema):
    selected_option = var_opcao.get()
    if selected_option == 1:
        opcao.config(text=sistema)
    elif selected_option == 2:
        opcao.config(text=sistema)
    elif selected_option == 3:
        opcao.config(text=sistema)
    elif selected_option == 4:
        opcao.config(text=sistema)
    elif selected_option == 5:
        opcao.config(text=sistema)
    else:
        opcao.config(text="Nenhuma opção selecionada")

def escolha_sistema(janela,migracao):
    # Oculta a primeira janela
    janela.withdraw()
    
    # Cria a janela para escolha de sistema
    tela_escolha = NovaTela()
    tela_escolha.title("Escolha o sistema")

    # Dimensões da tela
    largura = 420
    altura = 280
    x = (tela_escolha.winfo_screenwidth() // 2) - (largura // 2)
    y = (tela_escolha.winfo_screenheight() // 2) - (altura // 2)
    tela_escolha.geometry(f"{largura}x{altura}+{x}+{y}")
    
    # Frame superior
    frame_superior = tk.Frame(tela_escolha)
    frame_superior.pack(side=tk.TOP, padx=10, expand=True, fill=tk.BOTH)
    label_titulo = tk.Label(frame_superior, text=f"Migração de {migracao}:")
    label_titulo.pack()

    
    # Criando frame do sistema de origem
    frame1 = tk.Frame(frame_superior,padx=10, pady=10, width=20, height=100)
    frame1.pack(side=tk.LEFT,anchor=tk.N, padx=10)
    label_titulo = tk.Label(frame1, text="Escolha o sistema de origem:")
    label_titulo.pack(anchor=tk.W)
    var_opcao1 = tk.IntVar()
    msys = tk.Radiobutton(frame1, text="EMsys", variable=var_opcao1, value=1, command=lambda: mostrar_selecao(opcao,var_opcao1,'EMsys'))
    msys.pack(anchor=tk.W)
    posto_facil = tk.Radiobutton(frame1, text="Posto Fácil", variable=var_opcao1, value=2, command=lambda: mostrar_selecao(opcao,var_opcao1,"Posto Fácil"))
    posto_facil.pack(anchor=tk.W)
    seller = tk.Radiobutton(frame1, text="Seller", variable=var_opcao1, value=3, command=lambda: mostrar_selecao(opcao,var_opcao1,"Seller"))
    seller.pack(anchor=tk.W)
    outros = tk.Radiobutton(frame1, text="Outros", variable=var_opcao1, value=4, command=lambda: mostrar_selecao(opcao,var_opcao1, "Outros"))
    outros.pack(anchor=tk.W)
    opcao = tk.Label(frame1, text='Nenhuma opção selecionada')
    opcao.pack(anchor=tk.W)

    # Criando frame do sistema de destino
    frame2 = tk.Frame(frame_superior,padx=10, pady=10, width=20, height=100)
    frame2.pack(side=tk.LEFT,anchor=tk.N ,padx=10)
    label_titulo = tk.Label(frame2, text="Escolha o sistema de destino:")
    label_titulo.pack(anchor=tk.W)
    var_opcao2 = tk.IntVar()
    seller = tk.Radiobutton(frame2, text="AutoSystem", variable=var_opcao2, value=5, command=lambda: mostrar_selecao(opcao2,var_opcao2, "AutoSystem"))
    seller.pack(anchor=tk.W)
    opcao2 = tk.Label(frame2, text="Nenhuma opção selecionada")
    opcao2.pack(anchor=tk.W)

    # Criando frame de baixo
    frame_inferior = tk.Frame(tela_escolha)
    frame_inferior.pack(side=tk.BOTTOM, padx=10, expand=True, fill=tk.BOTH)
    button_submit = tk.Button(frame_inferior, text="Proximo", command=lambda: [tela_de_insercao() if (verifica_nulos(var_opcao1.get(),var_opcao2.get())) else alerta_invalido()])
    button_submit.pack()
    frame4 = tk.Frame(frame_inferior)
    frame4.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)
    sair = tk.Button(frame4, text="Sair", command=lambda: janela.quit())
    sair.pack(side=tk.RIGHT, pady=10, padx=10)
    voltar = tk.Button(frame4, text="Voltar", command=lambda: [voltar_uma_tela(janela,tela_escolha)])
    voltar.pack(side=tk.LEFT, pady=10, padx=10)
