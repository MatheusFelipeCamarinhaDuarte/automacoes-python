import os
import tkinter as tk
def caminho_icone():
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    # Define o caminho para o arquivo de ícone
    caminho_icone = os.path.join(diretorio_atual, "icons", "ms3.ico")
    return caminho_icone

class NovaTela(tk.Toplevel):
    def __init__ (self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.iconbitmap(caminho_icone())
        self.resizable(False, False)

        self.protocol("WM_DELETE_WINDOW", lambda: self.quit())
        