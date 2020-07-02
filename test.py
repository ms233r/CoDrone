import CoDrone

class Connection:

    def __init__(self):
        self.drone = CoDrone.CoDrone()

    def connect(self):
        """Connect to drone"""
        self.drone.pair('7852', 'COM5')
        print("Drone paired with BLE board")

    def disconnect(self):
        self.drone.disconnect()
        print("Drone disconnected from BLE board")

    def calibrate(self):
        self.drone.calibrate()

    def connection_test(self):
        self.drone.takeoff()
        self.drone.hover(3)
        self.drone.land()

if __name__ == '__main__':
    object = Connection()
    if object.drone.pair != True:
        object.connect()
    object.connection_test()
