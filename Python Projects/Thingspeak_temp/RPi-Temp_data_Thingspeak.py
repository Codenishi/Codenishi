import urllib.request
import time as t
import RPi.GPIO as g
import Adafruit_DHT

# Set up GPIO
g.setwarnings(False)
g.setmode(g.BCM)
g.setup(21, g.OUT)  # LED (BCM pin 21 corresponds to BOARD pin 40)
g.setup(20, g.OUT)  # DC Motor (BCM pin 20 corresponds to BOARD pin 38)

# Set up sensor
sensor = Adafruit_DHT.DHT11
pin = 5  # GPIO pin where the sensor is connected (BCM pin 5 corresponds to BOARD pin 29)

while True:
    
    humidity, temp = Adafruit_DHT.read_retry(sensor, pin)
    	
    
    if temp is not None:
            print(f"Temperature: {temp:.1f}C")
            print("Humidity:",humidity)
    
            if temp >25:
                
                print("Temperature is above 25C. Turning on LED and DC motor.")
                g.output(21, g.HIGH)  # Turn on LED
                t.sleep(10)
                g.output(21, g.LOW)
                g.output(20, g.HIGH)  # Turn on DC motor
                t.sleep(10)
                g.output(20,g.LOW)
                url="https://api.thingspeak.com/update?api_key=5II6FF3Y6AI7O3BP&field3="+str(temp)+"&field4="+str(humidity)
                conn=urllib.request.urlopen(url)
                print ("data uploaded")	
		
            else:
                print("Temperature is below 25C. Turning off LED and DC motor.")
                g.output(21, g.LOW)  # Turn off LED
                g.output(20, g.LOW)  # Turn off DC motor
    else:
        print("Failed to get reading. Try again!")
    
    t.sleep(2)
