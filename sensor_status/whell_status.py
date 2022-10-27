class WhellStatus():
    def __init__(self, *args):
        self.type_devise = "odrive" # input parametr (rosparam)
        self.type_mode = "dif"
        self.path = "/dev/ttyUSB0"
    
    def power_status(self):
        if self.type_devise == "odrive":
                pass
        status:bool = True
        value:float = 23 
        return status, value

    def connect_status(self):
        pass
        return status
    
    def data_status(self):
        pass
        return status, error

    def test(self):
        pass
        return status, error


def main():
    whell = WhellStatus()
    print(whell.power_status())
    print('Hi from sensor_status.')
    print()

if __name__ == '__main__':
    main()
