from SerialReadTest import DataGather

dataGather = DataGather('COM3', 115200, 2000, 0)

def main():
    while True:
        dT = dataGather.calculate()
        if dT >= 0:
            print(dT)
    pass

if __name__ == '__main__':
    main()