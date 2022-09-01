from datetime import datetime
import pytz

bogota_timezome = pytz.timezone('America/Bogota')
bogota_date = datetime.now(bogota_timezome)
print("Bogotá: ",bogota_date.strftime("%d/%m/%Y,%H:%M:%S"))

mexico_timezome = pytz.timezone('America/Mexico_City')
mexico_date = datetime.now(mexico_timezome)
print("Ciudad de México: ",mexico_date.strftime("%d/%m/%Y,%H:%M:%S"))