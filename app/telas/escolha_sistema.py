import tkinter as tk
from app.root import NovaTela

def mostrar_selecao(label_selecao,var_opcao):
    selected_option = var_opcao.get()
    if selected_option == 1:
        label_selecao.config(text="Opção selecionada: EMsys")
    elif selected_option == 2:
        label_selecao.config(text="Opção selecionada: Posto Fácil")
    elif selected_option == 3:
        label_selecao.config(text="Opção selecionada: Seller")
    elif selected_option == 4:
        label_selecao.config(text="Opção selecionada: Outros")
    elif selected_option == 5:
        label_selecao.config(text="Opção selecionada: AutoSystem")
    else:
        label_selecao.config(text="Nenhuma opção selecionada")

def escolha_sistema(janela,migracao):
    # Oculta a primeira janela
    janela.withdraw()
    
    # Cria a segunda janela
    tela_escolha = NovaTela()
    tela_escolha.title("Escolha o sistema")
    # Obtém as dimensões e a posição da primeira janela
    # Define a geometria da segunda janela para herdar a altura e a posição da primeira
    largura1 = janela.winfo_width()
    altura1 = janela.winfo_height()
    x1 = janela.winfo_x()
    y1 = janela.winfo_y()
    tela_escolha.geometry(f"{largura1}x{altura1}+{x1}+{y1}")
    
    # Criando um botão
    frame_inferior = tk.Frame(tela_escolha,bg="blue")
    frame_inferior.pack(side=tk.BOTTOM, padx=10, pady=10, expand=True, fill=tk.BOTH)
    button_submit = tk.Button(frame_inferior, text="Proximo", command=lambda: print("lorem ipsum"))
    button_submit.pack(pady=20)
    frame4 = tk.Frame(frame_inferior,bg="red")
    frame4.pack(side=tk.RIGHT)
    botao2 = tk.Button(frame4, text="Sair", command=lambda: janela.quit())
    botao2.pack(side=tk.RIGHT, pady=10, padx=10)
    frame_superior = tk.Frame(tela_escolha,bg="green")
    frame_superior.pack(side=tk.TOP, padx=10, pady=10, expand=True, fill=tk.BOTH)
    # Criando variável de controle para os radiobuttons
    frame1 = tk.Frame(frame_superior,bg="yellow")
    frame1.pack(side=tk.LEFT, padx=10, pady=10)
    label_titulo = tk.Label(frame1, text="Escolha o sistema de origem:")
    label_titulo.pack(anchor=tk.W, padx=20)
    var_opcao1 = tk.IntVar()
    msys = tk.Radiobutton(frame1, text="EMsys", variable=var_opcao1, value=1, command=lambda: mostrar_selecao(label_selecao,var_opcao1))
    msys.pack(anchor=tk.W, padx=20)
    posto_facil = tk.Radiobutton(frame1, text="Posto Fácil", variable=var_opcao1, value=2, command=lambda: mostrar_selecao(label_selecao,var_opcao1))
    posto_facil.pack(anchor=tk.W, padx=20)
    seller = tk.Radiobutton(frame1, text="Seller", variable=var_opcao1, value=3, command=lambda: mostrar_selecao(label_selecao,var_opcao1))
    seller.pack(anchor=tk.W, padx=20)
    outros = tk.Radiobutton(frame1, text="Outros", variable=var_opcao1, value=4, command=lambda: mostrar_selecao(label_selecao,var_opcao1))
    outros.pack(anchor=tk.W, padx=20)
    label_selecao = tk.Label(frame1, text="Nenhuma opção selecionada")
    label_selecao.pack(anchor=tk.W, padx=20)
    
    # Criando variável de controle para os radiobuttons
    frame2 = tk.Frame(frame_superior,bg="purple")
    frame2.pack(padx=10, pady=10)
    label_titulo = tk.Label(frame2, text="Escolha o sistema de destino:")
    label_titulo.pack(anchor=tk.W, padx=20)
    
    var_opcao2 = tk.IntVar()
    seller = tk.Radiobutton(frame2, text="AutoSystem", variable=var_opcao2, value=5, command=lambda: mostrar_selecao(label_selecao2,var_opcao2))
    seller.pack(anchor=tk.W, padx=20)
    label_selecao2 = tk.Label(frame2, text="Nenhuma opção selecionada")
    label_selecao2.pack(anchor=tk.W, padx=20)

