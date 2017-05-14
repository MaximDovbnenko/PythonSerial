from SerialReadTest import DataGather

dataGather = DataGather('COM3', 115200, 2000, 0)

   
def main():  
    Start_f = 100
    Curent_f = Start_f
    Max_f = 1300;
    Step = 10;
    dataGather.setStep(10)
    dataGather.setStartF(Start_f)
    dataGather.Start()
    while True:
        dataGather.Start()
        dataGather.incF()
        dT = dataGather.calculate()
        if dT > 0:
            dataGather.incF()
            Curent_f += Step
        elif dT < 0:
            dataGather.decF()
            Curent_f -= Step
        if Curent_f > Max_f:
            dataGather.setStartF(Start_f)
    pass

if __name__ == '__main__':
    main()