from GestionPrestamos import *
from GestionUsuario import *
from GestionAdministrador import *
from GestionJSON import *
from fechas import *
from validaciones import *

ARCHIVO_HERRAMIENTAS = "Administrador.json"
ARCHIVO_USUARIO = "Usuario.json"
ARCHIVO_PRESTAMO = "Prestamos.json"
ARCHIVO_CONSULTAS_REPORTES ="consultasReportes.json"

def mostrarPrestamos():
    prestamos = cargar(ARCHIVO_PRESTAMO)

    if not prestamos:
        print ("No hay prestamos\n")
        return

    for elemento in prestamos:
        print(f'ID: {elemento["id_prestamo"]}\n Nombre: {elemento["nombre_usuario"]}\n Apellido: {elemento["apellido_usuario"]}\n ID HERRAMIENTA: {elemento["id_herramienta"]}\n Nombre Herramienta: {elemento["nombre_herramienta"]}\n CANTIDAD SELECCIONADA: {elemento["cantidad tomada"]}\n Fecha inicio: {elemento["Fecha inicio"]}\n FECHA LIMITE DE ENTREGA: {elemento["Fecha de entrega"]}\n Estado de la solicitud: {elemento["Estado solicitud"]}\n')
    print()

def mostrarStockBajo():
    herramientas = cargar(ARCHIVO_HERRAMIENTAS)
    encontro_stock_bajo = False
    
    for elemento in herramientas:
        if elemento["Stock"]<=3 and elemento["Stock"]>=1:
            encontro_stock_bajo=True
            if encontro_stock_bajo==True :
                print("STOCK BAJO:")
                print(f'ID: {elemento["id"]}\n Nombre: {elemento["Nombre Herramienta"]}\n Stock: {elemento["Stock"]}\n Categoria: {elemento["Categoria"]}\n Estado: {elemento["Estado"]}\n Valor Unitario: {elemento["Valor"]}\n')
                print()   

def herramientasSolicitadas(id_herramienta):
    contador_aux=0
    prestamos=cargar(ARCHIVO_PRESTAMO)

    for elemento in prestamos:
        if id_herramienta==elemento["id_herramienta"]:
            contador_aux+=1
    return contador_aux

def contarTodaslasHerramientas():
    herramientas=cargar(ARCHIVO_HERRAMIENTAS)
    resultado=[]
    for elemento in herramientas:
        print(f'{elemento["Nombre Herramienta"]}->{herramientasSolicitadas(elemento["id"])}')
        resultado.append({"Nombre Herramienta": elemento["Nombre Herramienta"], "Cantidad": herramientasSolicitadas(elemento["id"])})
    return resultado

def demandaAlta():
    resultados=contarTodaslasHerramientas()
    print("**************************")
    print("FILTRANDO LA DEMANDA ALTA")
    if not resultados:
        print("NO HAY DATOS")
    else:
        for elemento in resultados:
            if elemento["Cantidad"]>=5:
                print(f'{elemento["Nombre Herramienta"]} -> {elemento["Cantidad"]}')       