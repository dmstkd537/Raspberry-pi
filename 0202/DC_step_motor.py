import RPi.GPIO as GPIO
import time

STEP_OUTA = 16
STEP_OUTB = 17
STEP_OUT2A = 18
STEP_OUT2B = 19

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(STEP_OUTA, GPIO.OUT)
    GPIO.setup(STEP_OUTB, GPIO.OUT)
    GPIO.setup(STEP_OUT2A, GPIO.OUT)
    GPIO.setup(STEP_OUT2B, GPIO.OUT)

    print("Step Motor Control Start !!")

    try:
        for i in range(2000):
            GPIO.output(STEP_OUTA, 1)
            time.sleep(0.19)
            GPIO.output(STEP_OUTA, 0)
            GPIO.output(STEP_OUTB, 1)
            time.sleep(0.19)
            GPIO.output(STEP_OUTB, 0)
            GPIO.output(STEP_OUT2A, 1)
            time.sleep(0.19)
            GPIO.output(STEP_OUT2A, 0)
            GPIO.output(STEP_OUT2B, 1)
            time.sleep(0.19)
            GPIO.output(STEP_OUT2B, 0)

    except KeyboardInterrupt:
        pass

    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()