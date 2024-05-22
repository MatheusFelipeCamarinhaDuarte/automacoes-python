from app.assets.conexao_banco import iniciar_banco, finalizar_banco
from app.importacoes.modelos_postos.seller.xml import xml_em_matriz_seller_produtos
from app.importacoes.produtos.envio_para_banco import cadastrar_no_banco
def importacoes():
    conexao, cursor = iniciar_banco()
    matriz = xml_em_matriz_seller_produtos()
    response = cadastrar_no_banco(cursor,matriz)
    finalizar_banco(conexao, cursor)
    


importacoes()