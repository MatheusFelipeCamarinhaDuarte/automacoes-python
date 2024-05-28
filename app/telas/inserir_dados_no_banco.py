import tkinter as tk
from tkinter import messagebox
from app.componentes.tela.componetes_tela import nova_tela_atual, multiplos_botoes, rodape_da_tela, input_com_titulo
from app.componentes.arquivo.produto.produto_seller_para_matriz import xml_to_matriz_produto
from app.componentes.banco_dados.produto_matriz_para_as import cadastrar_no_banco
def inserir_no_banco(tela_anterior,janela_principal,migracao,sistema_origem,sistema_destino,extensoes):
    # Criação da tela
    tela_atual = nova_tela_atual(tela_anterior,300,400,"Inserir no banco")
    frame_superior = tk.Frame(tela_atual)
    frame_superior.pack()
    
    matriz = xml_to_matriz_produto()
    # fram_input = tk.Frame(frame_superior)
    input_nome_banco = input_com_titulo(frame_pertencente=frame_superior,titulo="Nome do Banco",lista=True)
    input_usuario = input_com_titulo(frame_pertencente=frame_superior,titulo="Usuario do banco",lista=True)
    input_senha = input_com_titulo(frame_pertencente=frame_superior,titulo="Senha do banco",lista=True)
    
    # Menu de ação das telas de migração
    tipos_insercao = ['SUBISTITUIR',"ADICIONAR"]
    b0, b1 = multiplos_botoes(tipos_insercao,frame_superior,20,5,15,1)
    
    b0.config(command=lambda:[cadastrar_no_banco(input_usuario.get(),input_senha.get(),input_nome_banco.get(),matriz, janela_principal=janela_principal,tela_atual=tela_atual, substituir=True) if (input_nome_banco.get() !='' and input_usuario.get() !='' and input_senha.get() !='') else messagebox.showerror("Erro", f"Você precisa preencher todos os campos antes de continuar")])
    b1.config(command=lambda:[cadastrar_no_banco(input_usuario.get(),input_senha.get(),input_nome_banco.get(),matriz, janela_principal=janela_principal,tela_atual=tela_atual) if (input_nome_banco.get() !='' and input_usuario.get() !='' and input_senha.get() !='') else messagebox.showerror("Erro", f"Você precisa preencher todos os campos antes de continuar")])

    frame_inferior = tk.Frame(tela_atual)
    frame_inferior.pack(expand=True, fill=tk.X)
    rodape_da_tela(frame_inferior,janela_principal,tela_anterior,tela_atual)