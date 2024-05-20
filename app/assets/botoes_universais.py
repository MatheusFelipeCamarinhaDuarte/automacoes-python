def voltar_uma_tela(janela_anterior,janela_atual):
    largura = janela_anterior.winfo_width()
    altura = janela_anterior.winfo_height()
    x = (janela_anterior.winfo_screenwidth() // 2) - (largura // 2)
    y = (janela_anterior.winfo_screenheight() // 2) - (altura // 2)
    
    # Fecha a janela atual
    janela_atual.destroy()
    # Reposiciona a primeira janela na posição da segunda janela
    janela_anterior.geometry(f"{largura}x{altura}+{x}+{y}")
    # Mostra a primeira janela novamente
    janela_anterior.deiconify()
    
def mostrar_selecionado(opcao,var_opcao,sistema):
    selected_option = var_opcao.get()
    if selected_option == 1:
        opcao.config(text=sistema)
    elif selected_option == 2:
        opcao.config(text=sistema)
    elif selected_option == 3:
        opcao.config(text=sistema)
    elif selected_option == 4:
        opcao.config(text=sistema)
    elif selected_option == 5:
        opcao.config(text=sistema)
    else:
        opcao.config(text="Nenhuma opção selecionada")
