# Import modules
import sys, json, signal, time, logging, threading, uuid
from pitop import EncoderMotor, ServoMotor, ForwardDirection  # Motor control library
from pitop.miniscreen import Miniscreen
from pitop.pma import UltrasonicSensor,Buzzer, Button, LED

signal = signal
print("\n======= Signal - System Name ===================\n")

# for signum in signal.valid_signals():
#    print("{} - {}".format(signum, signal.strsignal(signum)))


ultrasonic_sensor = UltrasonicSensor("D0", threshold_distance=0.3)
args=sys.argv
# Set up the Motor on port M0 of the expansion plate
motor_r = EncoderMotor("M0", ForwardDirection.COUNTER_CLOCKWISE)
motor_l = EncoderMotor("M1", ForwardDirection.COUNTER_CLOCKWISE)
# Setup the servo on port S0 of the expansion plate
servo = ServoMotor("S0")
sp = 100 #sets servo speed and direction

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
alarm_set = False
usr1_set = False
usr1_time = 2
tik = 10

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)
    signal.raise_signal(signal.SIGUSR1)

def signal_handler(sig, frame):
    global alarm_set
    signal_name = '(unknown)'
    if sig == signal.SIGHUP:
        signal_name = 'SIGHUP'
    elif sig == signal.SIGUSR1:
        signal_name = 'SIGUSR1'
        usr1_set = False
    elif sig == signal.SIGUSR2:
        signal_name = 'SIGUSR2'
    elif sig == signal.SIGALRM:
        alarm_set = False
        signal_name = 'SIGALRM'
    print ('Received ', signal_name, 'signal')


    if sig == signal.SIGTERM or sig == signal.SIGINT :
        sys.exit(0)
    elif sig == signal.SIGHUP:
        print("collision")
        collision(20,0.8)
    elif sig == signal.SIGUSR1:
        triggerServo()
        print("scan 1")
    elif sig == signal.SIGUSR2:
        measure()
        print("scan 2")
    elif sig == signal.SIGALRM:
        print("alarm")
        alarm_set = False

    
    

def exit_handler(sig, frame):
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

def triggerMesure():
  measure()
  servo.sweep(sp)

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
    print("%.2f  " % floatNumber, alarm_set)
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
print ('Hello there')


for arg in args:
    print ('Hello there', arg)
    print ('Mode:',arg)

for arg in args:
    repeat = True
    print ('Mode F:',arg, repeat)
    i=1;
    while not button.is_pressed and repeat:
        repeat = False
        if (arg== "1"):
            print(__name__)
            if __name__ == "__main__":
                format = "%(asctime)s: %(message)s"
                logging.basicConfig(format=format, level=logging.INFO,
                                    datefmt="%H:%M:%S")
                logging.info("Main    : before creating thread")
                x = threading.Thread(target=thread_servo, args=(uuid.uuid4(),))
                x.start()
                logging.info("Main    : wait for the thread to finish")
                y = threading.Thread(target=thread_measure, args=(uuid.uuid4(),))
                y.start()
                logging.info("Main    : all done")

            measure()
            repeat = True
            time.sleep(3)
        if (arg== "2"):
            print ('--> drive forward',speed)
            moveWeel(speed)
            time.sleep(1)
        if (arg == "3"):
            print ('--> drive backward',speed)
            moveWeel(-speed)
            time.sleep(1)
        if (arg== "4"):
            print ('--> turn r',speed)
            turn(speed,1.0)
        if (arg== "5"):
            print ('--> turn l',speed)
            turn(speed,-1.0)
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
            time.sleep(duration)
        if (arg== "13"):
            print ('--> move backward')
            speed = int(input("Enter Speed : "))
            duration = int(input("Enter duration (sec): "))
            print("Speed:", speed)
            moveWeel(int(speed))
            time.sleep(duration)
        if (arg== "14"):
            print ('--> turn r',speed)
            speed = int(input("Enter Speed : "))
            print ('--> turn l',-speed)
            turn(-speed,1.0)
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
            lMail = Label(fenster, text='Enter Email:', bg='#9FD996').grid(row=0, column=0, pady = 2)
            lPassword = Label(fenster, text='Enter Password:', bg='#9FD996').grid(row=1, column=0, pady = 2)
            eMail = Entry(fenster).grid(row=0, column=1)
            entry = Entry(fenster).grid(row=1, column=1)

            bCancel = Button(fenster,text='Cancel', command=close).grid(row=3, column=0)
            bSave = Button(fenster,text='Login', command=button_save).grid(row=3, column=1)
        
        if (arg== "21"):
            # Trigger the servo when an object comes wicthin 30cm (the threshold distqnce).
            ultrasonic_sensor.when_in_range = triggerServo
            measure();
            # signal.raise_signal(signal.SIGUSR1)
            repeat = True
            if not alarm_set:
                print("set alarm !!! ")
                signal.alarm(tik)
                alarm_set = True;
            time.sleep(2.0)

        if (arg== "22"):
            repeat = True
            if not usr1_set:
                print("set usr1!!! ")
                signal.raise_signal(signal.SIGUSR1)
                usr1_set = True
            time.sleep(2.0)

        if (arg== "30"):
            measure()
            print("check term:", redLight)
            floatNumber=ultrasonic_sensor.distance
            if floatNumber < 0.20:
                stopWeel()
                print("redLight")
                collision(speed/2,1)
                repeat = True
            else:
                repeat = True
                moveWeel(speed)
            time.sleep(0.2)
terminate()
