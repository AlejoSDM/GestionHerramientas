from validaciones import *
from GestionUsuario import *
from GestionAdministrador import *
from fechas import *

ARCHIVO_HERRAMIENTAS = "Administrador.json"
ARCHIVO_USUARIO = "Usuario.json"
ARCHIVO_PRESTAMO = "Prestamos.json"

def agendaherramientas():
    # ESTA PARTE DE ACA ME VA A CARGAR LOS USUARIOS Y ME VA A PEDIR QUE INGRESE EL ID
    usuarios = cargar(ARCHIVO_USUARIO)
    listar_nombres()
    ID_usuario = validarCero("INGRESE SU ID: ",0)
    guardar_log_cantidad()
    while ID_usuario==None:
        ID_usuario = validarCero("ID INVALIDO, INTENTE NUEVAMENTE: ",0)
        guardar_log_cantidad()
    # ESTA PARTE BUSCA AL USUARIO
    Usuario_Seleccionado = None
    for elementos in usuarios:
        if elementos["id"] == ID_usuario:
            Usuario_Seleccionado = elementos
            break

    if Usuario_Seleccionado==None:
        print("Usuario no encontrado.")
        return

    print("BIENVENIDO", Usuario_Seleccionado["Nombre usuario"], 
          "A CONTINUACION SE LE MOSTRARA EL CATALOGO DE HERRAMIENTAS DISPONIBLES")

    # MUESTRA Y CARGA LAS HERRAMIENTAS
    listar_herramientas()
    herramientas = cargar(ARCHIVO_HERRAMIENTAS)

    # PIDE EL ID DE LA HERRAMIENTA
    ID_herramienta = validarEntero("Ingrese el ID de la herramienta que desea: ")
    herramienta_seleccionada = None
    for elemento in herramientas:
        if elemento["id"] == ID_herramienta:
            herramienta_seleccionada = elemento
            break

    

    if herramienta_seleccionada:
        cantidad_arrendada=validarCero("INGRESE LA CANTIDAD QUE DESEA ARRENDAR: ",0)
        while(cantidad_arrendada>herramienta_seleccionada["Stock"]):
            cantidad_arrendada=validarCero("NO PUEDE ARRENDAR MAS DE EL STOCK DISPONIBLE, Intente de nuevo: ",0)
        guardar(ARCHIVO_HERRAMIENTAS, herramientas)
        print("Has escogido la herramienta:", herramienta_seleccionada["Nombre Herramienta"])
        fecha_inicio, fecha_final_prestamo = dias_prestamo()
        observaciones=("PORFAVOR USAR SIGUIENDO EL MANUAL")
        prestamos = cargar(ARCHIVO_PRESTAMO)
        nuevo_prestamo = { 
            "id_prestamo": generar_id_prestamos(prestamos), 
            "id_usuario": Usuario_Seleccionado["id"],
            "nombre_usuario": Usuario_Seleccionado["Nombre usuario"],
            "apellido_usuario": Usuario_Seleccionado["Apellido"],
            "id_herramienta": herramienta_seleccionada["id"],
            "nombre_herramienta": herramienta_seleccionada["Nombre Herramienta"], 
            "estado_herramienta": herramienta_seleccionada["Estado"],
            "cantidad tomada": cantidad_arrendada,
            "Fecha inicio": str(fecha_inicio),
            "Fecha de entrega": str(fecha_final_prestamo),
            "Observaciones": observaciones,
            "Estado solicitud":"pendiente"
        }
        prestamos.append(nuevo_prestamo) 
        guardar(ARCHIVO_PRESTAMO, prestamos)
    else:
        print("No existe una herramienta con ese ID.")

def mostrarPrestamos():
    prestamos = cargar(ARCHIVO_PRESTAMO)

    if not prestamos:
        print ("No hay prestamos\n")
        return

    for elemento in prestamos:
        print(f'ID: {elemento["id_prestamo"]}\n Nombre: {elemento["nombre_usuario"]}\n Apellido: {elemento["apellido_usuario"]}\n ID HERRAMIENTA: {elemento["id_herramienta"]}\n Nombre Herramienta: {elemento["nombre_herramienta"]}\n CANTIDAD SELECCIONADA: {elemento["cantidad tomada"]}\n Fecha inicio: {elemento["Fecha inicio"]}\n FECHA LIMITE DE ENTREGA: {elemento["Fecha de entrega"]}\n Observaciones: {elemento["Observaciones"]}\n Estado Solicitud: {elemento["Estado solicitud"]}\n')
        print()

