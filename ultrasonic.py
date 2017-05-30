
import time
import RPi.GPIO as GPIO
while True:
    # Use BCM GPIO references
    # instead of physical pin numbers
    GPIO.setmode(GPIO.BCM)

    # Define GPIO to use on Pi
    GPIO_TRIGGER = 23
    GPIO_ECHO    = 24

    # Speed of sound in cm/s at temperature
    temperature = 20
    speedSound = 33100 + (0.6*temperature)

    print("Ultrasonic Measurement")
    print("Speed of sound is",speedSound/100,"m/s at ",temperature,"deg")

    # Set pins as output and input
    GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
    GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo

    # Set trigger to False (Low)
    GPIO.output(GPIO_TRIGGER, False)

    # Allow module to settle
    time.sleep(0.5)

    # Send 10us pulse to trigger
    GPIO.output(GPIO_TRIGGER, True)
    # Wait 10us
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    start = time.time()

    while GPIO.input(GPIO_ECHO)==0:
        start = time.time()

    while GPIO.input(GPIO_ECHO)==1:
        stop = time.time()

    # Calculate pulse length
    elapsed = stop-start

    # Distance pulse travelled in that time is time
    # multiplied by the speed of sound (cm/s)
    distance = elapsed * speedSound

    # That was the distance there and back so halve the value
    distance = distance / 2

    print("Distance : {0:5.1f}".format(distance))

    # Reset GPIO settings
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(10,GPIO.OUT)
    if distance<5:
        GPIO.output(10,False) #Turn off motor if the distance from the roof of tank is 5 cm.
    elif distance>90:
        GPIO.output(10,True) #Turn on motor if the distance from the roof of tank is 90 cm.
