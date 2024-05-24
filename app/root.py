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
        self.withdraw()
        xa = (self.winfo_screenwidth() // 2) - (300 // 2)
        ya = (self.winfo_screenheight() // 2) - (300 // 2)
        self.geometry(f"{300}x{300}+{xa}+{ya}")
        self.deiconify()

        self.protocol("WM_DELETE_WINDOW", lambda: self.quit())
        