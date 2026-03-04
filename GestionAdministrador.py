from logs import guardar_log_cantidad
from GestionJSON import *
from validaciones import *
from GestionUsuario import *


ARCHIVO_HERRAMIENTAS = "Administrador.json"

def agregar_herramienta():
    herramientas = cargar(ARCHIVO_HERRAMIENTAS)

    nombre_herramienta = input('Ingrese el nombre de la herramienta: ')
    while not nombre_valido(nombre_herramienta) or existe_herramienta(nombre_herramienta, herramientas):
        nombre_herramienta = input('Ingrese un nombre de herramienta válido: ')

    categoria_herramienta=validarMenu("""
                               Ingrese la categoria de la herramienta:
                                1=Jardineria
                                2=Construccion
                                3=Mecanica
                            """,1, 3)
    guardar_log_cantidad()
    while(categoria_herramienta==None):
            categoria_herramienta=validarMenu("Porfavor ingrese una opcion dentro de los parametros: ",1, 3)
            guardar_log_cantidad()
    if categoria_herramienta==1:
        categoria_herramienta="Jardineria"
    elif categoria_herramienta==2:
        categoria_herramienta="Construccion"
    elif categoria_herramienta==3:
        categoria_herramienta="Mecanica"

    estado_herramienta=validarMenu("""
                               Ingrese el estado de la herramienta:
                                1. ACTIVA 
                                2. REPARACION
                                3. FUERA DE SERVICIO
                            """,1, 3)
    guardar_log_cantidad()
    while(estado_herramienta==None):
                estado_herramienta=validarMenu("Porfavor ingrese una opcion dentro de los parametros: ",1 ,3)
                guardar_log_cantidad()
    if estado_herramienta==1:
                estado_herramienta="ACTIVA"
    elif estado_herramienta==2:
                estado_herramienta="REPARACION"
    elif estado_herramienta==3:
                estado_herramienta="FUERA DE SERVICIO"
  
    stock_herramientaD=validarCero("Ingrese la cantidad de herramientas disponibles: ",0)
    while (stock_herramientaD==None):
        stock_herramientaD=validarCero("Error ingrese un numero entero postivo, cantidad no vailda: ",0)

    valorEstimado=validarDecimalMayor0("Escriba el precio unitario de la herramienta: ",0)
    while (valorEstimado==None):
         valorEstimado=validarDecimalMayor0("Error, Ingrese un numero postivo",0)
    
    nueva_herramienta = {
        "id": generar_id(herramientas),
        "Nombre Herramienta": nombre_herramienta,
        "Categoria": categoria_herramienta,
        "Estado": estado_herramienta,
        "Stock": stock_herramientaD,
        "Valor": valorEstimado
    }
    
    herramientas.append(nueva_herramienta)
    guardar(ARCHIVO_HERRAMIENTAS, herramientas)
    print('HERRAMIENTA AGREGADA!')

def existe_herramienta(nombre_herramienta, herramientas):
    for herramienta in herramientas:
        if herramienta["Nombre Herramienta"].lower() == nombre_herramienta.lower():
            return True
    return False

def listar_herramientas():
    herramientas = cargar(ARCHIVO_HERRAMIENTAS)

    if not herramientas:
        print ("No hay herramientas\n")
        return

    for elemento in herramientas:
        print(f'ID: {elemento["id"]}\n Nombre: {elemento["Nombre Herramienta"]}\n Stock: {elemento["Stock"]}\n Categoria: {elemento["Categoria"]}\n Estado: {elemento["Estado"]}\n Valor Unitario: {elemento["Valor"]}\n')
        print()

