from app.assets.componetes_tela import nova_tela_atual, rodape_da_tela

def tela_de_insercao(tela_anterior, janela_principal, migracao,sistema_origem,sistema_destino):
    # Oculta a primeira janela e criar a nova
    tela_atual = nova_tela_atual(tela_anterior,300,300,"Inserir Dados")
    print(f"Iremos fazer a migração de {migracao.lower()} do sistema {sistema_origem} para o {sistema_destino}")
    rodape_da_tela(tela_atual,janela_principal,tela_anterior,tela_atual)