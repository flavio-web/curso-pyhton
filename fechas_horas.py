from datetime import datetime

#1. Obtener la fecha y hora actual
now = datetime.now()
print(f"Fecha y hora actual: {now}")

#2. fecha y hora especifica
fecha_especifica = datetime(2025, 4, 2, 16, 25, 0)
print(f"Fecha y hora especifica: {fecha_especifica}")

#3. formatear fechas
formato = now.strftime('%d/%m/%Y %H:%M:%S')
print(f"Fecha y hora formateada: {formato}")