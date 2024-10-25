#include <Arduino.h>
#define MQ9_PIN 34         // Pin analógico para el sensor MQ-9
#define BUZZER_PIN 25      // Pin digital para el buzzer (simulado con LED)
#define EXTRACTOR_PIN 26   // Pin digital para el extractor (simulado con LED)
#define INTERRUPT_PIN 27   // Pin para activar la interrupción (simulado con botón)
#define GAS_THRESHOLD_MODERATE 120  
#define GAS_THRESHOLD_CRITICAL 150

bool alertaCritica = false;

void IRAM_ATTR manejarAlertaCritica() {
  alertaCritica = true;  // Cambiar estado cuando ocurra interrupción
}

void setup() {
  pinMode(MQ9_PIN, INPUT);
  pinMode(BUZZER_PIN, OUTPUT);
  pinMode(EXTRACTOR_PIN, OUTPUT);
  pinMode(INTERRUPT_PIN, INPUT_PULLUP);
  
  attachInterrupt(digitalPinToInterrupt(INTERRUPT_PIN), manejarAlertaCritica, RISING);

  Serial.begin(9600);  // Asegúrate de que coincida con el programa Python
  delay(2000);  // Esperar un momento para que el puerto serial se estabilice
}

void loop() {
  int gasLevel = analogRead(MQ9_PIN);  // Lee el nivel de gas del sensor

  // Mapea el nivel de gas a un rango más comprensible
  gasLevel = map(gasLevel, 0, 4095, 0, 200);

  // Enviar los datos al puerto serial en el formato: ID_SENSOR:NIVEL_GAS
  Serial.print("1:");  // ID del sensor (puede ser fijo)
  Serial.println(gasLevel);  // Nivel de gas

  // Alerta crítica de gas detectada
  if (alertaCritica || gasLevel >= GAS_THRESHOLD_CRITICAL) {
    activarBuzzer(true, 100);  // Buzzer rápido
    digitalWrite(EXTRACTOR_PIN, HIGH);  // Encender extractor
    alertaCritica = false;  // Reiniciar alerta crítica
  } 
  // Gas moderado
  else if (gasLevel > GAS_THRESHOLD_MODERATE) {
    activarBuzzer(true, 1000);  // Buzzer lento
    digitalWrite(EXTRACTOR_PIN, HIGH);  // Encender extractor
  } 
  // Gas en nivel seguro
  else {
    desactivarAlarma();
  }

  delay(1000);  // Espera 1 segundo antes de la próxima lectura
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
  digitalWrite(EXTRACTOR_PIN, LOW);  // Apagar extractor
}
