#!/usr/bin/env python3
import time
import smbus
import paho.mqtt.client as mqtt

air_value = 225 # analog soil moisture value in air
water_value = 93 # analog soil moisture value in water
detect_interval = 30

# set the pin out mode of the GPIO module as GPIO.BCM
cmd = 0x84
address = 0x4b # 0x4b is the default i2c address for ADS7830 Module
bus = smbus.SMBus(1)
chn = 0
client = mqtt.Client()
client.connect("localhost", 1883, 60)

def detect():
    try:
        bus.write_byte(address,0)
        print("Found device in address 0x%x"%(address))
        return True
    except:
        print("Not found device in address 0x%x"%(address))
        return False

def convert_to_percentage(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def main(): 
    while detect():
        value = bus.read_byte_data(address, cmd|(((chn<<2|chn>>1)&0x07)<<4))
        soil_moisture = convert_to_percentage(value, air_value, water_value, 0, 100)
        print("Soil Moisture: "+ str(round(soil_moisture)) +"%")
        client.publish("moisture/raw", value)
        client.publish("moisture/value", round(soil_moisture))
        time.sleep(detect_interval)
        
if __name__ == '__main__': # Program entrance
    print ('Program is starting...')
    main()