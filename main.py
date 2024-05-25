import tkinter as tk
from app.telas.escolha_tipo import escolha_tipo
from app.componentes.genericas.icone import caminho_icone
from app.chave.conexao_firebase import conexao
from app.componentes.tela.alertas import alerta_invalido
from tkinter import messagebox



def tela_inicial():
    #Criação da janela principal
    janela_principal = tk.Tk()
    janela_principal.withdraw()
    janela_principal.title("Matheus Solutions")
    icone = caminho_icone()
    janela_principal.iconbitmap(icone)
    janela_principal.resizable(False, False)
    
    # Dimensões de tela
    janela_principal.geometry(f"{300}x{180}+{(janela_principal.winfo_screenwidth() // 2) - (300 // 2)}+{(janela_principal.winfo_screenheight() // 2) - (180 // 2)}")
    janela_principal.deiconify()
    
    apresentacao = tk.Label(janela_principal, text="Projeto de importação de dados para dentro do banco")
    apresentacao.pack(anchor=tk.CENTER, expand=True)
    button = tk.Button(janela_principal, text="INICIAR", width=10,height=1, command=lambda: escolha_tipo(janela_principal))
    button.pack(anchor=tk.CENTER, expand=True)
    
    # Retornando a primeira tela criada
    return janela_principal

if __name__ == "__main__":
    
    # app = tela_inicial()
    # app.mainloop()
    conectado = conexao()
    if conectado == True or conectado == False:
        if conectado:
            app = tela_inicial()
            app.mainloop()
        else:
            messagebox.showerror("Erro", "Você não tem um certificado válido")
            # alerta_invalido("Você não tem um certificado válido")
