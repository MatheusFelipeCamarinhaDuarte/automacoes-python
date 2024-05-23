import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import shutil
import os
# serve para separar os testes do main principal
try:
    from app.assets.verificacoes import verifica_vazios
except:
    from verificacoes import verifica_vazios

def selecionar_arquivo(extensao_desejada):
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
            diretorio_atual = os.path.dirname(os.path.abspath(__file__))
            caminho_app = os.path.dirname(diretorio_atual)
            caminho_absoluto = os.path.join(caminho_app, 'dados')
            
            # Capturo o nome antigo do arquivo e defino para um outro nome para ser o padrão
            antigo_nome = os.path.join(caminho_app, 'dados',nome_arquivo)
            novo_nome = os.path.join(caminho_app, 'dados','arquivo_temporario'+extensao_arquivo)
            
            # Copio e renomeio o arquivo 
            shutil.copy(arquivo_selecionado, caminho_absoluto)
            shutil.move(antigo_nome,novo_nome)
        else:
            # Caso a extensão não seja equivalente ao pedido, ele vai indicar qual a indicada.
            messagebox.showerror("Erro", f"Extensão inválida, o arquivo precisa ser {extensao_desejada}.")
    else:
        messagebox.showerror("Erro", "Nenhum arquivo selecionado.")

def deletar_arquivo_temp(extensao_desejada):
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_app = os.path.dirname(diretorio_atual)
    caminho_absoluto = os.path.join(caminho_app, 'dados')
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