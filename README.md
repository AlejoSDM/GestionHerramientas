
---
# Sistema de Gestión Comunitaria de Herramientas 🔧

**Versión 2026 — Python + JSON**

Aplicación desarrollada en **Python** que permite gestionar el préstamo de herramientas dentro de una comunidad o barrio. El sistema registra herramientas, usuarios y préstamos, permitiendo llevar un control organizado del inventario y evitando la pérdida o mal uso de herramientas compartidas.

---

# 🔍️ Problemática que resuelve

En muchos barrios existe la costumbre de compartir herramientas entre vecinos para evitar que cada persona tenga que comprarlas todas. Esto permite ahorrar dinero y fomenta la colaboración dentro de la comunidad.

Sin embargo, con el tiempo aparecen varios problemas. Algunas herramientas no se devuelven a tiempo, otras se dañan y no se sabe quién fue el último usuario que las utilizó. Además, al no existir un registro claro, resulta difícil saber cuántas herramientas están disponibles o quién las tiene prestadas.

Para solucionar esta situación, la junta comunal decidió implementar un programa de consola que permita registrar las herramientas, los vecinos y los préstamos realizados. De esta manera, cualquier integrante de la comunidad puede consultar la información sin depender de cuadernos o registros manuales.

El sistema permite mejorar la organización del inventario, controlar los préstamos y mantener un historial de uso de las herramientas dentro de la comunidad.

---

# ✨ Funcionalidades principales

- Registro y gestión de herramientas.
- Registro y administración de usuarios.
- Gestión de préstamos de herramientas.
- Control automático del stock disponible.
- Registro de fechas de préstamo y devolución.
- Consultas y reportes sobre herramientas y usuarios.
- Sistema de **registro de eventos (logs)**.
- Almacenamiento de datos mediante **archivos JSON**.

---

# 🏗️ Estructura del proyecto

El proyecto está organizado en módulos que separan la lógica de cada funcionalidad:


```
main.py # Archivo principal que inicia el programa
menu.py # Menu principal del sistema

GestionAdministrador.py # Gestión de herramientas
GestionUsuario.py # Gestión de usuarios
GestionPrestamos.py # Gestión de préstamos

consultasReport.py # Consultas y reportes
validaciones.py # Validación de datos
fechas.py # Manejo de fechas
logs.py # Registro de eventos
GestionJSON.py # Manejo de archivos JSON

Administrador.json # Datos de herramientas
Usuario.json # Datos de usuarios
Prestamos.json # Datos de préstamos
logs.json # Registro de eventos
```
