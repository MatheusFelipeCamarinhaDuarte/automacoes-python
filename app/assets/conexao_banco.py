import psycopg2
def iniciar_banco(usuario,senha,banco):
    while True:
        try:
            conn1 = psycopg2.connect(
                host="localhost",
                user=usuario,
                password=senha,
                database=banco
            )
            cur1 = conn1.cursor()
            break
        except:
            return False, False
    return conn1, cur1

def finalizar_banco(conexao, cursor):
    conexao.commit()
    cursor.close()
    conexao.close()