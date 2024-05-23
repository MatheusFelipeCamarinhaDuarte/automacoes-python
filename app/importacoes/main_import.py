from app.assets.conexao_banco import iniciar_banco, finalizar_banco
from app.importacoes.modelos_postos import seller_para_matriz
from app.importacoes.produtos.envio_para_banco import cadastrar_no_banco
def importacoes_para_as(arquivo,objeto_de_transfência:str,sistema_de_origem:str):
    conexao, cursor = iniciar_banco()
    matriz = seller_para_matriz(arquivo)
    
    response = cadastrar_no_banco(cursor,matriz)
    
    finalizar_banco(conexao, cursor)
    


importacoes_para_as()