# Arduino example 8
Tutorial 8. Potentiometer with Servo Motor\
Potentiomete의 움직임에 따라 Servo motor의 각도가 변하도록 제작

## circuit
Potentiometer : analog 0pin\
Servo Motor : digital 9pin\
![image](https://user-images.githubusercontent.com/79436159/109211965-4f3b2800-77f2-11eb-90d7-03e77892e377.png)

## code
``` from pyfirmata import Arduino,util ```\
pyfirmata의 아두이노 모듈을 사용하기 위해 import함

``` import time ```\
프로그램을 일정시간동안 지연시키기위해 time 모듈을 import함

``` board = Arduino('COM8')``` \
변수1 = Arduino('**포트번호**') 를 해서 보드와 연결 

``` analog_input = board.get_pin('a:0:i')``` \
  -> 0번핀을 analog신호 입력핀으로 설정\

 ```led = board.get_pin('d:9:s') ```\
  -> 9번 핀을 digital신호 신호핀으로 설정\
  신호핀으로 설정하면 sevor motor에 신호를 주는 핀으로 설정됨
  
 ```
def move_servo(v):
  servo.write(v)
  board.pass_time(DELAY)
```
모터를 움직이게 하는 함수 작성\
원하는 각도를 입력으로 주고 DELAY변수만큼 지연시킴
  
