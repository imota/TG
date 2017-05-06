int pin;

void setup(){
  Serial.begin(9600);
  while(!Serial);
  for (int i=2; i<=19; i++) {
    pinMode(i,OUTPUT);
  }
}

bool flag = HIGH;
void loop() {
  if (Serial.available() > 0) { 
    pin = Serial.read();
    digitalWrite(pin,flag);
    flag = !flag;
  }
}
