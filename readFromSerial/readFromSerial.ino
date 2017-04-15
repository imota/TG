byte incomingByte1;
int LED = 8;
int pin = HIGH;

void setup(){
  pinMode(LED,OUTPUT);
  Serial.begin(115200);
  digitalWrite(LED,LOW); //turn off LED
}

void loop() {
  if (Serial.available() > 0) { 
    digitalWrite(LED,pin); //flash LED everytime data is available
    pin = !pin;
    delay(30);
    incomingByte1 = Serial.read(); //read incoming data
  }
}
