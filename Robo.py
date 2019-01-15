import RPi.GPIO as GPIO
import time

RIGHT_WHEEL = 38
LEFT_WHEEL = 40


GPIO.setmode(GPIO.BOARD)


GPIO.setup(RIGHT_WHEEL, GPIO.OUT)
GPIO.setup(LEFT_WHEEL, GPIO.OUT)

GPIO.output(RIGHT_WHEEL, True)
GPIO.output(LEFT_WHEEL, True)





def BACKWARD(frequency = (25, 50)):

    left = GPIO.PWM(LEFT_WHEEL, frequency[1])
    right = GPIO.PWM(RIGHT_WHEEL, frequency[0])

    left.start(5)
    right.start(5)

    time.sleep(1)



def FORWARD(frequency = (25, 50) ):
    left = GPIO.PWM(LEFT_WHEEL, frequency[0])
    right = GPIO.PWM(RIGHT_WHEEL, frequency[1])

    left.start(5)
    right.start(5)

    time.sleep(1)

def ROTATE_LEFT( frequency = (25, 50) ):

    left = GPIO.PWM(LEFT_WHEEL, frequency[1])
    right = GPIO.PWM(RIGHT_WHEEL, frequency[1])

    left.start(5)
    right.start(5)

    time.sleep(1)
    


def ROTATE_RIGHT( frequency = (25, 50) ):

    left = GPIO.PWM(LEFT_WHEEL, frequency[0])
    right = GPIO.PWM(RIGHT_WHEEL, frequency[0])

    left.start(5)
    right.start(5)

    time.sleep(1)




FORWARD()
BACKWARD()

ROTATE_LEFT()
ROTATE_RIGHT()

GPIO.cleanup()
