def verifica_nulos(*args):
    # Pra cada
    for i, arg in enumerate(args):
        if (arg == None):
            return False
    return True
def verifica_zeros(*args:int):
    for i, arg in enumerate(args):
        if (arg == 0):
            return False
    return True
def verifica_vazios(*args:str):
    for i, arg in enumerate(args):
        if (arg == ""):
            return False
    return True
def verifica_outros(identificador,*args):
    for i, arg in enumerate(args):
        if (arg == identificador):
            return False
    return True