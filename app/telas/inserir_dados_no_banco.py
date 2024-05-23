import tkinter as tk
from app.assets.componetes_tela import nova_tela_atual, multiplos_botoes, rodape_da_tela
from app.telas.escolha_sistema import tela_de_escolha_sistema
from app.importacoes.modelos_postos.seller_para_matriz import xml_to_matriz_produto
def inserir_no_banco(tela_anterior,janela_principal,migracao,sistema_origem,sistema_destino,extensoes):
    # Criação da tela
    tela_atual = nova_tela_atual(tela_atual,300,300,"Inserir no banco")
    frame_superior = tk.Frame(tela_atual)
    frame_superior.pack()
    
    matriz = xml_to_matriz_produto()
    
    # Menu de ação das telas de migração
    tipos_insercao = ['SUBISTITUIR', 'ADICIONAR']
    b0,b1 = multiplos_botoes(tipos_insercao,frame_superior,20,15,25,1)
    b0.config(command=lambda:[])
    b1.config(command=lambda:[])

    frame_inferior = tk.Frame(tela_atual)
    frame_inferior.pack()
    rodape_da_tela(frame_inferior,janela_principal,tela_anterior,tela_atual)