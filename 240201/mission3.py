import RPi.GPIO as GPIO
import time
import random

led_pins = [4, 5, 6]
sw1 = 22
sw2 = 23
sw3 = 24
buzzer = 18

#핀 모드 설정
GPIO.setmode(GPIO.BCM)
for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)
GPIO.setup(sw1, GPIO.IN)
GPIO.setup(sw2, GPIO.IN)
GPIO.setup(sw3, GPIO.IN)
GPIO.setup(buzzer, GPIO.OUT)

#LED 초기화
GPIO.output(led_pins, GPIO.LOW)

total = 0

randColor = [led_pins]

    
for i in range(10):  # 10회 반복
        judgment = 0  # 판정 1 : 버튼을 올바르게 눌렀는지
        judgment2 = 0  # 판정 2 : 시간내에 버튼을 눌렀는지 아닌지

        # 색 랜덤으로 출력하기
        color = randColor[random.randint(0, 2)]
        # 랜덤 시간 설정하기
        sleep_time = random.uniform(0.5, 1.0)

        GPIO.output(color, GPIO.HIGH)

        start_time = time.time()
        while True:  # 랜덤 시간 만큼 반복
            ret = GPIO.input(sw1)  # 빨강 - SW2
            if ret == 0:
                judgment2 = 1
                if color != led_pins:
                    judgment = 1
            ret = GPIO.input(sw2)
            if ret == 0:
                judgment2 = 1
                if color != led_pins:
                    judgment = 1
            ret = GPIO.input(sw3)
            if ret == 0:
                judgment2 = 1
                if color != led_pins:
                    judgment = 1

            current_time = time.time()
            if current_time - start_time >= sleep_time:  # 지정한 시간이 지나면 종료
                break

        if judgment == 1:
            print("bad")
            #GPIO.output(buzzer, 1)
            #time.sleep(0.1)
            #GPIO.output(buzzer, 0)
        elif judgment2 == 0:
                print("miss")
        else:
            total += 1
        print("perfect")
        GPIO.output(color, GPIO.LOW)
print("최종 점수는 " + str(total) + "점")  # 최종 점수 출력

GPIO.cleanup()