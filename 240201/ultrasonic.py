import RPi.GPIO as GPIO
import time

trigPin = 20
echoPin = 21

def trig():
    GPIO.output(trigPin, GPIO.LOW)
    time.sleep(0.002)
    GPIO.output(trigPin, GPIO.HIGH)
    time.sleep(0.00002)
    GPIO.output(trigPin, GPIO.LOW)
    GPIO.output(trigPin, GPIO.LOW)
    
    while GPIO.input(echoPin) == 0:
        start = time.time()

    while GPIO.input(echoPin) == 1:
        end = time.time()

    duration = end - start
    distance = duration * 34300 /2

    return distance

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(trigPin, GPIO.OUT)
    GPIO.setup(echoPin, GPIO.IN)

    print("warning unidentified detecting!!")
    for i in range(20):
        distance = trig()
        print(f"unidentified object :{distance:2f}cm")
        time.sleep(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()