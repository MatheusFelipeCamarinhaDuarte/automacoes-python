import psycopg2

conn1 = psycopg2.connect(
    host="localhost",
    user='postgres',
    password='postgres',
    database='flora_loja'
)
cur1 = conn1.cursor()
cur1.execute("SELECT * FROM produto")
result1 = cur1.fetchall()
maior_numero = 0
for i in result1:
    numero = int(i[0])
    if numero >= maior_numero:
        maior_numero = numero
print(f'Produtos adicionados: {len(result1)}')
print(maior_numero)