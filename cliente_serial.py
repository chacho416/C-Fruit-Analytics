import serial
import requests
import time

# Configuración del Nodo IoT
PUERTO_SERIAL = 'COM8' 
BAUD_RATE = 9600
URL_ALERTA = 'http://127.0.0.1:5501/index.html' 

try:
    print(f"Conectando a {PUERTO_SERIAL}...")
    arduino = serial.Serial(PUERTO_SERIAL, BAUD_RATE, timeout=1)
    print("¡Conexión serial con Arduino establecida!")
except Exception as e:
    print(f"Error fatal conectando al Arduino: {e}")
    exit()

print("\n--- Puente Serial IoT ACTIVO ---")
print("Escuchando al sensor infrarrojo... (Presiona Ctrl+C para detener)")

try:
    while True:
        if arduino.in_waiting > 0:
            senal = arduino.readline().decode('utf-8').strip()
            
            # Si el sensor detecta el objeto
            if senal == '1':
                print("\n[!] Sensor activado. Cambiando semáforo a VERDE...")
                try:
                    # Encendemos la alerta en el servidor FastAPI
                    respuesta = requests.post(URL_ALERTA)
                    print(f"Respuesta del servidor: {respuesta.json()}")
                except Exception as e:
                    print(f"Error de red: El servidor FastAPI está apagado: {e}")
                
                # Tiempo de espera para evitar rebotes físicos del sensor
                time.sleep(1.5)
                print("Listo para el siguiente fruto...")

except KeyboardInterrupt:
    print("\nApagando puente serial...")
finally:
    arduino.close()