def actualizar_herramientas():
    herramientas = cargar(ARCHIVO_HERRAMIENTAS)
    listar_herramientas()
    id_herramientas=validarEntero("Escoja el id a actualizar: ")
    guardar_log_cantidad()
    while(id_herramientas==None):
        id_herramientas=validarEntero("Error, Escoja el id a actualizar: ")
        guardar_log_cantidad()
        

    for elemento in herramientas:
            if id_herramientas==elemento["id"]:
                while(True):
                    updateHerramienta = validarMenu("""
                               Ingrese el parametro que requiere actualizar:
                                1. Nombre
                                2. Categoria
                                3. Estado
                                4. Stock
                                5. Valor
                                6. Volver
                            """,1, 6)
                    guardar_log_cantidad()
                    while updateHerramienta==None:
                        updateHerramienta=validarMenu("Error, Escoja una opcion dentro de los parametros",1,6)
                        guardar_log_cantidad()
                    match(updateHerramienta):
                        case 1:
                            NombreH_Act=input('Ingrese el nombre de la herramienta: ')
                            while not nombre_valido(NombreH_Act) or existe_herramienta(NombreH_Act, herramientas):
                                NombreH_Act=input('Ingrese un nombre valido que no se repita de la herramienta: ')
                            elemento["Nombre Herramienta"]=NombreH_Act
                            guardar(ARCHIVO_HERRAMIENTAS, herramientas)
                            print('herramienta actualizada!')
                            return
                        case 2:
                            categoria_herramienta_act = validarMenu("""
                               Ingrese la categoria de la herramienta:
                                1=Jardineria
                                2=Construccion
                                3=Mecanica
                            """,1,3)
                            guardar_log_cantidad()
                            while(categoria_herramienta_act)==None:
                                categoria_herramienta_act=validarMenu('Error, Ingrese la nueva categoria de la herramienta dentro de los parametros establecidos: ',1,3)
                                guardar_log_cantidad()
                            #LO PONEMOS DESPUES DEL VALIDADOR POR QUE SI NO SE VA A LEER LO QUE PONEMOS
                            if categoria_herramienta_act==1:
                                categoria_herramienta_act="Jardineria"
                            elif categoria_herramienta_act==2:
                                categoria_herramienta_act="Construccion"
                            elif categoria_herramienta_act==3:
                                categoria_herramienta_act="Mecanica"
                            elemento["Categoria"]=categoria_herramienta_act
                            guardar(ARCHIVO_HERRAMIENTAS, herramientas)
                            print('herramienta actualizada!')
                            return
                        case 3:
                            estado_herramienta_act = validarMenu("""
                               Ingrese el nuevo estado de la herramienta:
                                1. ACTIVA
                                2. REPARACION
                                3. FUERA DE SERVICIO
                            """,1, 3)
                            guardar_log_cantidad()
                            while(estado_herramienta_act)==None:
                                estado_herramienta_act=validarMenu('Error, ingrese el nuevo estado de la herramienta: ',1,3)
                                guardar_log_cantidad()
                            if estado_herramienta_act==1:
                                estado_herramienta_act="ACTIVA"
                            elif estado_herramienta_act==2:
                                estado_herramienta_act="REPARACION"
                            elif estado_herramienta_act==3:
                                estado_herramienta_act="FUERA DE SERVICIO"
                            elemento["Estado"]=estado_herramienta_act
                            guardar(ARCHIVO_HERRAMIENTAS, herramientas)
                            print('herramienta actualizada!')
                            return
                        case 4:
                            StockD_Act=validarCero('Ingrese el nuevo stock a sumar de la herramienta: ',0)
                            while (StockD_Act)==None:
                                StockD_Act=validarCero('Error ingrese solo numeros enteros positivos, Ingrese el nuevo stock a sumar de la herramienta: ',0)
                            elemento["Stock"]+=StockD_Act
                            guardar(ARCHIVO_HERRAMIENTAS, herramientas)
                            print('herramienta actualizada!')
                            return
                        case 5:
                            valorEstimado_Act=validarDecimalMayor0('Ingrese el nuevo precio unitario de la herramienta: ',0)
                            while (valorEstimado_Act)==None:
                                 valorEstimado_Act=validarDecimalMayor0('Error ingrese solo numeros postivos: ',0)
                            elemento["Valor"]=valorEstimado_Act
                            guardar(ARCHIVO_HERRAMIENTAS,herramientas)
                            print('Herramienta actualizada!')
                            return
                        case 6:
                              return
    print("La herramienta no existe. \n")


def eliminar_herramienta():
    contador_aux=0
    herramientas=cargar(ARCHIVO_HERRAMIENTAS)
    listar_herramientas()
    id_herramientas=validarEntero("Escoja el id a eliminar")
    guardar_log_cantidad()
    while(id_herramientas==None):
        id_herramientas=validarEntero("Error, Escoja el id a eliminar")
        guardar_log_cantidad()

    for elemento in herramientas:
        if id_herramientas==elemento["id"]:
            herramientas.pop(contador_aux)
            guardar(ARCHIVO_HERRAMIENTAS,herramientas)
            print('Herramienta eliminada!')
            return
        contador_aux+=1
    print("La herramienta no existe. \n")
    guardar_log_cantidad()


