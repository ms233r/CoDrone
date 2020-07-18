import CoDrone
import time

DRONE = CoDrone.CoDrone()


class Drone:
    """Parent class with general data."""

    def get_statuses(self):
        """Get statuses from drone."""
        self.state = DRONE.get_state()
        self.flight_state = DRONE.is_ready_to_fly()
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
        self.pair_status = DRONE.pair('7852', 'COM5')
        # TODO: Add check for battery level.
        if self.pair_status:
            print("Drone successfully paired")
        else:
            print("Try again for any drone and on any port")
            DRONE.pair()
        self.get_statuses()

    def disconnect_ble(self):
        """Disconnect drone from BLE board."""
        DRONE.disconnect()
        self.pair_status = False
        print("Drone is disconnected.")
        self.get_statuses()


class Flight(Drone):
    """Flight movements class."""

    def drone_pushups(self):
        """Perform dance with drone."""
        Connection().connect_ble()
        if DRONE.is_ready_to_fly():
            print("Dance!, Dance!, Dance!")
            for rounds in range(5):
                DRONE.takeoff()
                time.sleep(1)
                DRONE.land()
                time.sleep(1)

        else:
            print(f"\nDrone is not ready to fly.\n\nCheck:\n" +
                  f"1. Is the drone oriented right-side up?\n" +
                  f"2. Is the drone already flying?")
            while True:
                usri_continue = input("Do you want to try again? (y/n):\n")
                if usri_continue == 'y' or usri_continue == 'Y':
                    self.drone_pushups()
                    break
                elif usri_continue == 'n' or usri_continue == 'N':
                    print(f"\n[!!!!]: Program terminated")
                    break
                else:
                    continue
        DRONE.close()  # TODO: https://edu.workbencheducation.com/cwists/cwistings/101301/37916


def main():
    """Execute when program is run, not when imported."""
    if __name__ == '__main__':
        DRONE_FLIGHT = Flight()
        DRONE_FLIGHT.drone_pushups()


main()
