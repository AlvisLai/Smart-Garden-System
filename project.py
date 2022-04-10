#!/usr/bin/env python3
import RPi.GPIO as GPIO
from gpiozero import LightSensor
import paho.mqtt.client as mqtt
import time

client = mqtt.Client()
client.connect("localhost", 1883, 60)

def main():
    ldr = LightSensor(17)
    while True:
        client.publish("ldr/value", ldr.value)
        time.sleep(2) #push every 2 sec
    
    
main()