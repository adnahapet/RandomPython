import RPi.GPIO as GPIO
import time



#assigns board numbers
blinkPin = 17
buttonPin = 19
binaryOnePin = 27
binaryTwoPin = 22
binaryFourPin = 26


#sets GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#init setup for each i/o
GPIO.setup(blinkPin,GPIO.OUT)
GPIO.setup(buttonPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(binaryOnePin,GPIO.OUT)
GPIO.setup(binaryTwoPin,GPIO.OUT)
GPIO.setup(binaryFourPin,GPIO.OUT)


#function takes frequency for blinker, stage number, and 0n or Off for the binary stage indicators 
def blink(x, stage, onePin, twoPin, fourPin):
        p=GPIO.PWM(blinkPin, x)
	GPIO.add_event_detect(19,GPIO.FALLING)  #looks for button press to pause
	p.start(1)
	GPIO.output(binaryOnePin, onePin)
	GPIO.output(binaryTwoPin, twoPin)
	GPIO.output(binaryFourPin, fourPin)
	t_end = time.time() + 5
	while time.time() <t_end:
                print ('stage ' + str(stage))
                if GPIO.event_detected(19):
                        print ('paused at stage ' + str(stage))
                        time.sleep(.02)
                        GPIO.wait_for_edge(19,GPIO.FALLING)
                        print('unpausing')
                        GPIO.remove_event_detect(19)            #removes and then adds event detect to prevent bouncing
                        GPIO.add_event_detect(19,GPIO.FALLING)
                        t_end = time.time()+5                   #extends stage for 5 more seconds
	p.stop()
	GPIO.remove_event_detect(19)
        



def main():
	try:               #5 stages at varying frequencies
                while True:
                        blink(1,1,GPIO.HIGH,GPIO.LOW,GPIO.LOW)
                        blink(2,2,GPIO.LOW,GPIO.HIGH,GPIO.LOW)
                        blink(4,3,GPIO.HIGH,GPIO.HIGH,GPIO.LOW)
                        blink(8,4,GPIO.LOW,GPIO.LOW,GPIO.HIGH)
                        blink(16,5,GPIO.HIGH,GPIO.LOW,GPIO.HIGH)
	except KeyboardInterrupt:          #ctrl+c to exit
                GPIO.cleanup()
		pass


main()


