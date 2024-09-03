const int numMicrophones = 6;
int microphonePins[numMicrophones] = {A0,A1,A2,A3,A4,A5};

void setup() {
  Serial.begin(9600); // Initialize serial communication
}

void loop() {
  // Read analog signals from all microphones
  for (int i = 0; i < numMicrophones; i++) {
    int microphoneReading = analogRead(microphonePins[i]);
    // Send the readings over serial
    Serial.print(microphoneReading);
    if (i < numMicrophones - 1) {
      Serial.print(","); // Delimiter between readings
    }
  }
  Serial.println(); // Newline to indicate end of data
  delay(100); // Adjust delay according to your sampling rate
}
