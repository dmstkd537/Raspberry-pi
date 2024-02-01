import RPi.GPIO as GPIO
import time

buzzer = 18  # 부저에 연결된 핀 번호 18
GPIO.setmode(GPIO.BCM)  # 사용할 GPIO SETUP
GPIO.setup(buzzer, GPIO.OUT)  # 부저 출력

pwm = GPIO.PWM(buzzer, 1.0)  # 초기 주파수를 1Hz로 설정
pwm.start(5.0)  # 듀티비를 90프로로 설정(음 구분이 잘 되고 부드럽게 들림)

print("==== 동요 : 옥수수 하모니카 ====\n")  # 동요 제목

# 5옥타브 : 도(1) 레(2) 미(3) 파(4) 솔(5) 라(6) 시(7) 도(8), 레(9)
scale = [523.2511, 587.3295, 659.2551, 698.4565, 783.9908, 880, 987.7666, 1046.502, 1174.659, 1318.510]
corn_harmonica = [1, 3, 2, 1, 5, 6, 5, 5, 6, 8, 7, 6, 5, 3, 4, 5, 6, \
                  5, 5, 3, 1, 2, 2, 2, 3, 2, 1, 3, 2, 1, 5, 6, 5, 5, 6, 8, 7, 6, 5, \
                  8, 9, 8, 6, 5, 6, 5, 3, 2, 2, 5, 5, 3, 1, 2, 3, 4, 5, 6, 7, 8, \
                  9, 1, 7, 6, 5, 1, 3, 5, 8, 8, 5, 3, 1, 2, 2, 5, 5, 1]

try:
    for i in range(0, 79):
        # 음계 인덱스 확인 후 주파수 변경
        if 0 <= corn_harmonica[i] < len(scale):
            pwm.ChangeFrequency(scale[corn_harmonica[i]])
            if i == 13 or i == 26 or i == 39 or i == 52 or i == 65:
                time.sleep(1.0)
            else:
                time.sleep(0.5)
        else:
            print(f"유효하지 않은 음계 인덱스입니다: {corn_harmonica[i]}")

except IndexError as e:
    print(f"에러가 발생했습니다: {e}")
finally:
    pwm.stop()
    GPIO.cleanup()