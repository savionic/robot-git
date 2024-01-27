#sample main.py for testing Microphyton for ESP32 for Sparkfun TB6612FNG Motor Drive for two motors
from machine import Pin, PWM
from time import sleep
from TB6612FNG import Motor
import network
# from network import espnow
import ubinascii
import binascii
import espnow
onboardled = machine.Pin(2, machine.Pin.OUT)


frequency = 50

BIN2 = 14 
BIN1 = 27 
STBY = 26
AIN1 = 32
AIN2 = 33
PWMA = 12
PWMB = 13
ofsetA = 1
ofsetB = 1

motor = Motor(BIN2,BIN1,STBY,AIN1,AIN2,PWMA,PWMB,ofsetA,ofsetB)

print("Initializing ...")
onboardled.value(1)
time.sleep(1)
onboardled.value(0)
#motor.forward(400)
#sleep(10)

#motor.backward(600)
#sleep(10)

#motor.right(700)
#sleep(10)

#motor.left(800)
#sleep(10)

#motor.brake()
#sleep(5)

#motor.stop()
#sleep(5)

#motor.standby()
#sleep(5)

#motor.run()
#sleep(5)



#print("End running motor ...")

 
#sleep(20)


# A WLAN interface must be active to send()/recv()
        
sta = network.WLAN(network.STA_IF)    # Enable station mode for ESP
sta.active(True)
sta.disconnect()        # Disconnect from last connected WiFi SSID
ac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
print("MAC Address:", ac)

import network
import espnow

def espnow_rx():
    #config UART
    uart = UART(0, baudrate=115200)

    # A WLAN interface must be active to send()/recv()
    sta = network.WLAN(network.STA_IF)
    sta.active(True)
    sta.disconnect()                # Disconnect from last connected WiFi SSID

    e = espnow.ESPNow()                  # Enable ESP-NOW
    e.active(True)

    peer = b'\x5c\xcf\x7f\xf0\x06\xda'   # MAC address of peer's wifi interface
    e.add_peer(peer)                     # Sender's MAC registration

    while True:
        host, msg = e.recv()
        
        befehl = msg[0]
        if befehl:
            if befehl == 0:
                motor.stop()
                print("stop 0:")
                
                onboardled.value(1)
                time.sleep(1)
                onboardled.value(0)
            elif befehl == 1:
                motor.forward(400)
                onboardled.value(1)
                time.sleep(1)
                onboardled.value(0)
                print("forwaert 1:")
            elif befehl == 2:
                motor.backward(400)
                onboardled.value(1)
                time.sleep(1)
                onboardled.value(0)
                print("rueckwaerts 2:")
            elif befehl == 3:
                motor.left(200)
                #motor.right(200)
                print("links 3:")
                onboardled.value(1)
                time.sleep(1)
                onboardled.value(0)
            elif befehl == 4:
                motor.right(200)
                onboardled.value(1)
                time.sleep(1)
                onboardled.value(0)
                # motor.right(200)
                print("rechts 4:")
        # if msg:                          # wait for message
         #   if msg == b'walk':           # decode message and translate
         #       print("WALKING")      # to the NyBoard's command
         #   elif msg == b'back':
         #       print("BACK")
         #   elif msg == b'stop':
         #       print("STOP")
         #   else:
         #       print(msg)
         #       print(msg[0])
         #       print(binascii.a2b_base64(msg))

if __name__ == "__main__":
    espnow_rx()
    


