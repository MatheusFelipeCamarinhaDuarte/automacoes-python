import tkinter as tk
class Janela(tk.Tk):
    """Janela principal da nossa aplicação que herda tk.Tk do Tkinter,
    com o objetivo de ser uma single-page aplication e adiciona funções
    extras como o Limpar
    
    A janela principal já inicia com nome fixo e icone de nossa aplicação,
    além de fixar a largura e altura, e realizar um protocolo correto de quit()
    caso alguém delete a janela pelo botao.
    """
    from typing import Callable, Optional
    def __init__(self):
        """Método de criação de tela personalizada
        """
        from app.componentes.genericas.icone import caminho_icone
        super().__init__()
        self.title("Matheus Solutions")
        self.iconbitmap(caminho_icone())
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", lambda: self.quit())

    def limpar(self):
        """Método para limpar todos os widgets

        Returns:
            Janela: retorna a janela limpa
        """
        for widget in self.winfo_children():
            widget.destroy()
        return self

    def rodape(self, frame_inferior:tk.Frame, func_tela_anterior:Optional[Callable[[], None]] = None) -> tk.Frame:
        """Método que chame e adiciona um frame de rodapé com funções voltar e sair.

        Args:
            frame_inferior (tk.Frame): Frame em que se localiza a parte de baixo da janela.
            func_tela_anterior (function, optional): Aqui fica a função da geração da tela 
            anterior, sem ela, o código não adiciona o botão voltar. Defaults to False.

        Returns:
            tk.Frame: Frame equivalente ao rodape da janela.
        """        
        
        # A partir do frame inferior, cria um outro frame destinado ao rodapé
        frame_rodape = tk.Frame(frame_inferior)
        frame_rodape.pack(anchor=tk.S,expand=True, fill=tk.X)
        
        # Caso tenha a função da tela anterior, adiciona a tela voltar
        if func_tela_anterior:
            voltar = tk.Button(frame_rodape, text="Voltar", command=lambda: [func_tela_anterior(self)])
            voltar.pack(side=tk.LEFT, pady=10, padx=10)
        
        # Adiciona o botão de sair da aplicação com o devido
        sair = tk.Button(frame_rodape, text="Sair", command=lambda: self.quit())
        sair.pack(side=tk.RIGHT, pady=10, padx=10)
        
        # Retorna o frame do rodape (Já ligado ao frame inferior)
        return frame_rodape

    def multiplos_botoes(self, dicionario_botoes:dict, frame_pertencente:tk.Frame, largura_botao:int = 20, orientacao=tk.CENTER) -> list[tk.Button]:
        """Método para criar multiplos botões em sequência um do outro.

        Args:
            dicionario_botoes (dict): um dicionario onde a chave é o text do
            botao e o valor é a função passada por meio de lambda.
            frame_pertencente (tk.Frame): Frame onde o botão será colocado
            largura_botao (int, optional): largura padrão do botão. Defaults to 20.
            orientacao (optional): Orientação do botão (padrão é centro). Defaults to tk.CENTER.

        Returns:
            list[tk.Button]: Retorna uma lista de botões para caso queria modificar algo nele
        """
        # Gera uma lista vazia
        todos = []
        # Para cada nome gerado, cria um botao com a respectiva funcao dele e adiciona na lista
        for texto, funcao in dicionario_botoes.items():
            button = tk.Button(frame_pertencente, text=texto, width=largura_botao,height=1, command=funcao)
            button.pack(anchor=orientacao, pady=5, padx=10)
            todos.append(button)
        return todos
def nova_tela_atual(tela_anterior,largura:int,altura:int, titulo:str):
    try:
        from app.componentes.genericas.icone import NovaTela
    except:
        from tkinter import Toplevel as NovaTela

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
    from app.componentes.tela.botoes_universais import botao_sair,botao_voltar
    
    
    frame_rodape = tk.Frame(frame_inferior)
    frame_rodape.pack(anchor=tk.S,expand=True, fill=tk.X)
    botao_voltar(frame_rodape,tela_anterior,tela_atual)
    botao_sair(frame_rodape,janela_principal)
    return frame_rodape

def novo_rodape(frame_inferior,tela_atual,func_tela_anterior = False):
    from app.componentes.tela.botoes_universais import botao_sair,botao_voltar_novo
    
    frame_rodape = tk.Frame(frame_inferior)
    frame_rodape.pack(anchor=tk.S,expand=True, fill=tk.X)
    if func_tela_anterior:
        botao_voltar_novo(frame_rodape,func_tela_anterior,tela_atual)
    
    botao_sair(frame_rodape,tela_atual)
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

def multiplos_botoes(lista_botoes:list, frame_pertencente,padix:int = 10,padiy:int = 5, largura_botao:int = 20, altura_botao:int = 1, orientacao=tk.CENTER):
    

    todos = []
    for texto in lista_botoes:
        button = tk.Button(frame_pertencente, text=texto, width=largura_botao,height=altura_botao, command=lambda: lista_botoes[texto])
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