def gestion_prestamos_admin():
    prestamos=cargar(ARCHIVO_PRESTAMO)
    herramientas=cargar(ARCHIVO_HERRAMIENTAS)

    Solicitudes_pendientes=[]

    for elemento in prestamos:
        if elemento["Estado solicitud"]=="pendiente":
            Solicitudes_pendientes.append(elemento)

    if not Solicitudes_pendientes:
        print('No hay prestamos pendientes.')
        return
    
    print("---PRESTAMOS PENDIENTES---")
    for nuevo_prestamo in Solicitudes_pendientes:
        print(f'''
            ID: {nuevo_prestamo["id_prestamo"]} 
            Nombre: {nuevo_prestamo["nombre_usuario"]}
            Apellido: {nuevo_prestamo["apellido_usuario"]}
            Herramienta: {nuevo_prestamo["nombre_herramienta"]}
            Cantidad: {nuevo_prestamo["cantidad tomada"]}
            Fecha fin: {nuevo_prestamo["Fecha de entrega"]}
            Estado: {nuevo_prestamo["Estado solicitud"]}       
            ''')
        
    id_solicitado=validarEntero('Ingrese el ID del prestamo a gestionar: ')
    while id_solicitado==None:
        id_solicitado=validarEntero('Error, intentelo nuevamente: ')

    for nuevo_prestamo in Solicitudes_pendientes:
        if nuevo_prestamo["id_prestamo"]==id_solicitado and nuevo_prestamo["Estado solicitud"]=="pendiente":
            op=validarMenu('''  
                    Porfavor esoja una opcion para el prestamo
                    1.  Aprobar prestamo
                    2.  Rechazar prestamo
                        ''',1,2)
            if op==1:
                for elemento in herramientas:
                    if elemento["id"]==nuevo_prestamo["id_herramienta"]:
                        if elemento["Estado"]=="REPARACION":
                            print("La herramienta esta en reparacion, no se puede aprobar")
                            return
                        elif elemento["Stock"]<nuevo_prestamo["cantidad tomada"]:
                            print("No hay stock suficiente")
                            return
                        elif elemento["Estado"]=="FUERA DE SERVICIO":
                            print("La herramienta esta fuera de servicio, no se puede aprobar")
                            return
                            
                        elemento["Stock"]-=nuevo_prestamo["cantidad tomada"]
                        nuevo_prestamo["Estado solicitud"]="activo"
                        print("Prestamo aprobado con exito!")
                        break
            elif op==2:
                nuevo_prestamo["Estado solicitud"]="rechazado"
                print("Prestamo rechazado")

            guardar(ARCHIVO_PRESTAMO, prestamos)
            guardar(ARCHIVO_HERRAMIENTAS, herramientas)
            return
    print("Prestamo no encontrado.")

                            
def devolver_prestamo():
    prestamos=cargar(ARCHIVO_PRESTAMO)
    herramientas=cargar(ARCHIVO_HERRAMIENTAS)
    usuarios=cargar(ARCHIVO_USUARIO)
    
    prestamos_activos=[]

    for prestamo in prestamos:
        if prestamo["Estado solicitud"]=="activo":
            prestamos_activos.append(prestamo)
    
    if not prestamos_activos:
        print("No hay prestamos activos para devolver.")
        return
    
    print("Prestamos activos: ")
    for prestamo in prestamos_activos:

        nombre_usuario= "Desconocido"
        nombre_herramienta="Desconocida"

        for usuario in usuarios:
            if usuario["id"]==prestamo["id_usuario"]:
                nombre_usuario = usuario["Nombre usuario"]
                break

        for herramienta in herramientas:
            if herramienta["id"]==prestamo["id_herramienta"]:
                nombre_herramienta = herramienta["Nombre Herramienta"]
                break

        print(f''' 
                =============================================== 
                ID: {prestamo["id_prestamo"]}
                Usuario: {nombre_usuario} ID: {prestamo["id_usuario"]}
                Herramienta: {nombre_herramienta} ID: {prestamo["id_herramienta"]}
                Cantidad: {prestamo["cantidad tomada"]}
                ===============================================
                ''')

    id_prestamo=validarEntero('Ingrese el ID del prestamo a devolver: ')
    while id_prestamo==None:
        id_prestamo=validarEntero('Error, intentelo nuevamente: ')

    for prestamo in prestamos_activos:
        if prestamo["id_prestamo"]== id_prestamo:
            
            print(f'Cantidad prestada: {prestamo["cantidad tomada"]}')
            cantidad_devuelta=validarEntero('Ingrese la cantidad de herramientas que va a devolver: ')
            while cantidad_devuelta is None or cantidad_devuelta <=0 or cantidad_devuelta>prestamo["cantidad tomada"]:
                cantidad_devuelta=validarEntero(f"Error, ingrese un numero valido (max {prestamo['cantidad tomada']}): ")

            estado_entregado=validarMenu('''
                        Ingrese el estado en el que devuelve la herramienta
                        1.  Buen estado
                        2.  Mal estado
                        ''',1,2)
            for herramienta in herramientas:
                if herramienta["id"]==prestamo["id_herramienta"]:

                    if estado_entregado==1:
                        herramienta["Estado"]="buen estado"
                        herramienta["Stock"]+= cantidad_devuelta
                    if estado_entregado==2:
                        herramienta["Estado"]="mal estado"
                        herramienta["Stock"]+=cantidad_devuelta
                    break
            prestamo["cantidad tomada"]-=cantidad_devuelta
            if prestamo["cantidad tomada"]==0:
                prestamo["estado"]="devuelto"

            guardar(ARCHIVO_PRESTAMO, prestamos)
            guardar(ARCHIVO_HERRAMIENTAS, herramientas)

            print(f'Prestamo actualizado correctamente. Cantidad restante: {prestamo["cantidad tomada"]}')
            return
    print('Prestamo no encontrado o ya devuelto.')