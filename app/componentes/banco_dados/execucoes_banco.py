import csv


def definir_id_com_exclusao(substituir, cursor):
    id = 1
    if substituir:
        cursor.execute("DELETE FROM produto")
    else:
        cursor.execute("SELECT * FROM produto")
        result1 = cursor.fetchall()
        maior_numero = 0
        for i in result1:
            numero = int(i[0])
            if numero >= maior_numero:
                maior_numero = numero
        id = maior_numero + 1
    return id






def inserir_grupos_as(dicionario:dict, cursor):
    
    cursor.execute(f"DELETE FROM grupo_produto")
    cursor.execute(f"DELETE FROM subgrupo_produto")
    id = 1
    id_sub = 1
    grupo_com_grid = {} 
    subgrupo_com_grid = {}
    for grupo, subgrupos in dicionario.items():
        cursor.execute("INSERT INTO grupo_produto (codigo,nome,flag) VALUES (%s,%s,%s);", (id,grupo,'A'))
        cursor.execute("SELECT * FROM grupo_produto WHERE codigo = %s;", (id,))
        result1 = cursor.fetchall()
        grid_grupo = result1[0][3]
        grupo_com_grid[grupo] = grid_grupo
        for subgrupo in subgrupos:
            cursor.execute("INSERT INTO subgrupo_produto (codigo,nome,grupo,flag) VALUES (%s,%s,%s,%s);", (id_sub,subgrupo,grid_grupo,'A'))
            cursor.execute("SELECT * FROM subgrupo_produto WHERE codigo = %s;",(id_sub,))
            result1 = cursor.fetchall()
            grid_subgrupo = result1[0][4]
            subgrupo_com_grid[subgrupo] = grid_subgrupo
            id_sub += 1
        id += 1        
    return grupo_com_grid, subgrupo_com_grid

# matriz = [
#     ["001", "nome produto 1", "6", "nome produto"],
#     ["002", "nome produto 2", "6", "proco produto"],
#     ["003", "nome produto 3", "9", "produto KIT"],
#     ["004", "nome produto 4", "9", "codigo produto"],
# ]

# relatorio_erros(matriz)
