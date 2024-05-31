import tkinter as tk

# Exemplo de função para o comando do botão
def baixar_arquivo_relatorio(nome_arquivo, mensagem, janela_principal, janela_secundaria, nome_cliente):
    # Implementação da função
    pass

# Criação da janela principal
janela_principal = tk.Tk()
janela_principal.geometry(f"{300}x{200}")            

# Criação do frame ou janela para a mensagem
mensagem = tk.Frame(janela_principal)
mensagem.pack()

# Nome do arquivo e cliente para o exemplo
nome_arquivo = "exemplo.txt"
nome_cliente = "Cliente Exemplo"

# Criação do botão com tamanho de fonte aumentado
botao = tk.Button(
    mensagem,
    text='Baixar relatório de importação',
    command=lambda: baixar_arquivo_relatorio(nome_arquivo, mensagem, janela_principal, janela_principal, nome_cliente),
    font=("Arial", 12)  # Define a fonte e o tamanho da fonte
)

# Adiciona o botão ao frame
botao.pack()

# Inicia o loop principal do Tkinter
janela_principal.mainloop()
