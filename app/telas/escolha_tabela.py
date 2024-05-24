import tkinter as tk
import webbrowser
from tkinter import messagebox
from app.assets.componetes_tela import nova_tela_atual, rodape_da_tela, radio_botoes
from app.assets.pegar_arquivo_tranferencia import selecionar_arquivo
def tela_de_insercao(tela_anterior, janela_principal, migracao,sistema_origem,sistema_destino):
    # Oculta a primeira janela e criar a nova
    tela_atual = nova_tela_atual(tela_anterior,300,230,"Inserir Dados")
    
    frame_superior = tk.Frame(tela_atual)
    frame_superior.pack(side=tk.TOP, padx=10,pady=20, expand=True, fill=tk.BOTH)
    extensoes_aceitas = ['.xml','.csv','.xls']
    var_extensoes = radio_botoes(extensoes_aceitas,frame_superior, orientacao=tk.CENTER, lista=True)
    
    button_selecionar = tk.Button(frame_superior, text="Selecionar Arquivo", command=lambda:[selecionar_arquivo(tela_atual,janela_principal,migracao,sistema_origem,sistema_destino,var_extensoes.get()) if (var_extensoes.get() !='Nenhuma opção selecionada') else messagebox.showerror("Erro", f"Selecione uma extensão antes de prosseguir.")])
    button_selecionar.pack(pady=20)
    
    
    
    frame_inferior = tk.Frame(tela_atual)
    frame_inferior.pack(side=tk.BOTTOM, padx=10, expand=True, fill=tk.BOTH)    
    rodape_da_tela(frame_inferior=frame_inferior,tela_anterior=tela_anterior,janela_principal=janela_principal,tela_atual=tela_atual)
    
    sub_frame = tk.Frame(frame_inferior)
    sub_frame.pack(anchor=tk.S)
    
    texto = tk.Label(sub_frame, height=2, wraplength=250,text=f"como retirar relatorios no formato correto de dentro do {sistema_origem}?", )
    texto.pack(anchor=tk.S)
    link = "https://google.com"
    texto.config(foreground='blue', underline=True)
    texto.bind("<Button-1>", lambda event: webbrowser.open(link))
