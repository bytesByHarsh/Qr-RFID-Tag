float tem;
int tempPin = 0;
int relay = 13;

void setup() {
    Serial.begin(9600);
    pinMode(relay, OUTPUT)
    digitalWrite(relay, LOW);
}

void loop() {
   tem = analogRead(tempPin);
   
   // read analog volt from sensor and save to variable temp
   tem = tem * 0.48828125;
   
   // convert the analog volt to its temperature equivalent
   Serial.print("TEMPERATURE FROM THE SENSOR = ");

   // display temperature value
   Serial.print(tem);
   Serial.print("*C");
   Serial.println();
   
   // update sensor reading each one second
   delay(1000);
	 
    if(tem > desired_temp) {
        digitalWrite(relay, HIGH);
        Serial.print("Temprature Going Higher,Starting the cooling system...");
    }
    else {
        digitalWrite(relay, LOW);
    }
}
