from app.componentes.tela.componetes_tela import nova_tela_atual, multiplos_botoes, rodape_da_tela
from app.telas.escolha_sistema import tela_de_escolha_sistema
from tkinter import messagebox
import tkinter as tk
from app.componentes.genericas.icone import NovaTela
def escolha_tipo(janela_principal):
    # tela_atual = nova_tela_atual(janela_principal,250,180,"IMPORTAÇÃO")
    tela_atual = NovaTela()
    xa = (tela_atual.winfo_screenwidth() // 2) - (200 // 2)
    ya = (tela_atual.winfo_screenheight() // 2) - (200 // 2)
    tela_atual.geometry(f"{200}x{200}+{xa}+{ya}")  
    janela_principal.withdraw()
    # Menu de ação das telas de migração
    importacoes = ['PRODUTOS', 'ESTOQUE', 'CLIENTES']
    b0,b1,b2 = multiplos_botoes(importacoes,tela_atual,20,5,15)
    b0.config(command=lambda:tela_de_escolha_sistema(janela_principal,tela_atual,importacoes[0]))
    b1.config(command=lambda:messagebox.showerror('Error','Módulo ainda não implantado!'))
    b2.config(command=lambda:messagebox.showerror('Error','Módulo ainda não implantado!'))
    rodape_da_tela(tela_atual,janela_principal,janela_principal,tela_atual)