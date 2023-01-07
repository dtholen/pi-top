# Import modules
import sys
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
  motor_r.set_target_rpm(-speed)
  motor_l.set_target_rpm(speed)

def turn(speed, time):
    print ("turn",speed, time)
    motor_r.set_target_rpm(speed)
    motor_l.set_target_rpm(speed)
    sleep(time)
    stopWeel()

def collision(speed, time):
    turn(speed,time)
    moveWeel(-speed)
    sleep(1)
    stopWeel()
  
def stopWeel():
  motor_r.stop()
  motor_l.stop()
  
args=sys.argv
for arg in args:
  print ('Mode:',arg)
  if (arg== "1"):
      print ('Hello there', arg)
  if (arg== "2"):
      print ('--> drive forward',speed)
      moveWeel(speed)
      sleep(1)
      stopWeel()
  if (arg == "3"):
      print ('--> drive backward',speed)
      moveWeel(-speed)
      sleep(1)
      stopWeel()
  if (arg== "4"):
      print ('--> turn r',speed)
      turn(speed,1.0)
  if (arg== "5"):
      print ('--> turn l',-speed)
      turn(-speed,1.0)
  if (arg== "6"):
      print ('--> collision')
      collision(20,0.8)
  if (arg== "7"):
      print ('--> collision')
      collision(-20,0.8)
      


  
