from datetime import datetime, timedelta

#1. Obtener la fecha y hora actual
now = datetime.now()
print(f"Fecha y hora actual: {now}")

#2. fecha y hora especifica
fecha_especifica = datetime(2025, 4, 2, 16, 25, 0)
print(f"Fecha y hora especifica: {fecha_especifica}")

#3. formatear fechas
formato = now.strftime('%d/%m/%Y %H:%M:%S')
print(f"Fecha y hora formateada: {formato}")

#4. Operaciones con fechas
yesterday = datetime.now() - timedelta(days=1)
print(f"Ayer: {yesterday}")

tomorrow = datetime.now() + timedelta(hours=1)
print(f"Tomoroow: {tomorrow}")

#5. obtener componentes individuales de una fecha
year = datetime.now().year
print(f"Anio: {year}")

#6.calcular la diferencia entre dos fechas
date1 = datetime.now()
date2 = datetime(2025, 4, 2)
difference = date2 - date1
print(f"Diferencia: {difference}")
print(f"Diferencia days: {difference.days}")

#importar el locale para poner los nombres de las fechas es espaniol
import locale
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
formate_date = now.strftime("%A %B %Y %H:%M:%S")
print(f"fecha formateada al espaniol: {formate_date}")