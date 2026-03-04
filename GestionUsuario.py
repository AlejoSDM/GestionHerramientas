from GestionJSON import *
from GestionAdministrador import *
from validaciones import *
from logs import *


ARCHIVO_USUARIO = "Usuario.json"

def agregar_usuario():
    usuarios = cargar(ARCHIVO_USUARIO)

    nombre_usuario = input('Ingrese el nombre de el usuario: ')
    while not nombre_valido(nombre_usuario) or existe_nombre(nombre_usuario, usuarios):
        nombre_usuario = input('Ingrese un nombre de usuario válido: ')
    
    Apellido = input('Ingrese el apellido de el usuario: ')
    while not nombre_valido(Apellido):
        Apellido = input('Ingrese un nombres de usuario válido: ')

    Telefono = validarCero('Ingrese el telefono de el usuario: ',0)
    guardar_log_cantidad
    while(Telefono==None):
        Telefono=validarCero("Error no ingrese numeros negativos ni simbolos, Ingrese el nuevo numero de tefono: ",0)
        guardar_log_cantidad

    Direccion = input('Ingrese la direccion de el usuario: ')
    

    nuevo_usuario = {
        "id": generar_id(usuarios),
        "Nombre usuario": nombre_usuario,
        "Apellido": Apellido,
        "Telefono": Telefono,
        "Direccion": Direccion,
    }

    
    usuarios.append(nuevo_usuario)
    guardar(ARCHIVO_USUARIO, usuarios)
    print('USUARIO AGREGADO!')

def existe_nombre(nombreU, usuarios):
    for elemento in usuarios:
        if elemento["Nombre usuario"].lower() == nombreU.lower():
            return True
    return False

def listar_usuarios():
    usuarios = cargar(ARCHIVO_USUARIO)

    if not usuarios:
        print ("No hay usuarios\n")
        return

    for elemento in usuarios:
        print(f'ID: {elemento["id"]}\n Nombre: {elemento["Nombre usuario"]}\n Apellido: {elemento["Apellido"]}\n Telefono: {elemento["Telefono"]}\n Direccion: {elemento["Direccion"]}\n')
    print()

def listar_nombres():
    usuarios = cargar(ARCHIVO_USUARIO)

    if not usuarios:
        print ("No hay nombres\n")
        return

    for elemento in usuarios:
        print(f'ID: {elemento["id"]}\n Nombre: {elemento["Nombre usuario"]}\n Apellido: {elemento["Apellido"]}\n')
    print()


def actualizar_usuario():
    usuarios = cargar(ARCHIVO_USUARIO)
    listar_usuarios()
    id_usuarios=validarEntero("Escoja el id a actualizar: ")
    while(id_usuarios==None):
        id_usuarios=validarEntero("Error, Escoja el id a actualizar: ")
        

    for elemento in usuarios:
            if id_usuarios==elemento["id"]:
                while(True):
                    updateUsuario = validarMenu("""
                               Ingrese el parametro que requiere actualizar:
                                1. Nombre
                                2. Apellido
                                3. Telefono
                                4. Direccion
                            """,1, 4)
                    
                    match(updateUsuario):
                        case 1:
                            NombreU_Act=input('Ingrese el nuevo nombre de el usuario: ')
                            while not nombre_valido(NombreU_Act) or existe_nombre(NombreU_Act, usuarios):
                                NombreU_Act = input('Ingrese un nombre de usuario válido, no repetido: ')
                            elemento["Nombre usuario"]=NombreU_Act
                            guardar(ARCHIVO_USUARIO, usuarios)
                            print('Usuario actualizado!')
                            return
                        case 2:
                            Apellido_Act=input('Ingrese el nuevo apellido de el usuario: ')
                            elemento["Apellido"]=Apellido_Act
                            guardar(ARCHIVO_USUARIO, usuarios)
                            print('Usuario actualizado!')
                            return
                        case 3:
                            Telefono_Act=validarCero('Ingrese el nuevo telefono de el usuario: ',0)
                            guardar_log_cantidad()
                            while (Telefono_Act)==None:
                                Telefono_Act=validarCero("Error no ingrese numeros negativos ni simbolos, Ingrese el nuevo numero de tefono: ",0)
                                guardar_log_cantidad()
                            elemento["Telefono"]=Telefono_Act
                            guardar(ARCHIVO_USUARIO, usuarios)
                            print('Usuario actualizado!')
                            return
                        case 4:
                            Direccion_Act=input('Ingrese la nueva direccion de el usuario: ')
                            elemento["Direccion"]=Direccion_Act
                            guardar(ARCHIVO_USUARIO, usuarios)
                            print('Usuario actualizado!')
                            return
    print("El usuario no existe. \n")


def eliminar_usuario():
    contador_aux=0
    usuarios=cargar(ARCHIVO_USUARIO)
    listar_usuarios()
    id_usuarios=validarEntero("Escoja el id a eliminar")
    guardar_log_cantidad()
    while(id_usuarios==None):
        id_usuarios=validarEntero("Error, Escoja el id a eliminar")
        guardar_log_cantidad
    for elemento in usuarios:
        if id_usuarios==elemento["id"]:
            usuarios.pop(contador_aux)
            guardar(ARCHIVO_USUARIO,usuarios)
            print('Usuario eliminado!')
            return
        contador_aux+=1
    print("El usuario no existe. \n")
    guardar_log_cantidad()
