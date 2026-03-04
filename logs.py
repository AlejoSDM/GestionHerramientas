from datetime import date
from GestionJSON import cargar, guardar, generar_id

ARCHIVO_LOG = "logs.json"

def guardar_log_cantidad():
    logs = cargar(ARCHIVO_LOG)

    nuevo_log = {
        "id": generar_id(logs),
        "fecha": date.today().strftime("%Y-%m-%d"),
        "descripcion": "Se digito un valor no disponible"
    }

    logs.append(nuevo_log)
    guardar(ARCHIVO_LOG, logs)


