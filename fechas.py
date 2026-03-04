from datetime import date, timedelta
from validaciones import *

def dias_prestamo():
   fecha_inicio=date.today()
   fecha_limite=fecha_inicio
   dias_prestamo=validarMenu("CUANTOS DIAS SE PRESTARA LA HERRAMIENTA? ",1,15)
   while(dias_prestamo==None):
      dias_prestamo=validarMenu("SOLO SE PUEDE PRESTAR LA HERRAMIENTA POR UN MAXIMO DE 15 DIAS, INTENTELO DE NUEVO: ",1,15)
   print("SU FECHA DE INICIO ES: ",str(fecha_inicio))
   fecha_final_prestamo=fecha_limite+timedelta(days=dias_prestamo)
   print("SU FECHA LIMITE PARA ENTREGAR LA HERRAMIENTA ES DE: ",fecha_final_prestamo)
   return fecha_inicio, fecha_final_prestamo