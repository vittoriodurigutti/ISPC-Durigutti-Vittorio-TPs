#include <Arduino.h>

// Pines del encoder y otros dispositivos
#define CLK_PIN 32          // Pin CLK del encoder
#define DT_PIN 33           // Pin DT del encoder
#define PULSADOR_PIN 27     // Pin del pulsador externo
#define BUZZER_PIN 25       // Pin del buzzer
#define EXTRACTOR_PIN 26    // Pin del LED verde (extractor)

// Variables globales
int gasLevel = 0;            // Nivel de gas simulado
int lastCLKState;            // Estado anterior del pin CLK
unsigned long lastDebounceTime = 0;  // Tiempo del último pulso
const unsigned long debounceDelay = 5;  // Tiempo de debounce (ms)
bool alertaCritica = false;  // Estado de alerta crítica

// **Prototipos de las funciones** (Declaraciones)
void activarBuzzer(bool encendido, int delayMs);
void desactivarAlarma();
void IRAM_ATTR manejarAlertaCritica();

void setup() {
  // Configurar los pines del encoder como entradas
  pinMode(CLK_PIN, INPUT);
  pinMode(DT_PIN, INPUT);
  pinMode(PULSADOR_PIN, INPUT_PULLUP);  // Pull-up interno para el pulsador

  // Configurar el buzzer y LED extractor
  pinMode(BUZZER_PIN, OUTPUT);
  pinMode(EXTRACTOR_PIN, OUTPUT);

  // Leer el estado inicial del pin CLK
  lastCLKState = digitalRead(CLK_PIN);

  // Iniciar comunicación serial
  Serial.begin(9600);
  Serial.println("ESP32 inicializado correctamente.");

  // Adjuntar interrupción al pulsador
  attachInterrupt(digitalPinToInterrupt(PULSADOR_PIN), manejarAlertaCritica, FALLING);
}

void loop() {
  // Leer el estado actual del CLK
  int currentCLKState = digitalRead(CLK_PIN);

  // Detectar cambios de estado con debounce
  if (currentCLKState != lastCLKState) {
    if (millis() - lastDebounceTime > debounceDelay) {
      // Verificar dirección del giro usando DT
      if (digitalRead(DT_PIN) != currentCLKState) {
        gasLevel++;  // Incrementar nivel de gas
      } else {
        gasLevel--;  // Decrementar nivel de gas
      }

      // Limitar el rango del nivel de gas entre 0 y 20
      gasLevel = constrain(gasLevel, 0, 30);

      // Mostrar el nivel de gas en el puerto serial
      Serial.print("1:");
      Serial.println(gasLevel);
      Serial.flush(); // intenta limpiar el buffer luego de cada envio.

      // Actualizar el tiempo de debounce
      lastDebounceTime = millis();
    }
  }

  lastCLKState = currentCLKState;  // Actualizar estado del CLK
  delay(10);

  
  // Verificar alertas de gas
  if (alertaCritica || gasLevel >= 15) {  // Alerta crítica
    activarBuzzer(true, 100);  // Buzzer rápido
    digitalWrite(EXTRACTOR_PIN, HIGH);  // Encender LED (extractor)
    alertaCritica = false;  // Reiniciar alerta crítica
  } else if (gasLevel >= 10) {  // Nivel moderado
    /*activarBuzzer(true, 1000);*/  // Buzzer lento
    digitalWrite(EXTRACTOR_PIN, HIGH);  // Encender LED (extractor)
  } else {  // Nivel seguro
    desactivarAlarma();
  }

  delay(10);  // Pequeño retraso para estabilidad
}

void activarBuzzer(bool encendido, int delayMs) {
  if (encendido) {
    digitalWrite(BUZZER_PIN, HIGH);
    delay(delayMs / 2);
    digitalWrite(BUZZER_PIN, LOW);
    delay(delayMs / 2);
  } else {
    digitalWrite(BUZZER_PIN, LOW);
  }
}

void desactivarAlarma() {
  digitalWrite(BUZZER_PIN, LOW);     // Apagar buzzer
  digitalWrite(EXTRACTOR_PIN, LOW);  // Apagar LED
} 

// Función para manejar la interrupción del pulsador
void IRAM_ATTR manejarAlertaCritica() {
  alertaCritica = true;  // Activar alerta crítica
}
