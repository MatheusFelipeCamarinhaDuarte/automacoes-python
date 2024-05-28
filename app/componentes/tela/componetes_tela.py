try:
    from app.componentes.genericas.icone import NovaTela
except:
    from tkinter import Toplevel as NovaTela
import tkinter as tk
from app.componentes.tela.botoes_universais import botao_sair,botao_voltar

def nova_tela_atual(tela_anterior,largura:int,altura:int, titulo:str):
    # Ocultação da janela anterior
    
    # Dimensões da tela com as informações passadas e sendo direcionadas para o meio da tela
    # Cria a janela nova com o título passado
    tela_atual = NovaTela()
    tela_atual.withdraw()
    xa = (tela_atual.winfo_screenwidth() // 2) - (largura // 2)
    ya = (tela_atual.winfo_screenheight() // 2) - (altura // 2)
    tela_atual.geometry(f"{largura}x{altura}+{xa}+{ya}")
    tela_atual.deiconify()
    tela_atual.title(titulo)
    tela_anterior.withdraw()
    

    # Retorna a janela atual
    return tela_atual


def rodape_da_tela(frame_inferior,janela_principal,tela_anterior,tela_atual):
    frame_rodape = tk.Frame(frame_inferior)
    frame_rodape.pack(anchor=tk.S,expand=True, fill=tk.X)
    botao_voltar(frame_rodape,tela_anterior,tela_atual)
    botao_sair(frame_rodape,janela_principal)
    return frame_rodape

def input_com_titulo(frame_pertencente, titulo:str, largura:int=20,lista=False,padiy:int = 10,padix:int = 10):
    # Cria o label com o título passado
    frame_conjunto = tk.Frame(frame_pertencente)
    frame_conjunto.pack()
    direcao = tk.TOP
    if lista:
        direcao = tk.LEFT
    
    label = tk.Label(frame_conjunto, text=titulo)
    label.pack(side=direcao, pady=padiy, padx=padix)
    
    # Cria o input com a largura passada
    input = tk.Entry(frame_conjunto, width=largura)
    input.pack(side=direcao, pady=padiy, padx=padix)
    
    # if lista:
    #     input.config(state=tk.DISABLED)
    # Retorna o input criado
    return input


def radio_botoes(lista_radio:list, frame_pertencente,orientacao=tk.W,lista:bool=False):
    # Definição da variável que indica o radio_button
    var_opcao = tk.StringVar(value='Nenhuma opção selecionada')
    frame_dos_radio_buttons = tk.Frame(frame_pertencente)
    lado = tk.TOP
    if lista:
        lado = tk.RIGHT
    frame_dos_radio_buttons.pack()

    # Criação de radio_button versionada de acordo com a lista passada
    for texto in lista_radio:
        radio_button = tk.Radiobutton(frame_dos_radio_buttons, text=texto, variable=var_opcao, value=texto, command=lambda: opcao.config(text=var_opcao.get()))
        radio_button.pack(anchor=orientacao,side=lado)

    opcao = tk.Label(frame_pertencente, text=var_opcao.get())
    opcao.pack(anchor=orientacao)
    
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


