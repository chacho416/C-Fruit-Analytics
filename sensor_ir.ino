/**
 * Chachos Software - Escaner Agricola
 * Archivo: sensor_ir.ino
 * Plataforma: Arduino UNO
 *
 * Descripcion:
 *   Lee el pin digital de un sensor IR evasor de obstaculos.
 *   El sensor tiene salida ACTIVA EN BAJO (LOW = objeto detectado).
 *   Cuando detecta un fruto, envia el caracter '1' por Serial (una sola vez).
 *   Cuando el fruto se retira, el sistema queda listo para el siguiente escaneo.
 *
 * Conexion del sensor IR evasor:
 *   VCC  -> 5V  (Arduino)
 *   GND  -> GND (Arduino)
 *   OUT  -> Pin 2 (INPUT_PULLUP interno)
 */

// ---------------------------------------------------------------------------
// Constantes de configuracion
// ---------------------------------------------------------------------------
static const uint8_t IR_PIN         = 2;     // Pin digital del sensor IR
static const uint32_t SERIAL_BAUD   = 9600;  // Velocidad del puerto serial
static const uint16_t DEBOUNCE_MS   = 80;    // Tiempo anti-rebote (ms)

// ---------------------------------------------------------------------------
// Variables de estado (tipos primitivos, sin String)
// ---------------------------------------------------------------------------
static uint8_t  estadoAnterior      = HIGH;  // Estado previo del sensor
static uint32_t tiempoUltimoEvento  = 0;     // Marca de tiempo para debounce
static bool     escaneoPendiente    = false; // Evita envios repetidos

// ---------------------------------------------------------------------------
// setup()
// ---------------------------------------------------------------------------
void setup() {
  Serial.begin(SERIAL_BAUD);
  pinMode(IR_PIN, INPUT);      // El modulo IR ya tiene resistencia pull-up interna

  // Caracter de sincronizacion: le indica al cliente PC que el Arduino esta listo
  Serial.write('R');
  Serial.write('\n');
}

// ---------------------------------------------------------------------------
// loop()
// ---------------------------------------------------------------------------
void loop() {
  const uint8_t estadoActual = digitalRead(IR_PIN);
  const uint32_t ahora       = millis();

  // --- Deteccion de flanco descendente (HIGH -> LOW = fruto presente) ---
  if (estadoActual == LOW && estadoAnterior == HIGH) {
    if ((ahora - tiempoUltimoEvento) > DEBOUNCE_MS && !escaneoPendiente) {
      tiempoUltimoEvento = ahora;
      escaneoPendiente   = true;

      // Enviar bandera de escaneo: un solo caracter '1' seguido de newline
      Serial.write('1');
      Serial.write('\n');
    }
  }

  // --- Flanco ascendente (LOW -> HIGH = fruto retirado) ---
  // Resetear el flag para permitir el proximo escaneo
  if (estadoActual == HIGH && estadoAnterior == LOW) {
    if ((ahora - tiempoUltimoEvento) > DEBOUNCE_MS) {
      tiempoUltimoEvento = ahora;
      escaneoPendiente   = false;
    }
  }

  estadoAnterior = estadoActual;

  // Pequena pausa para no saturar el bucle (sin bloquear con delay largo)
  // Equivalente a un tick de muestreo de ~5 ms
  delayMicroseconds(5000);
}
