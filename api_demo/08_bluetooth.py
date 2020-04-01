# Simple inquiry example.
# 
# sudo apt install bluetooth bluez python-bluez blueman
# pip3 install pybluez
import bluetooth

nearby_devices = bluetooth.discover_devices(lookup_names = True)
print("Found %d devices" % len(nearby_devices))

for addr, name in nearby_devices:
    print("%s - '%s'" % (addr, name))
