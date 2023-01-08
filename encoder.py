# Import modules
import sys, json
from pitop import EncoderMotor, ForwardDirection  # Motor control library
from time import sleep  # Allows us to tell the program to wait
from pitop.miniscreen import Miniscreen
from pitop.pma import UltrasonicSensor,Buzzer, Button, LED
from tkinter import *

ultrasonic_sensor = UltrasonicSensor("D0")

# Set up the Motor on port M0 of the expansion plate
motor_r = EncoderMotor("M0", ForwardDirection.COUNTER_CLOCKWISE)
motor_l = EncoderMotor("M1", ForwardDirection.COUNTER_CLOCKWISE)
time_limit = 2
scip_param = 0
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

def button_save():
    print("-->Speicher")
def close():
    fenster.destroy()
  
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
  if (arg== "12"):
      print ('--> move forward')
      speed = int(input("Enter Speed : "))
      duration = int(input("Enter duration (sec): "))
      print("Speed:", speed)
      moveWeel(int(speed))
      sleep(duration)
      stopWeel()
  if (arg== "13"):
      print ('--> move backward')
      speed = int(input("Enter Speed : "))
      duration = int(input("Enter duration (sec): "))
      print("Speed:", speed)
      moveWeel(int(speed))
      sleep(duration)
      stopWeel()
  if (arg== "14"):
      print ('--> turn r',speed)
      speed = int(input("Enter Speed : "))
      duration = int(input("Enter duration (sec): "))
      print("Speed:", speed)
      turn(speed,duration)
  if (arg== "15"):
      print ('--> turn l',speed)
      speed = int(input("Enter Speed : "))
      duration = int(input("Enter duration (sec): "))
      print("Speed:", speed)
      turn(-speed,duration)
  if (arg== "20"):
      print ('--> GUI')
# some JSON:
      data =  '{ "speed":"", "duration":1}'
      fenster = Tk()
      fenster.title("Define parameters")
      fenster.title('PythonGuides')
      fenster.geometry('400x300')
      fenster.config(bg='#9FD996')
      lMail = Label(fenster, text='Enter Email:', bg='#9FD996').grid(row=0, column=0,sticky = W, pady = 2,rowspan=2)
      lPassword = Label(fenster, text='Enter Password:', bg='#9FD996').grid(row=1, column=0,sticky = W, pady = 2,rowspan=2)
      eMail= Entry(fenster).grid(row=0, column=1)
      ePassword=Entry(fenster).grid(row=1, column=1)
      bCancel = Button(fenster,text='Cancel', command=close).grid(row=3, column=0)
      bSave = Button(fenster,text='Login', command=button_save).grid(row=3, column=1)

      fenster.mainloop()
      print("-->finish")


  
