import tkinter as tk
from app.telas.escolha_tipo import escolha_tipo
from app.root import caminho_icone

def tela_inicial():
    #Criação da janela principal
    janela_principal = tk.Tk()
    janela_principal.title("Matheus Solutions")
    icone = caminho_icone()
    janela_principal.iconbitmap(icone)
    janela_principal.resizable(False, False)

    # Dimensões de tela
    largura_primeira_janela = 300
    altura_primeira_janela = 180
    largura_tela = janela_principal.winfo_screenwidth()
    altura_tela = janela_principal.winfo_screenheight()
    x = (largura_tela // 2) - (largura_primeira_janela // 2)
    y = (altura_tela // 2) - (altura_primeira_janela // 2)
    janela_principal.geometry(f"{largura_primeira_janela}x{altura_primeira_janela}+{x}+{y}")
    
    
    apresentacao = tk.Label(janela_principal, text="Projeto de importação de dados para dentro do banco")
    apresentacao.pack(anchor=tk.CENTER, expand=True)
    button = tk.Button(janela_principal, text="INICIAR", width=10,height=1, command=lambda: escolha_tipo(janela_principal))
    button.pack(anchor=tk.CENTER, expand=True)
    
    # # Menu de ação das telas de migração
    # importacoes = ['PRODUTOS', 'ESTOQUE', 'CLIENTES']
    # b0,b1,b2 = multiplos_botoes(importacoes,janela,20,5,30,1)
    # b0.config(command=lambda:tela_de_escolha_sistema(janela,importacoes[0]))
    # b1.config(command=lambda:tela_de_escolha_sistema(janela,importacoes[1]))
    # b2.config(command=lambda:tela_de_escolha_sistema(janela,importacoes[2]))

    
    # # Botao de sair
    # sair = botao_sair(janela,janela,padix=20)

    # Retornando a primeira tela criada
    return janela_principal

if __name__ == "__main__":
    # Criando uma instância da aplicação
    app = tela_inicial()
    # Permanecendo ela em loop
    app.mainloop()
