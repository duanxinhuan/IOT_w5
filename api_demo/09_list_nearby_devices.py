import bluetooth
import time

while True:
    print("Scanning...")
    nearbyDevices = bluetooth.discover_devices()

    for macAddress in nearbyDevices:
        print("Found device with mac-address: " + macAddress)

    print("Sleeping for 10 seconds.")
    time.sleep(10)
