from SerialReadTest import DataGather
import time
dataGather = DataGather('COM3', 115200, 1000, 0)

   
def main():  
    Start_f = 100
    Curent_f = Start_f
    Max_f = 300;
    Step = 1;
    IsNeedCorrectF = True
    dataGather.setStartF(Start_f)
    print('Start')
    dataGather.Start()
    T2 = time.sleep(15)
    while True:
        dT = dataGather.calculate()
        T1 = time.clock()
        if IsNeedCorrectF:
            if dT > 0:
                dataGather.incF()
                Curent_f += Step
            elif dT < 0:
                dataGather.decF()
                Curent_f -= Step
            dataGather.setStartF(Curent_f)
            dataGather.Start()
            if Curent_f > Max_f:
                dataGather.setStartF(Start_f)
                Curent_f = Start_f
        T2 = time.clock()  
        T = T2 - T1
        line_out = "Time: " + str(T) + "  Faze Error: " + str(dT) + " CurentF: " + str(Curent_f)
        print(line_out)

if __name__ == '__main__':
    main()