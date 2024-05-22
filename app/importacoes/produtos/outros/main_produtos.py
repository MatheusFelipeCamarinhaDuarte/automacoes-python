from app.assets.conexao_banco import iniciar_banco,finalizar_banco
from funcoes.funcoes_banco import cadastrar_no_banco
from funcoes.funcoes_interacao import escolha_importacao_dados, escolha_demilitador
from funcoes.funcoes_pegar_grupo import pegar_grupos


def transferidor_produtos():
    print("Bem vindo ao tranferidor de arquivos de produto.")
    conexao, cursor = iniciar_banco(intencao="inserir")
    tabela = escolha_importacao_dados()
    lista_grupos = pegar_grupos()
    lista_keys_grupo = list(lista_grupos.keys())
    listagem = escolha_demilitador(lista_keys_grupo,tabela)

    cadastrar_no_banco(cursor,tabela,listagem,lista_keys_grupo,lista_grupos)

    finalizar_banco(conexao,cursor)

if __name__ == "__main__":
    print("O script está sendo executado diretamente do repositório.")
    transferidor_produtos()