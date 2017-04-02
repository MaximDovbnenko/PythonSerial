import serial

ser = serial.Serial("COM3", 115200)
DataArrayString = []
DataArray = []
maxCount = 100
EPS = 2

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

def get_data():
    count = 0
    DataArrayString.clear()
    while count < maxCount:
        data = read_serial()
        DataArrayString.append(data)
        count += 1
        
def read_serial():
    data = ser.readline()
    data = str(data)
    data = data[2:]
    data = data.replace("\\r\\n'", '')
    return data

def calculate():
    DataArray.clear()
    for line in DataArrayString:
        split_data = line.split(':')
        if len(split_data) == 3:
            tmp_data = DataLine(split_data[0], split_data[1], split_data[2])
            DataArray.append(tmp_data)
    IndexD1 = 0
    IndexD2 = 0
    i = 0
    for line in DataArray:
        if line.D1 == 0: IndexD1 = i
        else: i += 1
    i = 0
    for line in DataArray:
        if line.D2 == 0: IndexD2 = i
        else: i += 1
    ResultTime = DataArray[IndexD2].Time - DataArray[IndexD1].Time
    return ResultTime
        
while True:
    get_data()
    dT = calculate()
    print(dT)
    direction = -1 if dT < 0 else 1
    dT = abs(dT)
    Error = EPS - dT
    pass

