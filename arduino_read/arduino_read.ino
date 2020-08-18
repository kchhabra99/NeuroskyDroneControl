int var1;
void setup(){
  Serial.begin(115200);
  }
  
void loop(){
 if (Serial.available()) {
var1=Serial.read();
Serial.println(var1);
 }
 delay(1000);
}
