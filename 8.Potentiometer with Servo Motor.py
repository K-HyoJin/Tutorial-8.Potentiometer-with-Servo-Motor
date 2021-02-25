from pyfirmata import Arduino,util
import time

#핀 모드설정
board = Arduino('COM8')
analog_input= board.get_pin('a:0:i') # 0번핀 입력
servo = board.get_pin('d:9:s') # 9번핀 서보모터의 신호선으로 설정

it = util.Iterator(board) # 회로의 입력상태를 읽어올 변수 선언
it.start()

#모터 작동 함수 작성 
def move_servo(v):
    servo.write(v)
    board.pass_time(1)
    
while True:
    analog_value = analog_input.read()
    print(analog_value)
    for i in range(1):
        if analog_value is None:
            time.sleep(0.1)
            break
        if analog_value < 0.5:
            move_servo(30)
            move_servo(0)
        if (analog_value > 0.5 and analog_value < 0.7):
            move_servo(100)
            move_servo(0)
        if analog_value > 0.7:
            move_servo(170)
            move_servo(0)
