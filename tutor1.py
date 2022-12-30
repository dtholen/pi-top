# Import modules
from pitop.miniscreen import Miniscreen
from pitop.pma import UltrasonicSensor,Buzzer, Button, LED
from time import sleep

# Set up the components
ultrasonic_sensor = UltrasonicSensor("D0")  # <- Fill in the port the Ultrasonic Sensor is connected to
led_green = LED("D1")
led_amber = LED("D2")
led_red = LED("D3")                             # <- Fill in the port the LED is connected to
buzzer = Buzzer("D4")
button = Button("D5")
# Loop, reading the value of the ultrasonic sensor
# Initialise the Miniscreen
miniscreen = Miniscreen()

while not button.is_pressed:
    floatNumber=ultrasonic_sensor.distance
    print("%.2f" % floatNumber)
    sDistance  = " {:.2f}".format(floatNumber)
    miniscreen.display_multiline_text('Distance' + sDistance, font_size=20)
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


# Print to the console 
print("Program terminated")
for x in range(3):
    led_red.on()
    led_amber.on()
    led_green.on()
    buzzer.on()
    sleep(0.5)
    led_red.off()
    led_amber.off()
    led_green.off()
    buzzer.off()
    sleep(0.5)

 