# 🥑 Chachos Software: Estación AIoT de Clasificación Agrícola

Sistema de control de calidad automatizado mediante Inteligencia Artificial de las Cosas (AIoT). Este proyecto integra visión computacional con hardware físico para detectar el estado de salud de frutos en tiempo real sobre una línea de producción.

## 🚀 Arquitectura del Sistema

El proyecto opera bajo una arquitectura de *Edge Computing* (Procesamiento en el Borde) compuesta por tres capas principales:

1. **El Cerebro (IA & Backend):** Servidor local desarrollado en **FastAPI** ejecutando un modelo de red neuronal **YOLOv8** entrenado a medida (`best.pt`) para clasificación de imágenes.
2. **El Gatillo (Hardware):** Placa **Arduino** conectada por puerto serial, equipada con un sensor infrarrojo que detecta el paso físico del fruto y envía la orden de escaneo.
3. **El Monitor (Frontend):** Interfaz web dinámica (HTML/JS) accesible desde cualquier dispositivo en la misma red local (LAN) para monitoreo de la producción en tiempo real.

## 🛠️ Tecnologías Utilizadas

* **Python 3.10+**
* **FastAPI & Uvicorn** (Servidor API REST)
* **Ultralytics (YOLOv8)** (Visión Computacional)
* **OpenCV** (Procesamiento de imágenes)
* **PySerial** (Puente de comunicación hardware-software)
* **Arduino C++** (Lógica de sensores)
* **HTML5, CSS3, Vanilla JavaScript** (Panel de control)

## 🔌 Requisitos de Hardware

* Computadora host (Edge Server) con Windows/Linux.
* Cámara Web (Resolución mínima 720p recomendada).
* Placa Arduino (Uno/Nano/Mega).
* Sensor Infrarrojo (TCRT5000 u obstáculo genérico).
* Conexión USB habilitada (`COM8` por defecto, configurable).

## ⚙️ Instalación y Configuración

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/tu-usuario/C-Fruit-Analytics.git](https://github.com/tu-usuario/C-Fruit-Analytics.git)
   cd C-Fruit-Analytics

```

2. **Instalar dependencias de Python:**
```bash
pip install fastapi uvicorn ultralytics opencv-python pyserial requests

```


3. **Configuración de Red (Opcional):**
Para acceder al panel desde otros dispositivos, asegúrate de que el servidor se levante apuntando al host `0.0.0.0` y actualiza la variable `URL_SERVIDOR` en tu `index.html` con la IP IPv4 de tu computadora host.

## 🎬 Uso del Sistema (Arranque Automático)

Para ambientes Windows, el sistema cuenta con un script de despliegue rápido:

1. Conecta la placa Arduino al puerto USB.
2. Asegúrate de tener la cámara despejada y bien iluminada.
3. Ejecuta el archivo `iniciar_sistema.bat` con doble clic.
4. Abre la interfaz web o ingresa desde cualquier dispositivo móvil conectado al mismo WiFi mediante la IP local en el puerto `8000`.
5. Pasa un objeto por el sensor físico; el sistema capturará, procesará y graficará el resultado automáticamente.

## 📂 Estructura del Proyecto

```text
📦 C-Fruit-Analytics
 ┣ 📜 servidor.py           # Core del backend y motor de inferencia YOLO
 ┣ 📜 cliente_serial.py     # Puente de escucha entre el Arduino y FastAPI
 ┣ 📜 index.html            # Interfaz de usuario y visor de cámara
 ┣ 📜 iniciar_sistema.bat   # Script de automatización de arranque
 ┣ 📜 best.pt               # Modelo de pesos entrenados (YOLOv8)
 ┣ 📜 .gitignore            # Reglas de exclusión de Git
 ┣ 📜 README.md             # Documentación del proyecto
 ┗ 📂 Sensor_ir             # Sensor Fisico

```
<img width="1901" height="867" alt="image" src="https://github.com/user-attachments/assets/9c9a7cad-a25b-4208-b33d-a007ee107708" />

## 👨‍💻 Autor

**Hugo Nicolas Pulido Moreno** - Ingeniería en Computación

