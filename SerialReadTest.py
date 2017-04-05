'''
/*Arduino code*/
void setup() {
  // put your setup code here, to run once:
  pinMode(8, INPUT);
  pinMode(9, INPUT);
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.print(digitalRead(8));
  Serial.print(":");
  Serial.print(digitalRead(9));
  Serial.print(":");
  Serial.println(millis());
}
'''
import serial

class DataLine:
    def __init__(self, d1, d2, time):
        try:
            self.D1 = int(d1)
            self.D2 = int(d2)
            self.Time = int(time)
        except:
            self.D1 = 0
            self.D2 = 0
            self.Time = 0
    def __str__(self):
        return "{"+self.D1+","+self.D2+","+self.Time+"}"

class DataGather:
    def __init__(self, comPort, rate, maxCount, s_val):
        self.DataArrayString = []
        self.serial = serial.Serial(comPort, rate)
        self.DataArray = []
        self.maxCount = maxCount
        self.Val = s_val

    def get_data(self):
        count = 0
        self.DataArrayString.clear()
        while count < self.maxCount:
            data = self.read_serial()
            self.DataArrayString.append(data)
            count += 1
        
    def read_serial(self):
        data = self.serial.readline()
        data = str(data)
        data = data[2:]
        data = data.replace("\\r\\n'", '')
        return data
    
    def indexOf(self, signal):
        i = 0;
        for line in self.DataArray:
            if signal == 1:
                if line.D1 == self.Val: break
            if signal == 2: 
                if line.D2 == self.Val: break
            i += 1
        return i
    def calculate(self):
        self.get_data()
        self.DataArray.clear()
        for line in self.DataArrayString:
            split_data = line.split(':')
            if len(split_data) == 3:
                tmp_data = DataLine(split_data[0], split_data[1], split_data[2])
                self.DataArray.append(tmp_data)
        IndexD1 = self.indexOf(1)
        IndexD2 = self.indexOf(2)
        ResultTime = self.DataArray[IndexD1].Time - self.DataArray[IndexD2].Time
        return ResultTime
        


