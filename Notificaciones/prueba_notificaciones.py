from notifypy import Notify
import time
from datetime import datetime

# Función para calcular los segundos hasta una hora específica
def time_until(target_time):
    current_time = datetime.now()
    delta = target_time - current_time
    return delta.total_seconds()

# Crear una instancia de Notify
notification = Notify()

# Configurar el título y el mensaje
notification.title = "Notificación Programada"
notification.message = "¡Es hora de la notificación!"

# Definir la fecha y hora a la que quieres que se envíe la notificación
# Por ejemplo, el 10 de abril de 2025 a las 15:30
target_time = datetime(2025, 4, 10, 14, 17)

# Calcular cuántos segundos quedan hasta esa hora
seconds_until_notification = time_until(target_time)

# Esperar hasta el momento de la notificación      34  
print(f"Esperando {seconds_until_notification} segundos...")
time.sleep(seconds_until_notification)
# Enviar la notificación
notification.send()
print("Notificación enviada.")

