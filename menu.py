from validaciones import *
from GestionAdministrador import *
from GestionUsuario import *
from GestionPrestamos import *
from consultasReport import *

def administrador():
    while(True):
        op2=validarMenu("""
                        MENU ADMINISTRADOR
                        1. Gestionar Herramienta
                        2. Gestionar Usuarios
                        3. Gestionar Solicitudes
                        4. Volver    
                    """,1,4)
        while op2==None:
            op2=validarMenu("Error, Escoja una opcion dentro de los parametros",1,4)
        match(op2):
            case 1:
                gestionarherramientas()
            case 2:
                gestionarUsuarios()
            case 3:
                gestion_prestamos_admin()
            case 4:
                return
            case _:
                print("NO SE ENCUENTRA LA OPCION")
        if op2==3:
            break

def gestionarherramientas():
    while(True):
        op3=validarMenu("""
                        GESTION DE HERRAMIENTAS
                        1. Agregar Herramienta
                        2. Eliminar Herramienta
                        3. Actualizar Herramienta
                        4. Mostrar Herramienas
                        5. Volver
                    """,1,5)
        while op3==None:
            op3=validarMenu("Error, Escoja una opcion dentro de los parametros",1,3)
        match(op3):
            case 1:
                print("AGREGAR HERRAMIENTA")
                agregar_herramienta()
            case 2:
                print("ELIMINAR HERRAMIENTA")
                eliminar_herramienta()
            case 3:
                print("ACTUALIZAR HERRAMIENTA")
                actualizar_herramientas()
            case 4:
                print("MOSTRAR HERRAMIENTAS")
                listar_herramientas()
            case 5:
                return
            case _:
                print("NO SE ENCUENTRA LA OPCION")
        if op3==5:
            break

def gestionarUsuarios():
    while(True):
        op4=validarMenu("""
                        GESTION DE USUARIOS
                        1. Agregar Persona
                        2. Eliminar Persona
                        3. Actualizar Persona
                        4. Mostrar Usuarios
                        5. Volver
                    """,1,5)
        while op4==None:
            op4=validarMenu("Error, Escoja una opcion dentro de los parametros",1,3)
        match(op4):
            case 1:
                print("AGREGAR PERSONA")
                agregar_usuario()
            case 2:
                print("ELIMINAR PERSONA")
                eliminar_usuario()
            case 3:
                print("ACTUALIZAR PERSONA")
                actualizar_usuario()
            case 4:
                print("MOSTRAR USUARIOS")
                listar_usuarios()
            case 5:
                return
            case _:
                print("NO SE ENCUENTRA LA OPCION")
        if op4==5:
            break


def menuAgenda():
        while(True):
            op5=validarMenu("""
                            GESTION DE ARRENDAMIENTOS
                            1. AGENDAR
                            2. VOLVER      
                        """,1,2)
            while op5==None:
                op5=validarMenu("Error, Escoja una opcion dentro de los parametros",1,2)
            match(op5):
                case 1:
                    agendaherramientas()
                case 2:
                    return
                case _:
                    print("NO SE ENCUENTRA LA OPCION")
            if op5==2:
                break

def ConsultasReportes():
        while(True):
            op6=validarMenu("""
                            CONSULTAS Y REPORTES
                            1. STOCK BAJO!!
                            2. VER ARRENDAMIENTOS
                            3. VER HERRAMIENTAS MAS DEMANDADAS
                            4. DEVOLVER HERRAMIENTA
                            5. VOLVER      
                        """,1,5)
            while op6==None:
                op6=validarMenu("Error, Escoja una opcion dentro de los parametros",1,5)
            match(op6):
                case 1:
                    mostrarStockBajo()
                case 2:
                    mostrarPrestamos()
                case 3:
                    demandaAlta()
                case 4:
                    devolver_prestamo()
                case 5:
                    return
                case _:
                    print("NO SE ENCUENTRA LA OPCION")
            if op6==5:
                break


def menu():
    while(True):
        op=validarMenu("""
                        GESTION DE HERRAMIENTAS PARA EL BARRIO
                        1. Administrador
                        2. Agendar Herramienta
                        3. Consultas y Reportes
                        4. Salir      
                    """,1,4)
        while op==None:
            op=validarMenu("Error, Escoja una opcion dentro de los parametros",1,4)
        match(op):
            case 1:
                clave=1234
                ingreso=int(input("INGRESE LA CLAVE DE ADMINISTRADOR: "))
                while ingreso!=clave:
                    ingreso=int(input("CLAVE INCORRECTA, INTENTE NUEVAMENTE: "))
                print("CLAVE CORRECTA, BIENVENIDO ADMINISTRADOR")
                administrador()
            case 2:
                menuAgenda()
            case 3:
                ConsultasReportes()
            case 4:
                print("GRACIAS POR USAR NUESTRO SERVICIO")
            case _:
                print("OPCION NO VALIDA")
        if op==4:
            break
            