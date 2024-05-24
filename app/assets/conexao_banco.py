import psycopg2
from tkinter import messagebox
def iniciar_banco(usuario,senha,banco):
    try:
        conn1 = psycopg2.connect(
            host="localhost",
            user=usuario,
            password=senha,
            database=banco
        )
        cur1 = conn1.cursor()
        return conn1, cur1
    except:
        messagebox.showerror("Erro", f"Os dados passados de usuário, senha ou banco estão incorretos.")
        return False, False

def finalizar_banco(conexao, cursor):
    conexao.commit()
    cursor.close()
    conexao.close()