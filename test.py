import CoDrone


class Connection:
    """Connection class."""

    def __init__(self):
        self.drone = CoDrone.CoDrone()

    def connect_ble(self):
        """Connect drone with BLE board."""
        # My drone = '7852'.
        # Use 'self.drone.Nearest' to connect to another drone.
        # For me the BLE board is connected to COM5 port (device management).
        print("Connecting to drone...")
        self.drone.pair('7852', 'COM5')

    def disconnect_ble(self):
        """Disconnect drone from BLE board."""
        self.drone.disconnect()
        print("Drone disconnected.")

    def calibrate(self):
        """Calibrate drone."""
        self.drone.calibrate()

    def connection_ble_test(self):
        """Move drone for testing connection."""
        self.drone.takeoff()
        self.drone.hover(5)
        self.drone.land()


if __name__ == '__main__':
    OBJECT = Connection()
    OBJECT.connect_ble()
    OBJECT.connection_ble_test()
    OBJECT.disconnect_ble()
