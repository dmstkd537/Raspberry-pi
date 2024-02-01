import RPi.GPIO as GPIO
import time

buzzer = 18  # 부저에 연결된 핀 번호 18
GPIO.setmode(GPIO.BCM)  # 사용할 GPIO SETUP
GPIO.setup(buzzer, GPIO.OUT)  # 부저 출력

pwm = GPIO.PWM(buzzer, 1.0)  # 초기 주파수를 1Hz로 설정
pwm.start(1.0)  # 듀티비를 90프로로 설정(음 구분이 잘 되고 부드럽게 들림)

print("==== 동요 : 비행기 ====\n")  # 동요 제목

# 5옥타브 : 도(1) 레(2) 미(3) 파(4) 솔(5) 라(6) 시(7) 도(8), 레(9)
scale = [523.2511, 587.3295, 659.2551, 698.4565, 783.9908, 880, 987.7666, 1046.502, 1174.659, 1318.510]
airplane = [3, 2, 1, 2, 3, 3, 3, 2, 2, 2, 3, 3, 3, \
                  3, 2, 1, 2, 3, 3, 3, 2, 2, 3, 2, 1]

try:
    for i in range(0, 25):  # 리스트 길이에 맞게 변경
        # 음계 인덱스 확인 후 주파수 변경
        if 0 <= airplane[i] - 1 < len(scale):
            pwm.ChangeFrequency(scale[airplane[i] - 1])
            if i == 6 or i == 13 or i == 20 or i == 27:
                time.sleep(1.0)
            else:
                time.sleep(0.5)
        else:
            print(f"유효하지 않은 음계 인덱스입니다: {airplane[i]}")

except IndexError as e:
    print(f"에러가 발생했습니다: {e}")
finally:
    pwm.stop()
    GPIO.cleanup()