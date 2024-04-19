import psycopg2
import pandas as pd
from funcoes import delimitador_automatico
from funcoes import delimitador_manual
from grupos_autosystem import pegar_grupos

# Conexão com o primeiro banco de dados
conn1 = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="postgres",
    database="flora_loja"
)

cur1 = conn1.cursor()

cur1.execute("DELETE FROM produto;")

dados = pd.read_csv('produtos.csv',sep=';')
tabela = dados.values




grupos = pegar_grupos()
lista_codigos_string = list(grupos.keys())
print('Escolha:')
print('1 - Inserir manualmente')
print('2 - Inserir por bloco')
# menu = int(input('Resposta:'))
menu = 2
match menu:
    case 1:
        listagem = delimitador_manual(lista=lista_codigos_string,tabela=tabela)
    case 2:
        listagem = delimitador_automatico(lista=lista_codigos_string,tabela=tabela)

print(listagem)

dicionario_codigos = pegar_grupos()

        
id = 1
contador_verificado = 0
for produto in tabela:
    contador_verificado += 1
    # print(produto[2])
    codigo = id
    codigo_barra = produto[2]
    nome = produto[3]
    if 'Ç' in nome:
        nome = nome.replace('Ç', 'C')
    if 'Ã' in nome:
        nome = nome.replace('Ã', 'A')
    if 'Õ' in nome:
        nome = nome.replace('Õ', 'O')
    # if 'Ç' in nome or 'Ã' in nome or 'Õ' in nome:
    #     continue
    for i in range(len(listagem)):
        if produto[5] in listagem[lista_codigos_string[i]]:
            grupo = dicionario_codigos[lista_codigos_string[i]]
            print(nome)
            # cur1.execute(f'''INSERT INTO produto(codigo,codigo_barra,nome,grupo) VALUES('{id}','{codigo_barra}', '{nome}','{grupo}');''')
            cur1.execute("INSERT INTO produto(codigo,codigo_barra,nome,grupo) VALUES(%s, %s, %s, %s);", (id, codigo_barra, nome, grupo))
            id = int(id)
            print(f'Produto {id} OK!')
            break
    id += 1
print(f'Produtos totais: {contador_verificado}')    

cur1.execute("SELECT * FROM produto;")
result1 = cur1.fetchall()
print(f'Produtos adicionados: {len(result1)}')    

conn1.commit()
cur1.close()
conn1.close()

