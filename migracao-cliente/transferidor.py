import psycopg2

import pandas as pd

# Conexão com o primeiro banco de dados
conn1 = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="postgres",
    database="flora_pista"
)

cur1 = conn1.cursor()



file_path = r'c:\Users\User\python\clientes.csv'

if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
    dados = pd.read_csv(file_path, sep=';')
else:
    print("The file is empty or does not exist.")
dados.fillna("",inplace=True)
tabela = dados.values

cur1.execute("DELETE FROM cliente;")
        
id = 20
contador_verificado = 0
for cliente in tabela:
    contador_verificado += 1
    codigo = id
    nome = cliente[0]
    nome = nome.replace("'","")
    # print(nome)
    if 'Ç' in nome:
        nome = nome.replace('Ç', 'C')
    if 'Ã' in nome:
        nome = nome.replace('Ã', 'A')
    if 'Õ' in nome:
        nome = nome.replace('Õ', 'O')
    if 'É' in nome:
        nome = nome.replace('É', 'E')
    if 'Á' in nome:
        nome = nome.replace('Á', 'A')
    if 'À' in nome:
        nome = nome.replace('À', 'A')
    logradouro = cliente[1]    
    numero = cliente[2]    
    complemento = cliente[3]    
    endereco = str(logradouro) +", "+ str(numero)+ " - " + str(complemento)
    bairro = cliente[4]    
    cidade = cliente[5]
    cep = cliente[6]
    uf = cliente[7]    
    cpf = cliente[8]
    if '/' in cpf:
        pessoa = 'J'
    else:
        pessoa = 'F'    
    telefone = cliente[9]    
    fax = cliente[10]    
    celular = cliente[11]    
    email = cliente[12]    
    rg = cliente[13]    
    inscricao = cliente[14]    
    # 12098 = Quinzenal | 110 = Cliente | 
    grupo = 12098

    cur1.execute("INSERT INTO cliente(codigo,nome, logradouro, numero, complemento, bairro, cidade, cep, uf, cpf,fone,fax,celular,email,rg,inscr_est, endereco, grupo,tipo_pessoa) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", (id, nome,logradouro, numero, complemento, bairro, cidade, cep, uf, cpf, telefone, fax, celular, email, rg, inscricao, endereco,grupo, pessoa))
    print(f'cliente {id} OK!')
    id += 1
    # try:
    #    cur1.execute("INSERT INTO cliente(codigo,nome, logradouro, numero, complemento, bairro, cidade, cep, uf, cpf,fone,fax,celular,email,rg,inscr_est, endereco) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", (id, nome,logradouro, numero, complemento, bairro, cidade, cep, uf, cpf, telefone, fax, celular, email, rg, inscricao, endereco))
    # except:
    #     print("ERRO AO CADASTRAR")
    # finally:
    #     print(f'cliente {id} OK!')
    #     id += 1

cur1.execute("SELECT * FROM cliente;")
result1 = cur1.fetchall()
# print(result1)
print(f'clientes adicionados: {len(result1)}')    
print(f'clientes totais: {contador_verificado}')    

conn1.commit()
cur1.close()
conn1.close()

