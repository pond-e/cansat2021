###############ローバーの設定###################
houkou_rad = 0.52
max     = -100
counter = 0
count_limit = 50
h_first     = -1
counter_h   = 0
min     = 1000
GPIO.setmode(GPIO.BCM)
#GPIO4を出力端子設定
GPIO.setup(4, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)

#GPIO4をPWM設定、周波数は50Hz
p1 = GPIO.PWM(4,50)
p2 = GPIO.PWM(5,50)
p3 = GPIO.PWM(6,50)

#Duty Cycle 0%
p1.start(0.0)
p2.start(0.0)
p3.start(0.0)

###########ローバーのflag設定########
flag_r = False
flag_p = False
flag_t = False
gosa_l = 0.5184
gosa_s = 0.4489

###################ローバ制御#########################
def para():
    dc3=0.035
    p3.ChangeDutyCycle(dc3)
    time.sleep(0.5)
    p3.ChangeDutyCycle(0.0)

def north_raspi(mag):
    if(mag[0]<10 and mag[0]>-30):
        if(mag[1]<50 and mag[1]>10):
            #時計回り（左）
            dc2 = 0.115
            p2.ChangeDutyCycle(dc2)
            time.sleep(0.4)
            p2.ChangeDutyCycle(0.0)
        elif(mag[1]<=10 and mag[1]>-10):
            #半時計回り（右）
            dc1 = 0.035
            p1.ChangeDutyCycle(dc1)
            time.sleep(0.4)
            p1.ChangeDutyCycle(0.0)
        else:
            #そもまま
            dc1 = 0.035
            p1.ChangeDutyCycle(dc1)
            dc2 = 0.115
            p2.ChangeDutyCycle(dc2)
            time.sleep(0.4)
            p1.ChangeDutyCycle(0.0)
            p2.ChangeDutyCycle(0.0)
    elif(mag[0]<30 and mag[0]>=10):
        if(mag[1]<10 and mag[1]>-10):
            #半時計回り（右）
            dc1 = 0.035
            p1.ChangeDutyCycle(dc1)
            time.sleep(0.4)
            p1.ChangeDutyCycle(0.0)
        else:
            #そもまま
            dc1 = 0.035
            p1.ChangeDutyCycle(dc1)
            dc2 = 0.115
            p2.ChangeDutyCycle(dc2)
            time.sleep(0.4)
            p1.ChangeDutyCycle(0.0)
            p2.ChangeDutyCycle(0.0)
    else:
        #そもまま
        dc1 = 0.035
        p1.ChangeDutyCycle(dc1)
        dc2 = 0.115
        p2.ChangeDutyCycle(dc2)
        time.sleep(0.4)
        p1.ChangeDutyCycle(0.0)
        p2.ChangeDutyCycle(0.0)

Servo_pin = 33

GPIO.setup(Servo_pin, GPIO.OUT)

Servo = GPIO.PWM(Servo_pin, 50)
Servo.start(0)
def servo_angle(angle):
    duty=2.5+(11.5-3.5)*(angle+90)/180
    duty=7.5
    Servo.ChangeDutyCycle(duty)
    time.sleep(0.3)
