# Import modules
from pitop import EncoderMotor, ForwardDirection  # Motor control library
from time import sleep  # Allows us to tell the program to wait
from pitop.miniscreen import Miniscreen
from pitop.pma import UltrasonicSensor,Buzzer, Button, LED

ultrasonic_sensor = UltrasonicSensor("D0")

# Set up the Motor on port M0 of the expansion plate
motor_r = EncoderMotor("M0", ForwardDirection.COUNTER_CLOCKWISE)
motor_l = EncoderMotor("M1", ForwardDirection.COUNTER_CLOCKWISE)
time_limit = 2
speed = 50
counter = [0,0,0]
setCounter = [100,100,100]
#Move weel
def moveWeel(speed):
  global sp,id,ultrasonoc_sensor
  motor_r.set_target_rpm(speed)
  motor_l.set_target_rpm(-speed)
def stopWeel():
  motor_r.stop()
  motor_l.stop()


for x in range(3):
  # Now for the algorith
  moveWeel(speed)
  sleep(1)
  moveWeel(-speed)
  sleep(1)
  stopWeel()
