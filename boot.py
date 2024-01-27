import network
import ugit
import time
import machine

onboardled = machine.Pin(2, machine.Pin.OUT)

update_pin = machine.Pin(4, machine.Pin.IN)

def connect_to_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.disconnect()
    wlan.connect(ssid, password)
    
    # Wait for the connection to be established
    checks = 0
    while not wlan.isconnected():
        time.sleep(1)
        print("waiting ..")
        checks += 1
        if checks == 5:
            raise Exception(ssid, ' failed!')
    
    print("Connected to", ssid)

# List of networks to try
networks = [
    {"ssid": "MunichUrbanColab", "password": "innovation"},
    {"ssid": "iPhone von Dennis", "password": "dennis98!"}
    # Add more networks as needed
]



# Try connecting to each network in the list
for network_info in networks:
    print("Trying to connect to wifi ...")
    onboardled.value(1)
    time.sleep(0.5)
    onboardled.value(0)
    time.sleep(0.5)
    onboardled.value(1)
    try:
        print("Trying: " + network_info["ssid"])
        connect_to_wifi(network_info["ssid"], network_info["password"])
        # If connected, break out of the loop
        onboardled.value(0)
        time.sleep(0.3)
        onboardled.value(1)
        time.sleep(0.3)
        onboardled.value(0)
        break
    except Exception as e:
        print(f"Failed to connect to {network_info['ssid']}: {e}")
        onboardled.value(0)
        time.sleep(0.3)
        onboardled.value(1)
        time.sleep(1)
        onboardled.value(0)

# After attempting to connect to all networks, pull from the repository
time.sleep(0.5)
onboardled.value(1)




if update_pin.value():
    print("Update Pin high, updating and rebooting...")
    files_updated = ugit.pull_all(isconnected=True)
    time.sleep(2)  # Delay for any print messages to be displayed
    machine.reset()
else:
    print("No files were updated.")

print("Everything done, going to main.py ....")
onboardled.value(0)
time.sleep(0.3)
onboardled.value(1)
time.sleep(0.3)
onboardled.value(0)


