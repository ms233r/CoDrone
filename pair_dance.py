import CoDrone

drone = CoDrone.CoDrone()


class Drone:
    """Parent class with general data."""

    def get_statuses(self):
        """Get statuses from drone."""
        self.state = drone.get_state()
        self.flight_state = drone.is_ready_to_fly()
        return print(f"[info]: General State:\t{self.state}\n" +
                     f"[info]: Flight state:\t{self.flight_state}")


class Connection(Drone):
    """Connection class."""

    def __init__(self):
        self.pair_status = False

    def connect_ble(self):
        """Connect drone with BLE board."""
        # For me the BLE board is connected to COM5 port (device management).
        # TODO: Print error when BLE board is not connected.
        print("\nConnecting to drone #7852 on port COM5...")
        self.pair_status = drone.pair('7852', 'COM5')
        # TODO: Add check for battery level.
        if self.pair_status:
            print("Drone successfully paired")
        else:
            print("Try again for any drone and on any port")
            drone.pair()
        self.get_statuses()

    def disconnect_ble(self):
        """Disconnect drone from BLE board."""
        drone.disconnect()
        self.pair_status = False
        print("Drone is disconnected.")
        self.get_statuses()


class Flight(Drone):
    """Flight movements class."""

    def drone_dance(self):
        """Perform dance with drone."""
        Connection().connect_ble()
        if drone.is_ready_to_fly():
            print("Dance!, Dance!, Dance!")
            drone.takeoff()
            self.get_statuses()
            drone.hover(2)
            self.get_statuses()
            drone.land()
            self.get_statuses()
        else:
            print(f"\nDrone is not ready to fly.\n\nCheck:\n" +
                  f"1. Is the drone oriented right-side up?\n" +
                  f"2. Is the drone already flying?")
            while True:
                usri_continue = input("Do you want to try again? (y/n):\n")
                if usri_continue == 'y' or usri_continue == 'Y':
                    self.drone_dance()
                    break
                elif usri_continue == 'n' or usri_continue == 'N':
                    print(f"\n[!!!!]: Program terminated")
                    break
                else:
                    continue


def main():
    """Execute when program is run, not when imported."""
    if __name__ == '__main__':
        DRONE_FLIGHT = Flight()
        DRONE_FLIGHT.drone_dance()
        DRONE_CONNECT = Connection()
        DRONE_CONNECT.disconnect_ble()


main()
