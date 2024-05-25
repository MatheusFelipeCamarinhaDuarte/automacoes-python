from app.componentes.tela.componetes_tela import nova_tela_atual, multiplos_botoes, rodape_da_tela
from app.telas.escolha_sistema import tela_de_escolha_sistema

def escolha_tipo(janela_principal):
    tela_atual = nova_tela_atual(janela_principal,250,180,"IMPORTAÇÃO")
    # Menu de ação das telas de migração
    importacoes = ['PRODUTOS', 'ESTOQUE', 'CLIENTES']
    b0,b1,b2 = multiplos_botoes(importacoes,tela_atual,20,5,15)
    b0.config(command=lambda:tela_de_escolha_sistema(janela_principal,tela_atual,importacoes[0]))
    b1.config(command=lambda:tela_de_escolha_sistema(janela_principal,tela_atual,importacoes[1]))
    b2.config(command=lambda:tela_de_escolha_sistema(janela_principal,tela_atual,importacoes[2]))
    rodape_da_tela(tela_atual,janela_principal,janela_principal,tela_atual)