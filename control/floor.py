import RPi.GPIO as GPIO
from control import LED_PIN


def is_on():
    return GPIO.input(LED_PIN) == 1


def switch_on():
    GPIO.output(LED_PIN, True)


def switch_off():
    GPIO.output(LED_PIN, False)


