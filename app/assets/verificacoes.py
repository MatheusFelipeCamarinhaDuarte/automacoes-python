def verifica_nulos(*args):
    for i, arg in enumerate(args):
        if (arg == 0 or arg == None):
            return False
    return True