import CoDrone

drone = CoDrone.CoDrone()

def connect():
    """Connect to drone with BLE."""
    print("Start Pairing with BLE boar ...")
    drone.pair(drone.Nearest)
    print("Drone paired with BLE board")

def disconnect():
    drone.disconnect()
    print("Drone disconnected from BLE board")

def conn_dance():
    drone.takeoff()
    drone.hover(1)
    drone.land()

if __name__ == '__main__':
    conn_dance()
