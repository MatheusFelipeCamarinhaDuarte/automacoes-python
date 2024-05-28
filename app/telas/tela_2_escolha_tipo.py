from app.componentes.tela.componetes_tela import nova_tela_atual, multiplos_botoes, rodape_da_tela
from tkinter import messagebox
import tkinter as tk
from app.componentes.genericas.icone import NovaTela
def escolha_tipo(janela_principal):
    from app.componentes.tela.componetes_tela import novo_rodape
    from app.telas.escolha_sistema import tela_de_escolha_sistema
    from app.telas.tela_1_inicial import tela_inicial 
    from app.componentes.tela.componetes_tela import limpar_frame
    limpar_frame(janela_principal)
    xa = (janela_principal.winfo_screenwidth() // 2) - (300 // 2)
    ya = (janela_principal.winfo_screenheight() // 2) - (300 // 2)
    janela_principal.geometry(f"{300}x{300}+{xa}+{ya}")  

    # Menu de ação das telas de migração
    importacoes = ['PRODUTOS', 'ESTOQUE', 'CLIENTES']
    b0,b1,b2 = multiplos_botoes(importacoes,janela_principal,20,5,15)
    b0.config(command=lambda:tela_de_escolha_sistema(janela_principal,janela_principal,importacoes[0]))
    b1.config(command=lambda:messagebox.showerror('Error','Módulo ainda não implantado!'))
    b2.config(command=lambda:messagebox.showerror('Error','Módulo ainda não implantado!'))
    novo_rodape(janela_principal,janela_principal)