import RPi.GPIO as GPIO
import time

led_red = 4  # led_red GPIO 4번과 연결
led_green = 5  # led_green GPIO 5번과 연결

GPIO.setmode(GPIO.BCM)  # BCM으로 사용
GPIO.setup(led_red, GPIO.OUT)  # led_red 출력으로 설정
GPIO.setup(led_green, GPIO.OUT)  # led_green 출력으로 설정

def toggle_led(led_pin, led_name, on_message, off_message):
    GPIO.output(led_pin, not GPIO.input(led_pin))
    print(f"{led_name} {on_message if GPIO.input(led_pin) else off_message}")

try:
    while True:
        # Red LED 켜고 꺼지기
        toggle_led(led_red, 'Red', 'On', 'Off')
        time.sleep(0.7)

        # Green LED 켜고 꺼지기
        toggle_led(led_green, 'Green', 'On', 'Off')
        time.sleep(0.7)

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
    print("GPIO 리소스를 정리하고 프로그램을 종료합니다.")