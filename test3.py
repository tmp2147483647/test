
# -*- coding: utf-8 -*- 
######################################################################
### Date: 2017/10/26
### Purpose: this code has been generated for the three-wheeled moving
###         object to go forward and backward
### this code is used for the student only
######################################################################

#GPIO  library를 임포트 한다.
import RPi.GPIO as GPIO 
from time import sleep

# =======================================================================
#좌우측 모터 드라이버와 연결되는 GPIO 핀 6개를 할당한다.
#좌우측 모터 전진/후진 결정 변수:(MotorLeft_A, MotorLeft_B), (MotorRight_A, MotorRight_B)
#좌우측 모터 속도 결정 변수: MotorLeft_PWM, MotorRight_PWM:

MotorLeft_A=12
MotorRight_A = 15 
MotorLeft_B = 11
MotorRight_B = 13
MotorLeft_PWM = 35
MotorRight_PWM = 37
go=1
back=0


#전진이나 후진 함수는 간단하기 때문에 풀어서 써 보았다.
def Go():    
    GPIO.output(MotorLeft_A, GPIO.HIGH)
    GPIO.output(MotorLeft_B, GPIO.LOW)
    GPIO.output(MotorRight_A, GPIO.LOW)
    GPIO.output(MotorRight_B, GPIO.HIGH)
    GPIO.output(MotorLeft_PWM,GPIO.HIGH)
    GPIO.output(MotorRight_PWM,GPIO.HIGH)

def Back():
    GPIO.output(MotorLeft_A, GPIO.LOW)
    GPIO.output(MotorLeft_B, GPIO.HIGH)
    GPIO.output(MotorRight_A, GPIO.HIGH)
    GPIO.output(MotorRight_B, GPIO.LOW)
    GPIO.output(MotorLeft_PWM,GPIO.HIGH)
    GPIO.output(MotorRight_PWM,GPIO.HIGH)

def LeftMotor(val):
    if val ==1:
        GPIO.output(MotorLeft_A, GPIO.HIGH)
        GPIO.output(MotorLeft_B, GPIO.LOW)
        GPIO.output(MotorLeft_PWM,GPIO.HIGH)
        GPIO.output(MotorRight_PWM,GPIO.HIGH)
    elif val ==0:
        GPIO.output(MotorLeft_A, GPIO.LOW)
        GPIO.output(MotorLeft_B, GPIO.HIGH)
        GPIO.output(MotorLeft_PWM,GPIO.HIGH)
        GPIO.output(MotorRight_PWM,GPIO.HIGH)
    else:
        print("Config Error")

def RightMotor(val):
    if val ==1:
        GPIO.output(MotorRight_A, GPIO.LOW)
        GPIO.output(MotorRight_B, GPIO.HIGH)
        GPIO.output(MotorLeft_PWM,GPIO.HIGH)
        GPIO.output(MotorRight_PWM,GPIO.HIGH)
    elif val==0:
        GPIO.output(MotorRight_A, GPIO.HIGH)
        GPIO.output(MotorRight_B, GPIO.LOW)
        GPIO.output(MotorLeft_PWM,GPIO.HIGH)
        GPIO.output(MotorRight_PWM,GPIO.HIGH)
    else:
        print("Config Error")
        
        
    

# BOARD 모드 BCM 모드 중 BOARD 모드를 선택한다.
# 에러 메시지가 아닌 이상 경고 메시지는 나타나지 않도록 한다.
#라즈베리 파이가 GPIO 핀을 통해 좌측,우측 모터에 출력을 내보냄
#드라이브 에게 출력하는 역할을 함 (OUT으로 설정)
def SetUp():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(MotorLeft_A,GPIO.OUT)
    GPIO.setup(MotorLeft_B,GPIO.OUT)
    GPIO.setup(MotorLeft_PWM,GPIO.OUT)
    GPIO.setup(MotorRight_A,GPIO.OUT)
    GPIO.setup(MotorRight_B,GPIO.OUT)
    GPIO.setup(MotorRight_PWM,GPIO.OUT)
    RightPwm=GPIO.PWM(MotorRight_PWM,100)
    LeftPwm=GPIO.PWM(MotorLeft_PWM,100)
    return LeftPwm,RightPwm
def go_forward(speed, running_time):
    Go()    
    LeftPwm.ChangeDutyCycle(speed)
    RightPwm.ChangeDutyCycle(speed)
    sleep(running_time)

def go_backward(speed, running_time):
    Back()
    LeftPwm.ChangeDutyCycle(speed)
    RightPwm.ChangeDutyCycle(speed)
    sleep(running_time)

#def PointTurn(speed, running_time):



def SwingTurn(Direction, speed, running_time):
    if Direction == 'R':
        LeftMotor(1)
        GPIO.output(MotorRight_PWM,GPIO.LOW)
        LeftPwm.ChangeDutyCycle(speed)
        RightPwm.ChangeDutyCycle(0)
    elif Direction == 'L':
        RightMotor(1)
        GPIO.output(MotorLeft_PWM,GPIO.LOW)
        RightPwm.ChangeDutyCycle(speed)
        LeftPwm.ChangeDutyCycle(0)

def PointTurn(Direction, speed, running_time):
    if Direction == 'R':
        LeftMotor(1)
        RightMotor(0)
        LeftPwm.ChangeDutyCycle(speed)
        RightPwm.ChangeDutyCycle(speed)
    elif Direction == 'L':
        LeftMotor(0)
        RightMotor(1)
        LeftPwm.ChangeDutyCycle(speed)
        RightPwm.ChangeDutyCycle(speed)
    sleep(running_time)
# =======================================================================

# =======================================================================
# define the stop module
def stop():
    # the speed of left motor will be set as LOW
    GPIO.output(MotorLeft_PWM,GPIO.LOW)
    # the speed of right motor will be set as LOW
    GPIO.output(MotorRight_PWM,GPIO.LOW)
    # left motor will be stopped with function of ChangeDutyCycle(0)
    LeftPwm.ChangeDutyCycle(0)
    # left motor will be stopped with function of ChangeDutyCycle(0)
    RightPwm.ChangeDutyCycle(0)
# =======================================================================

# =======================================================================
# mission has been started as below
if __name__=="__main__":
    try:
        LeftPwm,RightPwm=SetUp()
       
        LeftPwm.start(0)
        RightPwm.start(0)
        go_forward(40, 3)
        sleep(1)
        go_backward(40, 3)
        sleep(1)
        PointTurn('R',40,3)
        #SwingTurn('R',40,3)
        sleep(1)
        stop()
    except KeyboardInterrupt:
        # the speed of left motor will be set as LOW
        GPIO.output(MotorLeft_PWM,GPIO.LOW)
        # left motor will be stopped with function of ChangeDutyCycle(0)
        LeftPwm.ChangeDutyCycle(0)
        # the speed of right motor will be set as LOW
        GPIO.output(MotorRight_PWM,GPIO.LOW)
        # right motor will be stopped with function of ChangeDutyCycle(0)
        RightPwm.ChangeDutyCycle(0)
        # GPIO pin setup has been cleared
        GPIO.cleanup()
# =======================================================================
