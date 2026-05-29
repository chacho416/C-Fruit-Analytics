import cv2
import numpy as np
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from ultralytics import YOLO

app = FastAPI(title="Chachos Software - Motor AIoT")
# 🟢 El Semáforo en memoria
alerta_escaneo = False

@app.post("/alerta")
def activar_alerta():
    global alerta_escaneo
    alerta_escaneo = True
    return {"status": "alerta_recibida_servidor"}

@app.get("/status_alerta")
def verificar_alerta():
    global alerta_escaneo
    estado_actual = alerta_escaneo
    if alerta_escaneo:
        alerta_escaneo = False  # Apagamos el semáforo inmediatamente tras ser leído
    return {"disparar": estado_actual}
# --- BLOQUE DE SEGURIDAD (CORS) ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- CARGAR EL CEREBRO ---
print("Cargando red neuronal YOLOv8...")
modelo_ia = YOLO("best.pt")  # Asegúrate de que 'best.pt' esté en el mismo directorio o proporciona la ruta correcta
print("¡Cerebro en línea!")

@app.post("/procesar")
async def analizar_fruto(file: UploadFile = File(...)):
    try:
        # 1. Recibir la foto de la página web y convertirla a formato matemático
        contents = await file.read()
        nparr = np.frombuffer(contents, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # 2. ¡EL ESCANEO! Pasamos la imagen por la Inteligencia Artificial
        resultados = modelo_ia(img)
        
        # 3. Analizar el dictamen
        detecciones = resultados[0].boxes
        
        if len(detecciones) == 0:
            return {"veredicto": "No se detectó ningún aguacate en la imagen."}
        
        # Tomamos el objeto con la mayor seguridad de detección
        mejor_deteccion = detecciones[0] 
        id_clase = int(mejor_deteccion.cls[0])
        confianza = float(mejor_deteccion.conf[0]) * 100
        
        # Obtenemos el nombre exacto de la clase (Sana, enferma, etc.)
        nombre_resultado = resultados[0].names[id_clase]
        
        # 4. Enviar el resultado de regreso a la página web
        return {
            "veredicto": nombre_resultado,
            "confianza": f"{confianza:.1f}%"
        }
        
    except Exception as e:
        return {"error": f"Ocurrió un problema en el servidor: {str(e)}"}