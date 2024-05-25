import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import shutil
import os
from app.telas.inserir_dados_no_banco import inserir_no_banco

def selecionar_arquivo(tela_atual,janela_principal,migracao,sistema_origem,sistema_destino,extensao_desejada):
    # Pede ao usuário o arquivo
    arquivo_selecionado = filedialog.askopenfilename()
    
    # Verifica se o arquivo existe ou não. Se não existir, o programa alerta nenhuma caminho indicado
    if arquivo_selecionado:
        # Recupero o nome e a extensão original do arquivo
        nome_arquivo = os.path.basename(arquivo_selecionado)
        extensao_arquivo = os.path.splitext(arquivo_selecionado)[1]
        
        # Verifico se o arquivo que me entregou está no formato pedido:
        if extensao_arquivo == extensao_desejada:
            # Uso para referenciar a pasta onde ficara temporariamente os dados.
            caminho_app = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            
            caminho_absoluto = os.path.join(caminho_app, 'temp','dados')
            
            # Capturo o nome antigo do arquivo e defino para um outro nome para ser o padrão
            antigo_nome = os.path.join(caminho_absoluto,nome_arquivo)
            novo_nome = os.path.join(caminho_absoluto,'arquivo_temporario'+extensao_arquivo)
            
            # Copio e renomeio o arquivo 
            shutil.copy(arquivo_selecionado, caminho_absoluto)
            shutil.move(antigo_nome,novo_nome)
            inserir_no_banco(tela_atual,janela_principal,migracao,sistema_origem,sistema_destino,extensao_desejada)
        else:
            # Caso a extensão não seja equivalente ao pedido, ele vai indicar qual a indicada.
            messagebox.showerror("Erro", f"Extensão inválida, o arquivo precisa ser {extensao_desejada}.")
    else:
        messagebox.showerror("Erro", "Nenhum arquivo selecionado.")

def deletar_arquivo_temp(extensao_desejada):
    caminho_app = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    caminho_absoluto = os.path.join(caminho_app,'temp', 'dados')
    caminho_do_arquivo = os.path.join(caminho_absoluto, "arquivo_temporario"+extensao_desejada)
    os.remove(caminho_do_arquivo)

def coloca_arquivo_dentro_exe():
    # Criando a janela principal
    root = tk.Tk()
    root.title("Exemplo de Tkinter")
    root.geometry("300x200")

    # Criando um botão para selecionar arquivo
    extensao_desejavel = '.xml'
    button_selecionar = tk.Button(root, text="Selecionar Arquivo", command=lambda:[selecionar_arquivo(extensao_desejavel)])
    button_selecionar.pack()
    button_selecionar = tk.Button(root, text="deltar arquivo", command=lambda:[deletar_arquivo_temp(extensao_desejavel)])
    button_selecionar.pack()

    # Criando um botão para baixar o arquivo selecionado
    # button_baixar = tk.Button(root, text="Baixar Arquivo", command=lambda: baixar_arquivo_no_exe())
    # button_baixar.pack()

    # Criando um rótulo para mostrar o arquivo selecionado


    # Executando o loop principal da aplicação
    root.mainloop()
if __name__ == "__main__":
    coloca_arquivo_dentro_exe()