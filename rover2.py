# Import modules
import sys, json, signal, time, logging, threading, uuid
from pitop import EncoderMotor, ServoMotor, ForwardDirection  # Motor control library
from pitop.miniscreen import Miniscreen
from pitop.pma import UltrasonicSensor,Buzzer, Button, LED

signal = signal

ultrasonic_sensor = UltrasonicSensor("D0", threshold_distance=0.3)
args=sys.argv
# Set up the Motor on port M0 of the expansion plate
motor_r = EncoderMotor("M0", ForwardDirection.COUNTER_CLOCKWISE)
motor_l = EncoderMotor("M1", ForwardDirection.COUNTER_CLOCKWISE)
# Setup the servo on port S0 of the expansion plate
servo = ServoMotor("S0")
sp = 50 #sets servo speed and direction

miniscreen = Miniscreen()
led_green = LED("D1")
led_amber = LED("D2")
led_red = LED("D3") 
buzzer = Buzzer("D4")
button = Button("D5")

time_limit = 2
scip_param = 0
speed = 50
counter = [0,0,0]
setCounter = [100,100,100]
redLight = False
usr1_set = False
usr1_time = 2
tik = 10

def thread_servo(name):
 #   logging.info("Thread %s: starting", name)
    triggerServo()
    time.sleep(3.5)
 #   logging.info("Thread %s: finishing", name)
    x = threading.Thread(target=thread_servo, args=(uuid.uuid4(),))
    x.start()
    return(1)

def thread_measure(name):
#    logging.info("Thread %s: starting", name)
    measure()
    time.sleep(0.5)
#    logging.info("Thread %s: finishing", name)
    y = threading.Thread(target=thread_measure, args=(uuid.uuid4(),))
    y.start()
    return(1)

def signal_handler(sig, frame):
    signal_name = '(unknown)'
    if sig == signal.SIGHUP:
        signal_name = 'SIGHUP'
    elif sig == signal.SIGUSR1:
        signal_name = 'SIGUSR1'
        usr1_set = False
    elif sig == signal.SIGUSR2:
        signal_name = 'SIGUSR2'
    elif sig == signal.SIGALRM:
        signal_name = 'SIGALRM'
    elif sig == signal.SIGPOLL:
        signal_name = 'SIGPOLL'
    print ('Received ', signal_name, sig)


    if sig == signal.SIGTERM or sig == signal.SIGINT :
        sys.exit(0)
    elif sig == signal.SIGHUP:
        print("collision")
        collision(20,0.8)
    elif sig == signal.SIGUSR1:
        print("Hi")
        triggerServo()
        print("scan 1")
    elif sig == signal.SIGUSR2:
        measure()
        print("scan 2")
    elif sig == signal.SIGALRM:
        print("alarm")
    elif sig == signal.SIGPOLL:
        measure()
        print("Mesure")

    
    

def exit_handler(sig):
    print('Exiting....')
    print("Signal Number:", sig)  
    exit(0)

signal.signal(signal.SIGINT, exit_handler)
signal.signal(signal.SIGTERM, exit_handler)
signal.signal(signal.SIGHUP, signal_handler)
signal.signal(signal.SIGUSR1, signal_handler) # scan
signal.signal(signal.SIGUSR2, signal_handler) # measure
signal.signal(signal.SIGALRM, signal_handler)

#Move the servo using this is a function
def triggerServo():
    global sp
    servo.sweep(sp)
    sp = -sp
    # Print to the console
    print("Servo triggered with speed: " + str(sp))
    


#Move weel
def moveWeel(speed):
  global sp,id,ultrasonoc_sensor
  motor_r.set_target_rpm(-speed)
  motor_l.set_target_rpm(speed)

def turn(speed, time):
    print ("turn",speed, time)
    motor_r.set_target_rpm(speed)
    motor_l.set_target_rpm(speed)
    time.sleep(time)
    stopWeel()

def collision(speed, time):
    moveWeel(-speed)
    time.sleep(1)
    stopWeel()
    turn(speed,time)



def measure():
    global readLight
    floatNumber=ultrasonic_sensor.distance
    print("%.2f  " % floatNumber)
    sDistance  = " {:.2f}".format(floatNumber)
    miniscreen.display_multiline_text('Distance' + sDistance, font_size=20)

    if floatNumber < 0.20:
        led_red.on()
        redLight=True
        print ("Red:",redLight)
        led_green.off()
        led_amber.off()
    else:
        led_red.off()
        redLight = False
        if floatNumber < 0.40:
            led_green.off()
            led_amber.on()
        else:
            led_amber.off()
            if floatNumber > 0.50:
                led_green.on()
 

def terminate():
    print("Program terminated")
    stopWeel()
    for x in range(3):
        led_red.on()
        led_amber.on()
        led_green.on()
        time.sleep(0.5)
        led_red.off()
        led_amber.off()
        led_green.off()
        time.sleep(0.5)
    signal.signal(signal.SIGTERM, signal_handler)

def stopWeel():
  motor_r.stop()
  motor_l.stop()

def button_save():
    global ePassword, eMail
    print("-->Speicher")
    print(ePassword.get())
    print(eMail.get())
def close():
    fenster.destroy()
  

repeat = True
entry=args[1]
print ('Hello there')

print ('Mode F:',entry, repeat)


if (entry== "0"):
    print("\n======= Signal - System Name ===================\n")
    for signum in signal.valid_signals():
        print("{} - {}".format(signum, signal.strsignal(signum)))

if (entry== "1"):
    print(__name__)
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main    : wait for the thread to finish")
    logging.info("Main    : all done")
    x = threading.Thread(target=thread_servo, args=(uuid.uuid4(),))
    x.start()
    y = threading.Thread(target=thread_measure, args=(uuid.uuid4(),))
    y.start()

  
signal.pause()
terminate()
