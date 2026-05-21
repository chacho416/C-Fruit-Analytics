import cv2
import numpy as np

# Creamos una "ventana" con barras deslizantes (sliders) para encontrar el color perfecto.
def nothing(x):
    pass

cv2.namedWindow('Calibrador HSV')

# Sliders para el rango BAJO
cv2.createTrackbar('H (Bajo)', 'Calibrador HSV', 15, 179, nothing)
cv2.createTrackbar('S (Bajo)', 'Calibrador HSV', 15, 255, nothing)
cv2.createTrackbar('V (Bajo)', 'Calibrador HSV', 15, 255, nothing)

# Sliders para el rango ALTO
cv2.createTrackbar('H (Alto)', 'Calibrador HSV', 95, 179, nothing)
cv2.createTrackbar('S (Alto)', 'Calibrador HSV', 255, 255, nothing)
cv2.createTrackbar('V (Alto)', 'Calibrador HSV', 255, 255, nothing)

# CÁMERA (Pon aquí el número de tu cámara, 0 o 1 o 2)
camara = cv2.VideoCapture(1) 

print("INSTRUCCIONES:")
print("1. Pon el limón sobre el papel blanco.")
print("2. Mueve los sliders 'Bajo' hacia la IZQUIERDA y los 'Alto' hacia la DERECHA hasta que SOLO el limón se vea BLANCO en la ventana de Máscara.")
print("3. Cuando la máscara esté perfecta, anota los números en la terminal.")
print("4. Presiona 'ESC' para salir.")

while(1):
    # 1. Capturar frame de la cámara
    _, frame = camara.read()
    if frame is None:
        break
        
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 2. Leer las posiciones de los sliders
    h_bajo = cv2.getTrackbarPos('H (Bajo)', 'Calibrador HSV')
    s_bajo = cv2.getTrackbarPos('S (Bajo)', 'Calibrador HSV')
    v_bajo = cv2.getTrackbarPos('V (Bajo)', 'Calibrador HSV')
    
    h_alto = cv2.getTrackbarPos('H (Alto)', 'Calibrador HSV')
    s_alto = cv2.getTrackbarPos('S (Alto)', 'Calibrador HSV')
    v_alto = cv2.getTrackbarPos('V (Alto)', 'Calibrador HSV')

    # 3. Crear el rango con los valores de los sliders
    rango_bajo = np.array([h_bajo, s_bajo, v_bajo])
    rango_alto = np.array([h_alto, s_alto, v_alto])

    # 4. Crear la máscara (SÓLO lo que está dentro del rango se vuelve blanco)
    mascara = cv2.inRange(hsv, rango_bajo, rango_alto)
    
    # Opcional: ver el resultado sobre la foto real
    resultado = cv2.bitwise_and(frame, frame, mask=mascara)

    cv2.imshow('Foto Real', frame)
    cv2.imshow('Máscara (Solo el rango detectado)', mascara)
    cv2.imshow('Resultado', resultado)

    # Imprimir valores actuales en terminal
    print(f"\rRango Bajo: [{h_bajo},{s_bajo},{v_bajo}] | Rango Alto: [{h_alto},{s_alto},{v_alto}]", end="")

    if cv2.waitKey(1) & 0xFF == 27: # Presionar ESC para salir
        break

camara.release()
cv2.destroyAllWindows()