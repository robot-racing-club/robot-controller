import RPi.GPIO as GPIO
from signal import pause
from time import sleep

PIN_IN1 = 25
PIN_IN2 = 7
PIN_IN3 = 24
PIN_IN4 = 23

PIN_PWM1 = 21
PIN_PWM2 = 20

GPIO.setmode(GPIO.BCM)

GPIO.setup(PIN_IN1, GPIO.OUT)
GPIO.setup(PIN_IN2, GPIO.OUT)
GPIO.setup(PIN_IN3, GPIO.OUT)
GPIO.setup(PIN_IN4, GPIO.OUT)

GPIO.setup(PIN_PWM1, GPIO.OUT)
GPIO.setup(PIN_PWM2, GPIO.OUT)

pwm1 = GPIO.PWM(PIN_PWM1, 100)
pwm2 = GPIO.PWM(PIN_PWM2, 100)


def backward(speed):
    GPIO.output(PIN_IN1, GPIO.HIGH)
    GPIO.output(PIN_IN2, GPIO.LOW)
    GPIO.output(PIN_IN3, GPIO.HIGH)
    GPIO.output(PIN_IN4, GPIO.LOW)
    pwm1.ChangeDutyCycle(speed)
    pwm2.ChangeDutyCycle(speed)


def forward(speed):
    GPIO.output(PIN_IN1, GPIO.LOW)
    GPIO.output(PIN_IN2, GPIO.HIGH)
    GPIO.output(PIN_IN3, GPIO.LOW)
    GPIO.output(PIN_IN4, GPIO.HIGH)
    pwm1.ChangeDutyCycle(speed)
    pwm2.ChangeDutyCycle(speed)
