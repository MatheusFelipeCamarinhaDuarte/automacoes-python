try:
    from app.root import NovaTela
except:
    from tkinter import Toplevel as NovaTela
import tkinter as tk
from app.assets.botoes_universais import botao_sair,botao_voltar

def nova_tela_atual(tela_anterior,largura:int,altura:int, titulo:str):
    # Ocultação da janela anterior
    tela_anterior.withdraw()
    
    # Cria a janela nova com o título passado
    tela_atual = NovaTela()
    tela_atual.title(titulo)
    
    # Dimensões da tela com as informações passadas e sendo direcionadas para o meio da tela
    x = (tela_atual.winfo_screenwidth() // 2) - (largura // 2)
    y = (tela_atual.winfo_screenheight() // 2) - (altura // 2)
    tela_atual.geometry(f"{largura}x{altura}+{x}+{y}")

    # Retorna a janela atual
    return tela_atual
import tkinter as tk


def rodape_da_tela(frame_inferior,janela_principal,tela_anterior,tela_atual):
    frame_rodape = tk.Frame(frame_inferior)
    frame_rodape.pack( expand=True, fill=tk.BOTH)
    botao_voltar(frame_rodape,tela_anterior,tela_atual)
    botao_sair(frame_rodape,janela_principal)
    return frame_rodape



def radio_botoes(lista_radio:list, frame_pertencente):
    # Definição da variável que indica o radio_button
    var_opcao = tk.StringVar(value='Nenhuma opção selecionada')

    # Criação de radio_button versionada de acordo com a lista passada
    for texto in lista_radio:
        radio_button = tk.Radiobutton(frame_pertencente, text=texto, variable=var_opcao, value=texto, command=lambda: opcao.config(text=var_opcao.get()))
        radio_button.pack(anchor=tk.W)

    opcao = tk.Label(frame_pertencente, text=var_opcao.get())
    opcao.pack(anchor=tk.W)
    
    # Retorna a variável que mantém o valor selecionado
    return var_opcao

def multiplos_botoes(dicionario_botoes:list, frame_pertencente,padix:int = 10,padiy:int = 5, largura_botao:int = 20, altura_botao:int = 1, orientacao=tk.CENTER):
    todos = []
    for texto in dicionario_botoes:
        button = tk.Button(frame_pertencente, text=texto, width=largura_botao,height=altura_botao, command=lambda: dicionario_botoes[texto])
        button.pack(anchor=orientacao,pady=padiy,padx=padix)
        todos.append(button)
    # print(todos)
    return todos
# Teste unitário para verificação dos componentes
if __name__ == "__main__":
    # Exemplo de uso
    root = tk.Tk()

    new_root = nova_tela_atual(root,400,400,"NOVA TELA TESTE")

    frame = tk.Frame(new_root)
    frame.pack()

    # Lista de opções para os RadioButtons
    opcoes = ['Opção 1', 'Opção 2', 'Opção 3']

    # Chama a função para criar os RadioButtons
    radio_var = radio_botoes(opcoes, frame)

    root.mainloop()


