int pot0 = A0;
int pot1 = A1;
int pot2 = A2;
int pot3 = A3;
int pot4 = A4;
int pot5 = A5;
int s0 = 2;
int s1 = 3;
int s2 = 4;
int s3 = 5;
int s4 = 6; 
int s5 = 7;
int sA = 8;

void setup() {
  //begin SLIPSerial just like Serial
  Serial.begin(9600);
}

void loop(){
  Serial.println(String(digitalRead(5)) + "," + String(digitalRead(4)) + "," + String(digitalRead(3)) + "," + String(digitalRead(2)) + "+" +
      String(analogRead(A0)) + "," + String(analogRead(A1)) + "," +  String(analogRead(A2)) + "," + String(analogRead(A3)) + "+" + 
      String(analogRead(A5)) + "+" + String(analogRead(A4)));
  delay(0);
}

