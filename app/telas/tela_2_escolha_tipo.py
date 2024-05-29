from app.componentes.tela.componetes_tela import Janela
def escolha_tipo(janela_principal:Janela):
    
    # Importações
    from app.telas.tela_3_escolha_sistema import tela_de_escolha_sistema
    from tkinter import messagebox
    import tkinter as tk
    
    #Limpa a tela anterior
    janela_principal.limpar()
    
    # Refaz as dimensões da nova tela
    x = (janela_principal.winfo_screenwidth() // 2) - (200 // 2)
    y = (janela_principal.winfo_screenheight() // 2) - (200 // 2)
    janela_principal.geometry(f"{200}x{200}+{x}+{y}")  
    
    # Frame do botão de escolha
    frame = tk.Frame(janela_principal)
    frame.pack()
    
    # Menu de ação das telas de migração
    dicionario = {'PRODUTOS': lambda:[tela_de_escolha_sistema(janela_principal,'PRODUTOS')], 'ESTOQUE': lambda:[messagebox.showerror('Error','Módulo ainda não implantado!')], 'CLIENTES': lambda:[messagebox.showerror('Error','Módulo ainda não implantado!')]}
    janela_principal.multiplos_botoes(dicionario,frame,10)

    # Rodapé dinâmico da tela
    janela_principal.rodape(janela_principal)