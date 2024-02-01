import RPi.GPIO as GPIO
import time

buzzer = 18  # 부저에 연결된 핀 번호 18
GPIO.setmode(GPIO.BCM)  # 사용할 GPIO SETUP
GPIO.setup(buzzer, GPIO.OUT)  # 부저 출력

pwm = GPIO.PWM(buzzer, 1.0)  # 초기 주파수를 1Hz로 설정
pwm.start(1.0)  # 듀티비를 90프로로 설정(음 구분이 잘 되고 부드럽게 들림)

print("==== 동요 : 창밖을 보라 ====\n")  # 동요 제목

# 5옥타브 : 도(1) 레(2) 미(3) 파(4) 솔(5) 라(6) 시(7) 도(8), 레(9)
scale = [523.2511, 587.3295, 659.2551, 698.4565, 783.9908, 880, 987.7666, 1046.502, 1174.659, 1318.510]
look_outside = [5, 5, 5, 5, 3, 5, 5, 5, 5, 3, 5, 5, 3, 8, 7, 9,
                9, 9, 9, 8, 7, 7, 7, 7, 6, 5, 5, 5, 4, 4, 3, 5, 5, 5, 3, 5, 5, 5, 5, 3,
                5, 5, 3, 5, 5, 8, 8, 7, 9, 9, 9, 9, 8, 7, 7, 7, 7, 6,
                5, 5, 5, 6, 7, 8, 4, 1, 4, 6, 8, 8, 8, 5, 3, 1, 3, 5, 4, 1, 4, 6, 8, 8, 8,
                8, 9, 8, 7, 6, 5, 6, 7, 5, 5, 5, 5, 3, 5, 5, 5, 5, 3, 5, 5, 3, 5, 8, 7, 
                9, 9, 9, 9, 8, 7, 7, 7, 7, 6, 5, 5, 5, 6, 7, 8]

try:
    for i in range(0, 126):  # 리스트 길이에 맞게 변경
        # 음계 인덱스 확인 후 주파수 변경
        if 0 <= int(look_outside[i]) - 1 < len(scale):
            pwm.ChangeFrequency(scale[int(look_outside[i]) - 1])
            if i == 16 or i == 32 or i == 50 or i == 66 or i == 78 or i == 109 or i == 125:  
                time.sleep(1.0)
            else:
                time.sleep(0.5)
except IndexError as e:
    print(f"에러가 발생했습니다: {e}")
finally:
    pwm.stop()
    GPIO.cleanup()