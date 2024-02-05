from flask import Flask
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

red_pin = 14
green_pin = 15
blue_pin = 18
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)

app = Flask(__name__)

@app.route('/')
def hello():
    return "LED 제어를 위해 주소창을 변경하세요"

@app.route('/red_on')
def red_on():
    GPIO.output(red_pin, GPIO.HIGH)
    return "red Led on"

@app.route('/green_on')
def green_on():
    GPIO.output(green_pin, GPIO.HIGH)
    return "green led on"

@app.route('/blue_on')
def blue_on():
    GPIO.output(blue_pin, GPIO.HIGH)
    return "blue LED on"

@app.route('/off')
def off():
    GPIO.output(red_pin, GPIO.LOW)
    GPIO.output(green_pin, GPIO.LOW)
    GPIO.output(blue_pin, GPIO.LOW)
    return "all LED off"

@app.route('/clean_up')
def clean_up():
    GPIO.cleanup()
    return "clean up"

if __name__ == "__main__":
    app.run(host = "192.168.0.181", port = "8080")
