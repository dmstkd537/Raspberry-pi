from gpiozero import Motor
from time import sleep
import keyboard

#모터 핀 셋팅
motorR = Motor(forward=12, backward=13) # 모터 객체 생성

def stop_motor():
    motorR.stop()
    print("긴급정지")
    exit()

keyboard.add_hotkey('t', stop_motor)

# speed 변수에 0~1 사이의 값을 넣어서 속도를 조절할 수 있다 수가 클수록 빠름
#3초 동안 전진
motorR.forward(speed=0.7)
print("3초 전진후 정지합니다")
sleep(3)

#3초 동안 후진tttttt
motorR.backward(speed=0.7)
print("3초 후진후 정지합니다")
sleep(3)
print("정지")

#3초 동안 좌회전
motorR.forward(0.7)
print("3초 좌회전 후 정지합니다")
sleep(3)
print("정지")

#3초 동안 우회전
motorR.backward(speed=0.7)
print("3초 우회전 후 정지합니다")

#모터 정지
motorR.stop()
print("정지")

def stop_motor():
    motorR.stop()
    print("긴급정지")
    exit()