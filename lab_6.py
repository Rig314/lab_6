def lab_6():
    from gpiozero import Button
from picamera import PiCamera
from datetime import datetime
from signal import pause
button = Button(2)
camera = PiCamera()
def capture():
 timestamp = datetime.now().isoformat()
 camera.capture('/home/pi/%s.jpg' % timestamp)
button.when_pressed = capture
pause()

#distance sensor
from gpiozero import DistanceSensor
from time import sleep
sensor = DistanceSensor(23, 24)
while True:
 print('Distance to nearest object is', sensor.distance, 'm')
 sleep(1)
 
#servo
 
 from gpiozero import AngularServo
from time import sleep
btn = Button(2)
servo = AngularServo(17, min_angle=-90, max_angle=90)
while True:
 servo.angle = -90
 btn.wait_for_press()
 servo.angle = -45
 btn.wait_for_press()
 servo.angle = 0
 btn.wait_for_press()
 servo.angle = 45
 btn.wait_for_press()
 servo.angle = 90
 btn.wait_for_press()

    
    
    
    
    
    
if_name_=='_main_':
    lab_6()    