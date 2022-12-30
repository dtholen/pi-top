# Import modules
from pitop.pma import UltrasonicSensor,Buzzer, LED
from time import sleep

# Set up the components
ultrasonic_sensor = UltrasonicSensor("D0")  # <- Fill in the port the Ultrasonic Sensor is connected to
led_green = LED("D1")
led_amber = LED("D2")
led_red = LED("D3")                             # <- Fill in the port the LED is connected to
buzzer = Buzzer("D4")
# Loop, reading the value of the ultrasonic sensor
while True:
    print(ultrasonic_sensor.distance)
    sleep(0.1)
    # If the distance measured is less than 15cm, turn the led_red on
    if ultrasonic_sensor.distance < 0.15:
        led_red.on()
        led_green.off()
        led_amber.off()
        buzzer.on()
    else:
        led_red.off()
        if ultrasonic_sensor.distance < 0.30:
           buzzer.off()
           led_green.off()
           led_amber.on()
        else:
            buzzer.off()
            led_amber.off()
            if ultrasonic_sensor.distance < 0.40:
                led_amber.off()
                led_green.on()
            else:
                led_green.off()
