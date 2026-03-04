def validarCero(mesanje, minimo):
    try:
        dato=int(input(mesanje))
        if dato<=minimo:
            return None
        else:
            return dato
    except:
        return None
    
def validarDecimalMayor0(mesanje, minimo):
    try:
        dato=float(input(mesanje))
        if dato<=minimo:
            return None
        else:
            return dato
    except:
        return None
    

def validarEntero(mensaje):
    try:
        return int(input(mensaje))
    except:
        return None

def validarMenu(mensaje, minimo, maximo):
    try:
        dato=int(input(mensaje))
        if dato<minimo or dato>maximo:
            return None
        else:
            return dato
    except:
        return None

def nombre_valido(nombre):
    # ' David Dominguez '.strip()= 'David Dominguez'
    # '  '
    if nombre.strip().lower()=="":
        print("Nombre vacio")
        return False
    return True


def validar_herramienta(herramienta):
    if herramienta.strip()=="":
        print("herramienta vacia")
        return False
    return True

def validarFecha(mensaje, minimo, maximo):
    try:
        dato=int(input(mensaje))
        if dato<minimo or dato>maximo:
            return None
        else:
            return dato
    except:
        return None