#define F_AOUTO_PIN   8
#define DATA_1_INPUT  7
#define DATA_2_INPUT  6

int  cmd = -1;
int  arg1 = 0;
int  step_f;
long current_furqery = 0;
void init_contacts(){
  pinMode(F_AOUTO_PIN, OUTPUT);
  pinMode(DATA_1_INPUT, INPUT);
  pinMode(DATA_2_INPUT, INPUT);
  Serial.begin(115200);
}

void setup() {
  init_contacts();
}
void parse_incoming_cmd(){
    switch(cmd){
        //Start
        case 100: tone(F_AOUTO_PIN, current_furqery); break;
        //Set start F
        case 101: current_furqery = arg1; break;
        //Set step size
        case 102: step_f = arg1; break;
        //inc
        case 103: current_furqery += step_f; tone(F_AOUTO_PIN, current_furqery); break;
        //dec
        case 104: current_furqery -= step_f; tone(F_AOUTO_PIN, current_furqery); break;
    }
    /*Serial.println("-----------------------------------");
    Serial.print(cmd);
    Serial.print(" ");
    Serial.println(current_furqery);
    Serial.println("-----------------------------------");
    delay(2000);*/
}
void send_status(){
  Serial.print(digitalRead(DATA_1_INPUT));
  Serial.print(":");
  Serial.print(digitalRead(DATA_2_INPUT));
  Serial.print(":");
  Serial.println(millis());
}
void loop(){
  send_status();
  if (Serial.available() != 0) { 
    long ComandList[2]= {0, 0};
    int i = 0;
    int sign = 1;
    byte incomingByte = Serial.read();
    while (incomingByte != ';') {
      if (ComandList[i] == 0) {
        if(incomingByte == '-') { sign=-1;}
      }
      if (incomingByte == ' ') {
          ComandList[i] *= sign;
          sign = 1;
          i++;
      } else if (incomingByte >= '0' && incomingByte <= '9') {
          ComandList[i] = ComandList[i] * 10 + incomingByte - '0';
      }
      while(Serial.available() == 0) {
          delayMicroseconds(1);
          send_status();
      }
      incomingByte = Serial.read();
    }
    ComandList[i] *= sign;
    cmd  = ComandList[0];
    arg1 = ComandList[1];
    parse_incoming_cmd();
  }
}