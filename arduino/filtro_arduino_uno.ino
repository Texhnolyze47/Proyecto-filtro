/*
Esta una version estable que no incluye los filtro por problemas de envio de datos por parte de arduino

*/

#include <Float64.h>
void setup() {
  Serial.begin(9600);

}

void loop() {

  if (Serial.available()) {
    
    String bytes = Serial.readString();
    f64 x = atof64(Serial.readString().c_str());
    x.setDecs(17);
    Serial.print(F("Float value: "));
    Serial.println(bytes);
  }
}
