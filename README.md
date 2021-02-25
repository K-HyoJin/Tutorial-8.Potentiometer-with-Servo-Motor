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
  -> 0번핀을 analog신호 입력핀으로 설정

 ```led = board.get_pin('d:9:s') ```\
  -> 9번 핀을 digital신호 신호핀으로 설정\
  신호핀으로 설정하면 sevor motor에 신호를 주는 핀으로 설정됨
  
``` it = util.Iterator(board) ```\
보드의 입력값을 지속적으로 업데이트해주는 iterator 변수 선언

 ``` it.start()``` \
iterator 시작

 ```
def move_servo(v):
  servo.write(v)
  board.pass_time(DELAY)
```
모터를 움직이게 하는 함수 작성\
원하는 각도를 입력으로 주고 DELAY변수만큼 지연시킴
  

``` analog_value = analog_input.read() ```\
Potentiometer와 연결된 0번핀의 입력을 읽어와서 변수 analog_value에 저장

```
 for i in range(1):
   if analog_value is None:
      time.sleep(0.1)
      break
```    
입력으로 들어온 analog_value 값이 None이 아니면 0.1초동안 지연시키고 for문을 빠져나감

```      
   if analog_value < 0.5:
      move_servo(30)
      move_servo(0)
   if (analog_value > 0.5 and analog_value < 0.7):
      move_servo(100)
      move_servo(0)
   if analog_value > 0.7:
      move_servo(170)
      move_servo(0)
```
analogd_value값이 0.5보다 작으면 servo motor의 각도가 30도 → 0도로 변화\
0.5보다 크고 0.7보다 작으면 servo motor의 각도가 100도 → 0도로 변화\
0.7보다 크면 servo motor의 각도가 170도 → 0도로 변화



