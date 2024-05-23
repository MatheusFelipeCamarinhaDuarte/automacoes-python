import tkinter as tk
from app.assets.componetes_tela import nova_tela_atual, radio_botoes, rodape_da_tela
from app.assets.alertas import alerta_invalido
from app.assets.verificacoes import verifica_outros
from app.telas.escolha_tabela import tela_de_insercao


def tela_de_escolha_sistema(janela_principal,tela_anterior,migracao:str):
    # criação da nova tela
    tela_atual = nova_tela_atual(tela_anterior=tela_anterior, largura=420, altura=280 , titulo="Escolha o sistema")
    
    # Frame superior
    frame_superior = tk.Frame(tela_atual)
    frame_superior.pack(side=tk.TOP, padx=10, expand=True, fill=tk.BOTH)
    label_titulo = tk.Label(frame_superior, text=f"Importação de {migracao.lower()}:")
    label_titulo.pack()

    
    # Criando frame do sistema de origem
    frame_sistema_origem = tk.Frame(frame_superior,padx=10, pady=10, width=20, height=100)
    frame_sistema_origem.pack(side=tk.LEFT,anchor=tk.N, padx=10)
    label_titulo = tk.Label(frame_sistema_origem, text="Escolha o sistema de origem:")
    label_titulo.pack(anchor=tk.W)
    sistemas_origem = ["EMsys","Posto Fácil", "Seller", "Outros"]
    var_origem = radio_botoes(sistemas_origem,frame_sistema_origem)

    # Criando frame do sistema de destino
    frame_sistema_destino = tk.Frame(frame_superior,padx=10, pady=10, width=20, height=100)
    frame_sistema_destino.pack(side=tk.LEFT,anchor=tk.N ,padx=10)
    label_titulo = tk.Label(frame_sistema_destino, text="Escolha o sistema de destino:")
    label_titulo.pack(anchor=tk.W)
    sistemas_destino = ["AutoSystem"]
    var_destino = radio_botoes(sistemas_destino,frame_sistema_destino)


    # Criando frame de baixo
    frame_inferior = tk.Frame(tela_atual)
    frame_inferior.pack(side=tk.BOTTOM, padx=10, expand=True, fill=tk.BOTH)
    button_submit = tk.Button(frame_inferior, text="Proximo", command=lambda: [tela_de_insercao(tela_atual,janela_principal,migracao,var_origem.get(),var_destino.get()) if (verifica_outros('Nenhuma opção selecionada',var_origem.get(),var_destino.get())) else alerta_invalido("Você precisa escolher o campo de origem e destino antes de prosseguir!")])
    button_submit.pack()
    
    rodape_da_tela(frame_inferior,janela_principal,tela_anterior,tela_atual)



